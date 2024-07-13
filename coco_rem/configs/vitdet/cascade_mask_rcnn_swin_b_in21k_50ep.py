from detectron2.config import LazyCall as L
from detectron2.modeling import SwinTransformer

from ..common.data.coco import dataloader
from ..common.train import train
from .cascade_mask_rcnn_mvitv2_b_in21k_100ep import model

model.backbone.bottom_up = L(SwinTransformer)(
    depths=[2, 2, 18, 2],
    drop_path_rate=0.4,
    embed_dim=128,
    num_heads=[4, 8, 16, 32],
)
model.backbone.in_features = ("p0", "p1", "p2", "p3")
model.backbone.square_pad = 1024

train.init_checkpoint = (
    "detectron2://ImageNetPretrained/swin/swin_base_patch4_window7_224_22k.pth"
)
# 50 ep = (184375 / 2) iters * 64 images/iter / 118000 images/ep
train.max_iter = 184375 // 2
