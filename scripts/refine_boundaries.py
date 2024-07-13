"""
Refine mask boundaries of input COCO JSON to obtain COCO-ReM. Refinement is done
using the `SamRefiner` module in this package.
"""

from __future__ import annotations

import argparse
import json
import os
from collections import defaultdict

import torch
from detectron2 import engine
from detectron2.data.detection_utils import read_image
from detectron2.data.transforms import ResizeShortestEdge
from detectron2.structures import polygons_to_bitmask
from detectron2.utils import comm
from segment_anything.utils import amg
from tqdm import tqdm

from coco_rem.modeling.sam_refiner import SamRefiner

# Add documentation of `SamRefiner` to this script documentation, so argparse can
# display it with `--help`.
__doc__ += f"\n\n{SamRefiner.__doc__}\n{SamRefiner.__init__.__doc__}"

# fmt: off
parser = argparse.ArgumentParser(
    description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
)
_AA = parser.add_argument
_AA("--input-json", required=True, help="Path to COCO annotations JSON.")
_AA("--image-dir", default="datasets/coco/val2017", help="COCO image directory.")
_AA("--num-gpus", type=int, default=0, help="Number of GPUs for parallelization.")
_AA("--output", required=True, help="Path to save output annotations JSON.")

group = parser.add_argument_group("Input arguments to `SamRefiner`.")
group.add_argument("--arch", default="vit_h", choices=["vit_b", "vit_l", "vit_h"])
group.add_argument("--checkpoint", default="checkpoints/sam_vit_h_4b8939.pth")
group.add_argument("--num-extra-points", type=int, default=2)
group.add_argument("--num-trials", type=int, default=10)
group.add_argument(
    "--box-only-names", nargs="+",
    default=["bed", "bicycle", "bowl", "dining table", "motorcycle", "scissors"],
    help="COCO category names for which we only use box prompts.",
)
# fmt: on


def main(_A: argparse.Namespace):
    device = torch.device("cpu")
    if torch.cuda.is_available():
        device = torch.cuda.current_device()

    # ------------------------------------------------------------------------
    coco_json = json.load(open(_A.input_json))

    # Make a mapping between image ID and all instance annotations.
    image_id_annotations = defaultdict(list)
    for ann in coco_json["annotations"]:
        image_id_annotations[ann["image_id"]].append(ann)

    image_id_annotations = list(image_id_annotations.items())

    # Shard the dataset so each GPU only refines masks for a subset of images.
    WORLD_SIZE = comm.get_world_size()
    RANK = comm.get_rank()

    image_id_annotations = image_id_annotations[RANK::WORLD_SIZE]
    print(f"GPU {RANK}/{WORLD_SIZE} will process {len(image_id_annotations)} images.")

    # Get a list of category IDs for which only box prompts will be used.
    cat_id_map = {x["name"]: x["id"] for x in coco_json["categories"]}
    box_only_ids = [cat_id_map[x] for x in _A.box_only_names]

    # ------------------------------------------------------------------------
    # Instantiate model and input tranform (resize longest side to 1024 pixels).
    refiner = SamRefiner(
        _A.arch, _A.checkpoint, _A.num_extra_points, _A.num_trials, box_only_ids
    )
    refiner = refiner.eval().to(device)

    preprocess = ResizeShortestEdge(refiner.img_size, max_size=refiner.img_size)

    # ------------------------------------------------------------------------
    for image_id, annotations in tqdm(image_id_annotations, "Refining masks"):
        image_path = os.path.join(_A.image_dir, f"{image_id:0>12d}.jpg")
        image = read_image(image_path, "RGB")
        original_hw = image.shape[:2]

        # Pre-process image and masks.
        transform = preprocess.get_transform(image)
        image = transform.apply_image(image)

        # Get image height/width before and after applying resize transform.
        resized_hw = image.shape[:2]

        # Convert image to NCHW format tensor, RGB values in 0-255).
        image = torch.as_tensor(image, device=device)
        image = image.permute(2, 0, 1).contiguous()

        # Make batches of source masks (NHW bool tensor).
        source_masks = [ann["segmentation"] for ann in annotations]
        for idx, segm in enumerate(source_masks):
            if isinstance(segm, list):
                # Polygons.
                polygons = [torch.as_tensor(p).view(-1, 2) for p in segm]
                polygons = [p.view(-1) for p in transform.apply_polygons(polygons)]
                segm = polygons_to_bitmask(polygons, *resized_hw)
            elif isinstance(segm, dict):
                # RLE.
                segm = amg.rle_to_mask(segm).astype("uint8")
                segm = transform.apply_segmentation(segm)

            source_masks[idx] = torch.as_tensor(segm).bool()

        source_masks = torch.stack(source_masks).to(device)
        # --------------------------------------------------------------------

        category_ids = [ann["category_id"] for ann in annotations]
        refined_masks = refiner(image, source_masks, category_ids, original_hw)

        # Get tight boxes enclosing refined masks, then convert masks to RLE.
        refined_boxes_xyxy = amg.batched_mask_to_box(refined_masks)
        refined_masks = amg.mask_to_rle_pytorch(refined_masks)

        # Replace the source masks with refined masks in COCO annotations.
        # NOTE: Keep "crowd" annotations unchanged as they don't participate in
        # the calculation of COCO AP.
        for idx, ann in enumerate(annotations):
            if ann.get("iscrowd", 0) != 1:
                ann["segmentation"] = refined_masks[idx]
                ann["area"] = amg.area_from_rle(refined_masks[idx])

                # Recompute box enclosing the refined mask.
                x1, y1, x2, y2 = refined_boxes_xyxy[idx].tolist()
                ann["bbox"] = [x1, y1, x2 - x1 + 1, y2 - y1 + 1]

    # ------------------------------------------------------------------------

    # Combine the refined masks from all GPU processes to main process.
    all_refined_annotations = []
    for _, annotations in image_id_annotations:
        all_refined_annotations.extend(annotations)

    all_refined_annotations = comm.gather(all_refined_annotations, dst=0)

    # In main process, replace annotations in COCO JSON and save to output.
    if comm.is_main_process():
        coco_json["annotations"] = []
        for ann_list in all_refined_annotations:
            coco_json["annotations"].extend(ann_list)

        os.makedirs(os.path.dirname(_A.output), exist_ok=True)
        json.dump(coco_json, open(_A.output, "w"))
        print(f"Saved annotations JSON with refined masks to {_A.output}")

    comm.synchronize()
    print(f"GPU {RANK}/{WORLD_SIZE}: Refinement complete!")


if __name__ == "__main__":
    _A = parser.parse_args()

    print("Running with arguments:")
    for key, value in vars(_A).items():
        print(f"{key:<30}: {value}")

    engine.launch(main, num_gpus_per_machine=_A.num_gpus, dist_url="auto", args=(_A,))
