from .mask_rcnn_R_50_FPN_100ep import dataloader, model, train

train.max_iter *= 2  # 100ep -> 200ep
