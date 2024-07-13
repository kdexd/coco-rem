from detectron2.config import LazyCall as L
from detectron2.layers import ShapeSpec
from detectron2.modeling.box_regression import Box2BoxTransform
from detectron2.modeling.roi_heads import FastRCNNConvFCHead, FastRCNNOutputLayers

from coco_rem.modeling.convnext import ConvNeXt

from ..common.data.coco import dataloader
from ..common.data.constants import constants
from ..common.models.cascade_rcnn import model
from ..common.train import train

model.backbone.bottom_up = L(ConvNeXt)(
    in_chans=3,
    depths=[3, 3, 27, 3],
    dims=[128, 256, 512, 1024],
    drop_path_rate=0.7,
    layer_scale_init_value=1.0,
    out_features=["res2", "res3", "res4", "res5"],
)

model.roi_heads.update(
    # 4conv1fc box heads with BatchNorm
    box_heads=[
        L(FastRCNNConvFCHead)(
            input_shape=ShapeSpec(channels=256, height=7, width=7),
            conv_dims=[256, 256, 256, 256],
            fc_dims=[1024],
            conv_norm="SyncBN",
        )
        for k in range(3)
    ],
    box_predictors=[
        L(FastRCNNOutputLayers)(
            input_shape=ShapeSpec(channels=1024),
            test_score_thresh=0.05,
            box2box_transform=L(Box2BoxTransform)(weights=(w1, w1, w2, w2)),
            #
            # Cascade R-CNN implementation in Detectron2 has class-agnostic box reg
            # but checkpoints from ConvNext repo (MMDetection) use class-specific.
            cls_agnostic_bbox_reg=False,
            num_classes="${...num_classes}",
        )
        for (w1, w2) in [(10, 5), (20, 10), (30, 15)]
    ],
)

train.init_checkpoint = None  # Load externally.
train.max_iter *= 3
