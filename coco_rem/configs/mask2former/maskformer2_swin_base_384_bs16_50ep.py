from detectron2.config import LazyCall as L
from detectron2.layers import ShapeSpec

from .maskformer2_swin_tiny_bs16_50ep import dataloader, model, train

model.backbone.depths = [2, 2, 18, 2]
model.backbone.num_heads = [4, 8, 16, 32]
model.backbone.window_size = 12
model.backbone.embed_dim = 128
model.backbone.pretrain_img_size = 384

model.sem_seg_head.pixel_decoder.input_shape = {
    "p0": L(ShapeSpec)(channels=128, stride=4),
    "p1": L(ShapeSpec)(channels=256, stride=8),
    "p2": L(ShapeSpec)(channels=512, stride=16),
    "p3": L(ShapeSpec)(channels=1024, stride=32),
}

train.init_checkpoint = (
    "detectron2://ImageNetPretrained/swin/swin_base_patch4_window12_384.pth"
)
