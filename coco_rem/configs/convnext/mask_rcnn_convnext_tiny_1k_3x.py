from detectron2.config import LazyCall as L

from coco_rem.modeling.convnext import ConvNeXt

from ..common.data.coco import dataloader
from ..common.data.constants import constants
from ..common.models.mask_rcnn_fpn import model
from ..common.train import train

model.backbone.bottom_up = L(ConvNeXt)(
    in_chans=3,
    depths=[3, 3, 9, 3],
    dims=[96, 192, 384, 768],
    drop_path_rate=0.4,
    layer_scale_init_value=1.0,
    out_features=["res2", "res3", "res4", "res5"],
)

train.init_checkpoint = None  # Load externally.
train.max_iter *= 3
