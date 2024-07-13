from ..common.data.coco import dataloader
from ..common.models.mask2former import model
from ..common.train import train

# Initialization and trainer settings
train.init_checkpoint = "detectron2://ImageNetPretrained/torchvision/R-50.pkl"

# Schedule
# 50 ep = 368750 iters * 16 images/iter / 118000 images/ep
dataloader.train.total_batch_size = 16
train.max_iter = 368750
