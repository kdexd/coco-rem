import detectron2.data.transforms as T
from detectron2.config import LazyCall as L
from detectron2.data import (
    DatasetMapper,
    build_detection_test_loader,
    build_detection_train_loader,
    get_detection_dataset_dicts,
)
from omegaconf import OmegaConf

from coco_rem.coco_evaluator import COCOReMEvaluator

dataloader = OmegaConf.create()

# Mapper with large-scale jittering (LSJ) augmentation.
image_size = 1024

dataloader.train = L(build_detection_train_loader)(
    dataset=L(get_detection_dataset_dicts)(names="coco_2017_train"),
    mapper=L(DatasetMapper)(
        is_train=True,
        augmentations=[
            L(T.RandomFlip)(horizontal=True),  # flip first
            L(T.ResizeScale)(
                min_scale=0.1,
                max_scale=2.0,
                target_height=image_size,
                target_width=image_size,
            ),
            L(T.FixedSizeCrop)(crop_size=(image_size, image_size), pad=False),
        ],
        image_format="RGB",
        use_instance_mask=True,
        instance_mask_format="bitmask",
        recompute_boxes=True,
    ),
    total_batch_size=64,
    num_workers=4,
)

# Resize shortest edge to 1024 pixels.
dataloader.test = L(build_detection_test_loader)(
    dataset=L(get_detection_dataset_dicts)(names="coco_2017_val", filter_empty=False),
    mapper=L(DatasetMapper)(
        is_train=False,
        augmentations=[
            L(T.ResizeShortestEdge)(short_edge_length=image_size, max_size=image_size),
        ],
        image_format="${...train.mapper.image_format}",
    ),
    num_workers=4,
)

# Update: Custom COCO evaluator that returns exactly same results as default
# evaluator, with additionally returning AP90, AP95, and Boundary AP.
dataloader.evaluator = L(COCOReMEvaluator)(
    dataset_name="${..test.dataset.names}",
    output_dir="${...train.output_dir}",
)
