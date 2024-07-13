from detectron2.layers.batch_norm import NaiveSyncBatchNorm

from ..common.coco_schedule import lr_multiplier_100ep as lr_multiplier
from ..common.data.coco import dataloader
from ..common.data.constants import constants
from ..common.models.mask_rcnn_fpn import model
from ..common.optim import SGD as optimizer
from ..common.train import train

dataloader.train.mapper.image_format = "BGR"
model.pixel_mean = constants.imagenet_bgr256_mean
model.pixel_std = constants.imagenet_bgr256_std
model.input_format = "BGR"

# train from scratch
train.init_checkpoint = ""
train.amp.enabled = True
train.ddp.fp16_compression = True
model.backbone.bottom_up.freeze_at = 0

# SyncBN
model.backbone.bottom_up.stem.norm = "SyncBN"
model.backbone.bottom_up.stages.norm = "SyncBN"
model.backbone.norm = "SyncBN"

# Using NaiveSyncBatchNorm because heads may have empty input. That is not supported by
# torch.nn.SyncBatchNorm. We can remove this after
# https://github.com/pytorch/pytorch/issues/36530 is fixed.
model.roi_heads.box_head.conv_norm = lambda c: NaiveSyncBatchNorm(c, stats_mode="N")
model.roi_heads.mask_head.conv_norm = lambda c: NaiveSyncBatchNorm(c, stats_mode="N")

# 2conv in RPN:
model.proposal_generator.head.conv_dims = [-1, -1]

# 4conv1fc box head
model.roi_heads.box_head.conv_dims = [256, 256, 256, 256]
model.roi_heads.box_head.fc_dims = [1024]

# Equivalent to 100 epochs.
# 100 ep = 184375 iters * 64 images/iter / 118000 images/ep
train.max_iter = 184375

optimizer.lr = 0.1
optimizer.weight_decay = 4e-5
