from .cascade_mask_rcnn_mvitv2_b_in21k_100ep import dataloader, model, train

model.backbone.bottom_up.embed_dim = 192
model.backbone.bottom_up.depth = 80
model.backbone.bottom_up.num_heads = 3
model.backbone.bottom_up.last_block_indexes = (3, 11, 71, 79)
model.backbone.bottom_up.drop_path_rate = 0.6
model.backbone.bottom_up.use_act_checkpoint = True


train.init_checkpoint = "detectron2://ImageNetPretrained/mvitv2/MViTv2_H_in21k.pyth"


# 36 epochs
train.max_iter = 67500
