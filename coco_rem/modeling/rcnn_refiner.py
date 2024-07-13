# Copyright (c) Facebook, Inc. and its affiliates.
from __future__ import annotations

import torch

from detectron2.modeling.meta_arch.rcnn import GeneralizedRCNN


class GeneralizedRCNNRefiner(GeneralizedRCNN):
    """
    An extension of R-CNN that produces masks conditioned on box prompts. This
    model skips the region proposal network and box ROI head, running only the
    mask head by cropping ROI features using input boxes.
    """

    def forward(self, batched_inputs: list[dict[str, torch.Tensor]]):
        assert not self.training, "`GeneralizedRCNNRefiner` only supports inference!"

        # Prepare `detected_instances: list[Instances]` for `inference()` method
        # to get mask predictions for ground-truth boxes.
        detected_instances = [x.pop("instances") for x in batched_inputs]
        for x in detected_instances:
            x.pred_classes = x.gt_classes
            x.pred_boxes = x.gt_boxes
            x.scores = torch.ones_like(x.pred_classes).float()

        return self.inference(batched_inputs, detected_instances)
