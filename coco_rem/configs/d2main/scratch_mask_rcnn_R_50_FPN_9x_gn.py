from ..common.data.coco import dataloader
from ..common.data.constants import constants
from ..common.models.mask_rcnn_fpn import model
from ..common.train import train

dataloader.train.mapper.image_format = "BGR"
model.pixel_mean = constants.imagenet_bgr256_mean
model.pixel_std = constants.imagenet_bgr256_std
model.input_format = "BGR"

# Handle Caffe2 model specs:
model.backbone.bottom_up.stages.stride_in_1x1 = False
model.pixel_std = [57.375, 57.120, 58.395]

model.backbone.bottom_up.stem.norm = "GN"
model.backbone.bottom_up.stages.norm = "GN"
model.backbone.norm = "GN"
model.roi_heads.box_head.conv_norm = "GN"
model.roi_heads.mask_head.conv_norm = "GN"

# 4conv1fc box head
model.roi_heads.box_head.conv_dims = [256, 256, 256, 256]
model.roi_heads.box_head.fc_dims = [1024]

dataloader.train.total_batch_size = 64
train.max_iter *= 9
