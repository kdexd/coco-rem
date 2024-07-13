from .cascade_mask_rcnn_convnext_base_1k_3x import dataloader, model, train

# This config is IDENTICAL to ConvNeXt-B (ImageNet-1K) - the only difference
# is pre-training dataset of backbone (ImageNet-22K vs 1K) but weights in,
# `train.init_checkpoint` (to be provided externally) override everything.
