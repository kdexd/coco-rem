from .mask_rcnn_R_50_FPN_100ep import dataloader, model, train

model.backbone.bottom_up.stages.depth = 101
