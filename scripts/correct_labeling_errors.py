"""
Add and remove a few instances from a given COCO JSON, and mark a few other
instances as 'crowd' objects as their masks cover multiple instances.
"""

import argparse
import json

import torch
from pycocotools import mask as mask_utils
from segment_anything.utils import amg

import coco_rem.data.manual_rem as inv


parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument(
    "--input",
    default="datasets/coco_rem/instances_valrem_interim.json",
    help="COCO-ReM JSON file to apply all manual corrections.",
)
parser.add_argument(
    "--output", required=True, help="Path to save output annotations JSON."
)


def main(_A: argparse.Namespace):
    coco_json = json.load(open(_A.input))
    print(f"Number of instances in input JSON: {len(coco_json['annotations'])}")

    # ------------------------------------------------------------------------
    # Step 1: Remove some instances.
    remove_info_tuples = [
        (x["image_id"], x["source"], x["source_id"]) for x in inv.INSTANCES_TO_REMOVE
    ]
    coco_json["annotations"] = [
        x
        for x in coco_json["annotations"]
        if (x["image_id"], x["source"], x["source_id"]) not in remove_info_tuples
    ]

    num_instances = len(coco_json["annotations"])
    print(f"Removed few instances, updated JSON has {num_instances} instances.")

    # ------------------------------------------------------------------------
    # Step 2: Set 'iscrowd = 1' for few instances.
    crowd_info_tuples = [
        (x["image_id"], x["source"], x["source_id"]) for x in inv.INSTANCES_TO_CROWD
    ]
    for ann in coco_json["annotations"]:
        if (ann["image_id"], ann["source"], ann["source_id"]) in crowd_info_tuples:
            ann["iscrowd"] = 1

    print(f"Set 'iscrowd = 1' for {len(inv.INSTANCES_TO_CROWD)} instances.")

    # ------------------------------------------------------------------------
    # Step 3: Add some instances.
    for idx, ann in enumerate(inv.INSTANCES_TO_ADD):
        # Convert compressed RLE to mask.
        binary_mask = mask_utils.decode(ann["segmentation"])
        binary_mask = torch.from_numpy(binary_mask)

        # Convert torch tensor to uncompressed RLE.
        ann["segmentation"] = amg.mask_to_rle_pytorch(binary_mask[None, ...])[0]

        # Fill other attributes for the annotation - a unique ID, source, bbox,
        # area, and `iscrowd = 0`.
        bbox_xyxy = amg.batched_mask_to_box(binary_mask[None, ...])[0]

        # Convert bounding box from XYXY to XYWH format.
        x1, y1, x2, y2 = bbox_xyxy.tolist()
        ann["bbox"] = [x1, y1, x2 - x1 + 1, y2 - y1 + 1]

        ann["area"] = amg.area_from_rle(ann["segmentation"])
        ann["id"] = 2024000000 + idx
        ann["source_id"] = ann["id"]
        ann["source"] = "manual"
        ann["iscrowd"] = 0

        coco_json["annotations"].append(ann)

    num_instances = len(coco_json["annotations"])
    print(f"Added few instances, updated JSON has {num_instances} instances.")

    json.dump(coco_json, open(_A.output, "w"))
    print(f"Saved the updated annotations JSON at {_A.output}!")


if __name__ == "__main__":
    args = parser.parse_args()
    main(args)
