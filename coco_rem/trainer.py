# Copyright (c) Facebook, Inc. and its affiliates.
from __future__ import annotations

import time
from contextlib import nullcontext

import torch
from detectron2.engine import SimpleTrainer
from detectron2.utils.events import get_event_storage
from torch.cuda.amp import GradScaler, autocast
from torch.nn.parallel import DistributedDataParallel


class AMPWithGradAccumTrainer(SimpleTrainer):
    """
    Like :class:`SimpleTrainer`, but uses PyTorch's native automatic mixed precision
    in the training loop and gradient accumulation after every `N` batches.
    """

    def __init__(
        self,
        model,
        data_loader,
        optimizer,
        gather_metric_period: int = 1,
        grad_scaler: GradScaler | None = None,
        precision: torch.dtype = torch.float16,
        log_grad_scaler: bool = False,
        grad_accum_steps: int = 1,
    ):
        """
        Args:
            model, data_loader, optimizer, gather_metric_period:
                same as in :class:`SimpleTrainer`.
            grad_scaler: torch GradScaler to automatically scale gradients.
            precision: torch.dtype as the target precision to cast to in computations.
            grad_accum_steps: Number of gradient accumulation steps.
        """
        unsupported = (
            "AMPTrainer does not support single-process multi-device training!"
        )
        if isinstance(model, DistributedDataParallel):
            assert not (model.device_ids and len(model.device_ids) > 1), unsupported

        super().__init__(model, data_loader, optimizer, gather_metric_period)

        if grad_scaler is None:
            grad_scaler = GradScaler()
        self.grad_scaler = grad_scaler
        self.precision = precision
        self.log_grad_scaler = log_grad_scaler

        assert grad_accum_steps >= 1, "grad_accum_steps must be >= 1."
        self.grad_accum_steps = grad_accum_steps
        self.grad_sync_manager = _GradAccumSyncManager(model, grad_accum_steps)

    def run_step(self):
        """
        Implement the AMP training logic along with gradient accumulation.
        """
        assert self.model.training, "[AMPTrainer] model was changed to eval mode!"

        start = time.perf_counter()
        self.optimizer.zero_grad()

        # Record data loading time for all batches during gradient accumulation.
        total_data_time = 0.0
        prev_data_time = start

        for _ in range(self.grad_accum_steps):
            # Load batch and accumulate total time to load all batches throughout
            # all steps of gradient accumulation.
            data = next(self._data_loader_iter)
            current_data_time = time.perf_counter()
            total_data_time += current_data_time - prev_data_time
            prev_data_time = current_data_time

            with self.grad_sync_manager, autocast(dtype=self.precision):
                loss_dict = self.model(data)
                if isinstance(loss_dict, torch.Tensor):
                    losses = loss_dict
                    loss_dict = {"total_loss": loss_dict}
                else:
                    losses = sum(loss_dict.values())

                normalized_losses = losses / self.grad_accum_steps
                self.grad_scaler.scale(normalized_losses).backward()

        if self.log_grad_scaler:
            storage = get_event_storage()
            storage.put_scalar("[metric]grad_scaler", self.grad_scaler.get_scale())

        self.after_backward()

        if self.async_write_metrics:
            # write metrics asynchronically
            self.concurrent_executor.submit(
                self._write_metrics, loss_dict, total_data_time, iter=self.iter
            )
        else:
            self._write_metrics(loss_dict, total_data_time)

        self.grad_scaler.step(self.optimizer)
        self.grad_scaler.update()

    def state_dict(self):
        ret = super().state_dict()
        ret["grad_scaler"] = self.grad_scaler.state_dict()
        return ret

    def load_state_dict(self, state_dict):
        super().load_state_dict(state_dict)
        self.grad_scaler.load_state_dict(state_dict["grad_scaler"])


class _GradAccumSyncManager:
    """
    Distributed training with gradient accumulation can cause huge slowdowns if
    gradient synchronization is not done properly. This context manager does it.
    When using DDP and accumulation for `N` steps, gradients are not averaged
    across process for first `N - 1` steps. This context manager behaves as
    a no-op (`nullcontext`) when any of these conditions are true:

        - Training with single GPU or CPU only (`model` is not DDP object)
        - DDP with static graph (see https://github.com/pytorch/pytorch/issues/80832)
        - No gradient accumulation across multiple steps (`num_steps = 1`)
    """

    def __init__(self, model, num_steps: int):
        """
        Args:
            model: PyTorch module that is being trained with gradient accumulation.
            num_steps: Number of batches processed to accumulate gradients.
        """
        self.num_steps = num_steps
        self.step = 0
        self._sync = nullcontext()

        if isinstance(model, DistributedDataParallel) and not model.static_graph:
            self._no_sync = model.no_sync()
        else:
            self._no_sync = nullcontext()

    def __enter__(self):
        return self._no_sync if self.step < self.num_steps - 1 else self._sync

    def __exit__(self, *args, **kwargs):
        self.step = (self.step + 1) % self.num_steps
