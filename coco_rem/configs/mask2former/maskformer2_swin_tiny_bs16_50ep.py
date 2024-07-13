from detectron2.config import LazyCall as L
from detectron2.layers import ShapeSpec
from detectron2.modeling import SwinTransformer

from .maskformer2_R50_bs16_50ep import dataloader, model, train

model.backbone = L(SwinTransformer)(
    depths=[2, 2, 6, 2],
    embed_dim=96,
    num_heads=[3, 6, 12, 24],
    drop_path_rate=0.3,
)

model.sem_seg_head.pixel_decoder.input_shape = {
    "p0": L(ShapeSpec)(channels=96, stride=4),
    "p1": L(ShapeSpec)(channels=192, stride=8),
    "p2": L(ShapeSpec)(channels=384, stride=16),
    "p3": L(ShapeSpec)(channels=768, stride=32),
}
model.sem_seg_head.pixel_decoder.transformer_in_features = ["p1", "p2", "p3"]

train.init_checkpoint = (
    "detectron2://ImageNetPretrained/swin/swin_tiny_patch4_window7_224.pth"
)
