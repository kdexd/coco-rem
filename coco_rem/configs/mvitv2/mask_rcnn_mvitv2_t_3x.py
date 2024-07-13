from functools import partial

import torch.nn as nn
from detectron2.config import LazyCall as L
from detectron2.modeling import MViT

from ..common.data.coco import dataloader
from ..common.data.constants import constants
from ..common.models.mask_rcnn_fpn import model
from ..common.train import train

model.backbone.bottom_up = L(MViT)(
    embed_dim=96,
    depth=10,
    num_heads=1,
    last_block_indexes=(0, 2, 7, 9),
    residual_pooling=True,
    drop_path_rate=0.2,
    norm_layer=partial(nn.LayerNorm, eps=1e-6),
    out_features=("scale2", "scale3", "scale4", "scale5"),
)
model.backbone.in_features = "${.bottom_up.out_features}"

# Initialization and trainer settings
train.amp.enabled = True
train.ddp.fp16_compression = True
train.init_checkpoint = "detectron2://ImageNetPretrained/mvitv2/MViTv2_T_in1k.pyth"

# 36 epochs
train.max_iter = 67500
