from functools import partial

from detectron2.modeling.backbone.vit import get_vit_lr_decay_rate

from ..common.coco_schedule import lr_multiplier_100ep as lr_multiplier
from ..common.data.coco import dataloader
from ..common.models.mask_rcnn_vitdet import model
from ..common.optim import AdamW as optimizer
from ..common.train import train

# Initialization and trainer settings
train.ddp.fp16_compression = True
train.init_checkpoint = "detectron2://ImageNetPretrained/MAE/mae_pretrain_vit_base.pth?matching_heuristics=True"


# 100 ep = 184375 iters * 64 images/iter / 118000 images/ep
train.max_iter = 184375

# Layer-wise LR decay for ViT
optimizer.params.lr_factor_func = partial(
    get_vit_lr_decay_rate, num_layers=12, lr_decay_rate=0.7
)
optimizer.params.overrides = {"pos_embed": {"weight_decay": 0.0}}
