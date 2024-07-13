"""
Register COCO-ReM instances for training and evaluation.
"""

import os

from detectron2.data.datasets.coco import register_coco_instances
from detectron2.data.datasets.builtin_meta import _get_builtin_metadata

_PREDEFINED_SPLITS_COCO_REM = {
    "coco_rem_train": ("coco/train2017", "coco_rem/instances_trainrem.json"),
    "coco_rem_val": ("coco/val2017", "coco_rem/instances_valrem.json"),
}


def register_all_coco_rem(root: str = "datasets"):
    for key, (image_root, json_file) in _PREDEFINED_SPLITS_COCO_REM.items():
        # Assume pre-defined datasets live in `./datasets`.
        register_coco_instances(
            key,
            _get_builtin_metadata("coco"),
            os.path.join(root, json_file) if "://" not in json_file else json_file,
            os.path.join(root, image_root),
        )
