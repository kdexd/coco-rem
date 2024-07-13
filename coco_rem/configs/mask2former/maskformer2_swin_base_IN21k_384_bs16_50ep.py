from .maskformer2_swin_base_384_bs16_50ep import dataloader, model, train

train.init_checkpoint = (
    "detectron2://ImageNetPretrained/swin/swin_base_patch4_window12_384_22k.pth"
)
