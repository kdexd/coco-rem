from detectron2.config import LazyCall as L
from detectron2.layers import ShapeSpec

from .maskformer2_swin_base_384_bs16_50ep import dataloader, model, train

model.num_queries = 200
model.backbone.num_heads = [6, 12, 24, 48]
model.backbone.embed_dim = 192

model.sem_seg_head.pixel_decoder.input_shape = {
    "p0": L(ShapeSpec)(channels=192, stride=4),
    "p1": L(ShapeSpec)(channels=384, stride=8),
    "p2": L(ShapeSpec)(channels=768, stride=16),
    "p3": L(ShapeSpec)(channels=1536, stride=32),
}

train.max_iter *= 2
train.init_checkpoint = (
    "detectron2://ImageNetPretrained/swin/swin_base_patch4_window12_384_22k.pth"
)
