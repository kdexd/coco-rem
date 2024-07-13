from detectron2.config import LazyCall as L
from detectron2.solver import WarmupParamScheduler
from fvcore.common.param_scheduler import MultiStepParamScheduler


def default_lsj_epoch_scheduler(epochs: int):
    """
    Returns the config for a default multi-step LR scheduler that runs for fixed
    amount of COCO epochs, typically used with models using "LSJ" augmentations
    and training schedule (large-scale jittering augmentation and 50-400 epochs).
    """

    coco_100ep_iter = 184375
    coco_curr_iter = coco_100ep_iter * epochs // 100

    coco_100ep_milestones = [163889, 177546]
    coco_curr_milestones = [x * epochs // 100 for x in coco_100ep_milestones]

    lr_multiplier = L(WarmupParamScheduler)(
        scheduler=L(MultiStepParamScheduler)(
            values=[1.0, 0.1, 0.01],
            milestones=coco_curr_milestones,
            num_updates=coco_curr_iter,
        ),
        warmup_length=250 / coco_curr_iter,
        warmup_factor=0.001,
    )
    return lr_multiplier


lr_multiplier_75ep = default_lsj_epoch_scheduler(75)
lr_multiplier_100ep = default_lsj_epoch_scheduler(100)
lr_multiplier_200ep = default_lsj_epoch_scheduler(200)
lr_multiplier_400ep = default_lsj_epoch_scheduler(400)
