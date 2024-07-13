from .cascade_mask_rcnn_mvitv2_b_3x import dataloader, model, train

train.init_checkpoint = "detectron2://ImageNetPretrained/mvitv2/MViTv2_B_in21k.pyth"
