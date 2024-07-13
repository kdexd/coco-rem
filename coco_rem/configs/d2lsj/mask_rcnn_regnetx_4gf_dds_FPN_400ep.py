from .mask_rcnn_regnetx_4gf_dds_FPN_100ep import dataloader, model, train

train.max_iter *= 4  # 100ep -> 400ep
