from .mask_rcnn_R_101_FPN_100ep import dataloader, model, train

train.max_iter *= 4  # 100ep -> 400ep
