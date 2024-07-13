"""
Merge LVIS instance annotations for COCO categories (a.k.a "COCO-fied LVIS") into
the original COCO instance annotations.

COCO instance annotations are inconsistent, sometimes covering multiple objects
into one mask. LVIS offers a much stronger guarantee that instances are labeled
individually and exhaustively. For any `(image, category)` pair, if COCO-fied LVIS
has instance annotations, then they replace the corresponding COCO annotations.
"""

from __future__ import annotations

import argparse
import copy
import json
from collections import defaultdict

from coco_rem.data.lvis import COCO_CATEGORIES_IN_LVIS

parser = argparse.ArgumentParser(description=__doc__)
_AA = parser.add_argument
_AA("--coco-json", help="Path to COCO annotations JSON file.")
_AA(
    "--lvis-json",
    nargs=2,
    help="Paths to LVIS train and val JSON files.",
    default=["datasets/lvis/lvis_v1_train.json", "datasets/lvis/lvis_v1_val.json"],
)
_AA("--split", choices=["train", "val"], help="Which dataset split to pre-process?")
_AA("--output", required=True, help="Path to save the output annotations JSON.")


def make_cocofied_lvis(lvis_json_paths: list[str], split: str):
    """
    Load LVIS instance annotations and filter them to keep instance annotations
    of the COCO categories for all images belonging to a COCO split (train/val).
    Category IDs in the output JSON are same as COCO IDs.
    """

    lvis_images, lvis_annos = [], []
    for _path in lvis_json_paths:
        lvis_json = json.load(open(_path))
        lvis_images.extend(lvis_json.pop("images"))
        lvis_annos.extend(lvis_json.pop("annotations"))

    # LVIS train/val splits are different than COCO (but in total, they cover the
    # same set of images). So we load both train and val annotations, then retain
    # images and their instances of the desired COCO split.
    keep_ids = set([x["id"] for x in lvis_images if split in x["coco_url"]])
    lvis_images = [x for x in lvis_images if x["id"] in keep_ids]
    lvis_annos = [x for x in lvis_annos if x["image_id"] in keep_ids]

    # Replace the category ID in instance annotation (LVIS -> COCO), and remove
    # LVIS instances that do not represent COCO categories.
    lvis_to_coco_id = {x["lvis_id"]: x["coco_id"] for x in COCO_CATEGORIES_IN_LVIS}
    lvis_annos = [x for x in lvis_annos if x["category_id"] in lvis_to_coco_id]
    for ann in lvis_annos:
        ann["category_id"] = lvis_to_coco_id[ann["category_id"]]

    # Replace category IDs in the "negative categories" list per image, like above.
    for image in lvis_images:
        for key in ["not_exhaustive_category_ids", "neg_category_ids"]:
            image[key] = [x for x in image[key] if x in lvis_to_coco_id]
            image[key] = [lvis_to_coco_id[x] for x in image[key]]

    # Transfer metadata from original LVIS json to COCOfied LVIS json.
    cocofied_lvis = copy.deepcopy(lvis_json)
    cocofied_lvis["images"] = lvis_images
    cocofied_lvis["annotations"] = lvis_annos

    # Update category IDs of LVIS categories.
    cocofied_lvis["categories"] = [
        x for x in cocofied_lvis["categories"] if x["id"] in lvis_to_coco_id
    ]
    for ann in cocofied_lvis["categories"]:
        ann["id"] = lvis_to_coco_id[ann["id"]]

    print(f"COCO-fied LVIS stats for COCO {split} split:")
    print(f"  - Number of images      = {len(lvis_images)}")
    print(f"  - Number of annotations = {len(lvis_annos)}")

    return cocofied_lvis


def main(_A: argparse.Namespace):
    coco_json = json.load(open(_A.coco_json))
    lvis_json = make_cocofied_lvis(_A.lvis_json, _A.split)

    # Make a mapping from `(image_id, category_id) -> list[instances]` for both,
    # COCO and LVIS.
    coco_instances_dict = defaultdict(list)
    for ann in coco_json["annotations"]:
        # Mark the source of every annotation before merging.
        ann["source"] = "coco"
        ann["source_id"] = ann["id"]
        coco_instances_dict[(ann["image_id"], ann["category_id"])].append(ann)

    lvis_instances_dict = defaultdict(list)
    for ann in lvis_json["annotations"]:
        ann["source"] = "lvis"
        ann["source_id"] = ann["id"]
        lvis_instances_dict[(ann["image_id"], ann["category_id"])].append(ann)

    # ------------------------------------------------------------------------
    # For val set, remove all COCO-fied LVIS annotations for `(image, category)`
    # pair if instances are not annotated exhaustively.
    if _A.split == "val":
        _remove = [
            (image_info["id"], category_id)
            for image_info in lvis_json["images"]
            for category_id in image_info["not_exhaustive_category_ids"]
        ]
        lvis_instances_dict = {
            k: v for k, v in lvis_instances_dict.items() if k not in _remove
        }

    # ------------------------------------------------------------------------
    # If `(image, category)` tuple has more LVIS instances than COCO instances
    # then all COCO instances will be replaced by LVIS instances.
    merged_annotations = []
    for (image_id, category_id), anns_in_coco in coco_instances_dict.items():
        anns_in_lvis = lvis_instances_dict.get((image_id, category_id), [])

        if len(anns_in_lvis) > len(anns_in_coco):
            merged_annotations.extend(anns_in_lvis)
        else:
            merged_annotations.extend(anns_in_coco)

    # Some `(image, category)` instances of LVIS are completely absent in COCO.
    # Add all of these while merging.
    for (image_id, category_id), anns_in_lvis in lvis_instances_dict.items():
        if (image_id, category_id) not in coco_instances_dict:
            merged_annotations.extend(anns_in_lvis)

    coco_json["annotations"] = merged_annotations

    # Re-assign annotation IDs after merging.
    image_id_to_anns_coco = defaultdict(list)
    for ann in coco_json["annotations"]:
        image_id_to_anns_coco[ann["image_id"]].append(ann)

    for image_id, anns_in_coco in image_id_to_anns_coco.items():
        for idx, ann in enumerate(anns_in_coco):
            ann["id"] = image_id * 1000 + idx

    # ------------------------------------------------------------------------
    # Calculate number of annotations sourced from COCO/LVIS.
    num_coco_src = len([x for x in merged_annotations if x["source"] == "coco"])
    num_lvis_src = len([x for x in merged_annotations if x["source"] == "lvis"])

    print(f"Final COCO {_A.split} split statistics after merging:")
    print(f"  - Number of images      = {len(coco_json['images'])}")
    print(f"  - Number of annotations = {len(coco_json['annotations'])}")
    print(f"      - Annotations from COCO = {num_coco_src}")
    print(f"      - Annotations from LVIS = {num_lvis_src}")

    json.dump(coco_json, open(_A.output, "w"))
    print(f"Saved the merged annotations JSON to {_A.output}")


if __name__ == "__main__":
    _A = parser.parse_args()

    # Log all command-line arguments.
    print("Running with arguments:")
    for key, value in vars(_A).items():
        print(f"{key:<10}: {value}")

    main(_A)
