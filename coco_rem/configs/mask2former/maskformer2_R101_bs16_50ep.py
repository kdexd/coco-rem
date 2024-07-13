from .maskformer2_R50_bs16_50ep import dataloader, model, train

model.backbone.stages.depth = 101
train.init_checkpoint = "detectron2://ImageNetPretrained/MSRA/R-101.pkl"
