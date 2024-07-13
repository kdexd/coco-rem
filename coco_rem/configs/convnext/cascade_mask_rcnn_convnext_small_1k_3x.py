from .cascade_mask_rcnn_convnext_base_1k_3x import dataloader, model, train

model.backbone.bottom_up.dims = [96, 192, 384, 768]
model.backbone.bottom_up.drop_path_rate = 0.6
