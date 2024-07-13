from detectron2.config import LazyCall as L
from detectron2.modeling.backbone import RegNet
from detectron2.modeling.backbone.regnet import ResBottleneckBlock, SimpleStem

from .mask_rcnn_R_50_FPN_100ep import dataloader, model, train

# Config source:
model.backbone.bottom_up = L(RegNet)(
    stem_class=SimpleStem,
    stem_width=32,
    block_class=ResBottleneckBlock,
    depth=23,
    w_a=38.65,
    w_0=96,
    w_m=2.43,
    group_width=40,
    norm="SyncBN",
    out_features=["s1", "s2", "s3", "s4"],
)
model.pixel_std = [57.375, 57.120, 58.395]

# RegNets benefit from enabling cudnn benchmark mode
train.cudnn_benchmark = True
