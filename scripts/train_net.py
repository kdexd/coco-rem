"""
Train or evaluation a model using Detectron2-style lazy config.
"""

from __future__ import annotations

import argparse
import json
import logging
import warnings

import torch
from detectron2 import engine
from detectron2.checkpoint import DetectionCheckpointer
from detectron2.config import LazyConfig, instantiate
from detectron2.engine import hooks
from detectron2.engine.defaults import create_ddp_model
from detectron2.evaluation import inference_on_dataset, print_csv_format
from detectron2.evaluation.testing import flatten_results_dict
from detectron2.utils import comm

from coco_rem.data.builtin import register_all_coco_rem
from coco_rem.trainer import AMPWithGradAccumTrainer

warnings.filterwarnings("ignore")
logger = logging.getLogger("detectron2")


parser = engine.default_argument_parser(__doc__)
_AA = parser.add_argument
_AA("--checkpoint-period", type=int, default=5000, help="Checkpoint saving period.")
_AA("--log-period", type=int, default=10, help="Log training progress periodically.")


def do_test(_C, model):
    data_loader = instantiate(_C.dataloader.test)
    evaluator = instantiate(_C.dataloader.evaluator)

    results = inference_on_dataset(model, data_loader, evaluator)
    print_csv_format(results)
    return results


def main(_A: argparse.Namespace):
    # Register COCO-ReM dataset splits before starting the training job.
    register_all_coco_rem()

    _C = LazyConfig.load(_A.config_file)
    _C = LazyConfig.apply_overrides(_C, _A.opts)

    engine.default_setup(_C, _A)

    device = torch.cuda.current_device() if _A.num_gpus != 0 else torch.device("cpu")

    model = instantiate(_C.model).to(device)
    logger.info("Model:\n{}".format(model))

    model = create_ddp_model(model)
    DetectionCheckpointer(model).load(_C.train.get("init_checkpoint", None))

    if _A.eval_only:
        results = do_test(_C, model)
        if comm.is_main_process():
            results = flatten_results_dict(results)
            json.dump(results, open(f"{_C.train.output_dir}/eval_results.json", "w"))
        return

    train_loader = instantiate(_C.dataloader.train)

    _C.optimizer.params.model = model
    optim = instantiate(_C.optimizer)

    trainer_cls = AMPWithGradAccumTrainer if _C.train.amp else engine.SimpleTrainer
    trainer = trainer_cls(
        model, train_loader, optim, grad_accum_steps=_C.train.get("grad_accum_steps", 1)
    )
    checkpointer = DetectionCheckpointer(model, _C.train.output_dir, trainer=trainer)

    trainer.register_hooks(
        [
            hooks.IterationTimer(),
            hooks.LRScheduler(scheduler=instantiate(_C.lr_multiplier)),
            hooks.PeriodicCheckpointer(checkpointer, _A.checkpoint_period)
            if comm.is_main_process()
            else None,
            hooks.EvalHook(_A.checkpoint_period, lambda: do_test(_C, model)),
            hooks.PeriodicWriter(
                engine.default_writers(_C.train.output_dir, _C.train.max_iter),
                period=_A.log_period,
            )
            if comm.is_main_process()
            else None,
        ]
    )

    checkpointer.resume_or_load(_C.train.init_checkpoint, resume=_A.resume)
    if _A.resume and checkpointer.has_checkpoint():
        # The checkpoint stores the training iteration that just finished, thus we start
        # at the next iteration
        start_iter = trainer.iter + 1
    else:
        start_iter = 0
    trainer.train(start_iter, _C.train.max_iter)


if __name__ == "__main__":
    _A = parser.parse_args()
    engine.launch(
        main,
        num_gpus_per_machine=_A.num_gpus,
        num_machines=_A.num_machines,
        machine_rank=_A.machine_rank,
        dist_url=_A.dist_url,
        args=(_A,),
    )
