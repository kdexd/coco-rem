from ..common.data.coco import dataloader
from ..common.data.constants import constants
from ..common.models.cascade_rcnn import model
from ..common.train import train

dataloader.train.mapper.image_format = "BGR"
model.pixel_mean = constants.imagenet_bgr256_mean
model.pixel_std = constants.imagenet_bgr256_std
model.input_format = "BGR"

train.init_checkpoint = "detectron2://ImageNetPretrained/MSRA/R-50.pkl"
train.max_iter *= 3
