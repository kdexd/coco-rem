from .maskformer2_swin_tiny_bs16_50ep import dataloader, model, train

model.backbone.depths = [2, 2, 18, 2]

train.init_checkpoint = (
    "detectron2://ImageNetPretrained/swin/swin_small_patch4_window7_224.pth"
)
