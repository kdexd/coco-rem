from detectron2.config import LazyCall as L
from detectron2.layers import ShapeSpec
from detectron2.modeling.backbone import BasicStem, ResNet
from mask2former.maskformer_model import MaskFormer
from mask2former.modeling.meta_arch.mask_former_head import MaskFormerHead
from mask2former.modeling.pixel_decoder.msdeformattn import MSDeformAttnPixelDecoder
from mask2former.modeling.transformer_decoder import MultiScaleMaskedTransformerDecoder

from ..data.constants import constants

model = L(MaskFormer)(
    backbone=L(ResNet)(
        stem=L(BasicStem)(in_channels=3, out_channels=64, norm="FrozenBN"),
        stages=L(ResNet.make_default_stages)(
            depth=50,
            stride_in_1x1=False,
            norm="FrozenBN",
        ),
        out_features=["res2", "res3", "res4", "res5"],
    ),
    sem_seg_head=L(MaskFormerHead)(
        input_shape={
            "res2": L(ShapeSpec)(channels=256, stride=4),
            "res3": L(ShapeSpec)(channels=512, stride=8),
            "res4": L(ShapeSpec)(channels=1024, stride=16),
            "res5": L(ShapeSpec)(channels=2048, stride=32),
        },
        num_classes=80,
        pixel_decoder=L(MSDeformAttnPixelDecoder)(
            input_shape="${..input_shape}",
            transformer_dropout=0.0,
            transformer_nheads=8,
            transformer_dim_feedforward=1024,
            transformer_enc_layers=6,
            conv_dim=256,
            mask_dim=256,
            norm="GN",
            transformer_in_features=["res3", "res4", "res5"],
            common_stride=4,
        ),
        loss_weight=1.0,
        ignore_value=255,
        transformer_predictor=L(MultiScaleMaskedTransformerDecoder)(
            in_channels="${..pixel_decoder.conv_dim}",
            mask_classification=True,
            num_classes="${..num_classes}",
            hidden_dim="${..pixel_decoder.conv_dim}",
            num_queries="${...num_queries}",
            nheads=8,
            dim_feedforward=2048,
            dec_layers=9,
            pre_norm=False,
            mask_dim="${..pixel_decoder.mask_dim}",
            enforce_input_project=False,
        ),
        transformer_in_feature="multi_scale_pixel_decoder",
    ),
    criterion=None,
    num_queries=100,
    metadata=None,
    size_divisibility=32,
    sem_seg_postprocess_before_inference=True,
    object_mask_threshold=0.8,
    overlap_threshold=0.8,
    instance_on=True,
    semantic_on=False,
    panoptic_on=False,
    pixel_mean=constants.imagenet_rgb256_mean,
    pixel_std=constants.imagenet_rgb256_std,
    test_topk_per_image=100,
)
