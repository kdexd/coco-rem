"""
Visualize instances from a COCO annotations JSON (COCO-2017 or COCO-ReM).
"""

import argparse
import logging
import os

import numpy as np
from detectron2.data import DatasetCatalog, MetadataCatalog
from detectron2.data import detection_utils as utils
from detectron2.data.datasets import load_coco_json
from tqdm import tqdm

from coco_rem.mask_visualizer import MaskVisualizer

logger = logging.getLogger(__name__)

# fmt: off
parser = argparse.ArgumentParser(description=__doc__)
_AA = parser.add_argument
_AA(
    "--input-json", default="datasets/coco/annotations/instances_val2017.json",
    help="Path to JSON file containing COCO annotations."
)
_AA(
    "--image-dir", default="datasets/coco/val2017",
    help="Path to directory containing COCO images.",
)
_AA("--draw-labels", action="store_true", help="Whether to draw labels on masks.")
_AA("--class-name", help="If provided, visualize masks of this class only.")

_AA("--output", default="./viz", help="Path to output (saving) dir.")
_AA("--filename-suffix", help="Add a suffix to saved image file name.")
# fmt: on


def add_id_to_labels(dic, labels):
    labels = [f"{lbl} ({x['id']})" for lbl, x in zip(labels, dic["annotations"])]
    return labels


if __name__ == "__main__":
    _A = parser.parse_args()
    print("Arguments: " + str(_A))

    # Register the input COCO JSON file as a Detectron2 dataset to load nicely
    # formatted dataset dicts for visualization.
    # Extra annotation keys: all possible keys added in generated JSON files.
    name = "coco_or_lvis_v1_cocofied_to_visualize"
    extra_keys = ["source", "source_id", "id"]

    DatasetCatalog.register(
        name, lambda: load_coco_json(_A.input_json, _A.image_dir, name, extra_keys)
    )
    # ------------------------------------------------------------------------
    # Fix seed for reproducible colors.
    np.random.seed(0)

    dataset_dicts = DatasetCatalog.get(name)
    class_names = MetadataCatalog.get("coco_2017_val").thing_classes
    os.makedirs(_A.output, exist_ok=True)

    for ddict in tqdm(dataset_dicts):
        if _A.class_name is not None:
            ddict["annotations"] = [
                ann
                for ann in ddict["annotations"]
                if class_names[ann["category_id"]] == _A.class_name
            ]

        if len(ddict["annotations"]) > 0:
            img = utils.read_image(ddict["file_name"], "RGB")
            visualizer = MaskVisualizer(img, class_names)
            vis_image = visualizer.draw_dataset_dict(
                ddict, _A.draw_labels, label_suffix_formatter=add_id_to_labels
            )

            # Save the visualized image.
            filepath = os.path.join(_A.output, os.path.basename(ddict["file_name"]))
            if _A.class_name is not None:
                filepath = filepath.replace(".jpg", f"_{_A.class_name}.jpg")

            if _A.filename_suffix is not None:
                filepath = filepath.replace(".jpg", f"_{_A.filename_suffix}.jpg")

            vis_image.save(filepath)
