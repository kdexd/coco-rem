# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.

# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.
from __future__ import annotations

import einops as E
import torch
from segment_anything import sam_model_registry
from segment_anything.utils import amg
from torch import nn


class SamRefiner(nn.Module):
    """
    SamRefiner: An extension of SAM that refines (low-quality) input masks via
    iteratively prompting boxes and points.
    """

    def __init__(
        self,
        arch: str,
        checkpoint: str,
        num_extra_points: int = 2,
        num_trials: int = 10,
        box_only_ids: list[int] = [],
        min_mask_region_area: int = 100,
    ):
        """
        Args:
            arch: SAM image encoder architecture (vit_b, vit_l, vit_h).
            checkpoint: Path to .pth file containing pre-trained SAM weights.
            num_extra_points: Number of extra points to iteratively prompt SAM
                with, after the initial box prompt. Points are sampled from the
                error region (bitwise XOR) between SAM prediction and ground-truth.
            num_trials: Number of refinement trials per instance mask, to improve
                the overall mask quality by ensembling.
            box_only_ids: Category IDs for which only box prompts will used.
            min_mask_region_area: If >0, postprocessing will be applied to remove
                islands and holes in masks with area smaller than this value.
                However, masks smaller than `10 * min_mask_region_area` will not
                remain unchanged to avoid removing useful details in tiny masks.
        """
        super().__init__()

        # Initialize SAM, freeze parameters, and transfer them here.
        _sam = sam_model_registry[arch](checkpoint)
        for param in _sam.parameters():
            param.requires_grad = False

        self.image_encoder = _sam.image_encoder
        self.prompt_encoder = _sam.prompt_encoder
        self.mask_decoder = _sam.mask_decoder
        self.img_size = _sam.image_encoder.img_size  # 1024 pixels

        self.register_buffer("pixel_mean", _sam.pixel_mean)
        self.register_buffer("pixel_std", _sam.pixel_std)

        self.num_extra_points = num_extra_points
        self.num_trials = num_trials
        self.box_only_ids = box_only_ids
        self.min_mask_region_area = min_mask_region_area

    @torch.no_grad()
    def forward(
        self,
        image: torch.Tensor,
        masks: torch.Tensor,
        category_ids: list[int],
        original_size: tuple[int, int],
    ) -> torch.Tensor:
        """
        Regenerate an input mask by iteratively prompting points to SAM, same as
        the training procedure of SAM. This is done for multiple trials and masks
        are combining by averaging and thresholding in order to reduce variance.
        """

        # Normalize pixel values and pad to a square input.
        input_size = image.shape[-2:]
        image = (image[None, ...] - self.pixel_mean) / self.pixel_std
        padh = self.img_size - image.shape[-2]
        padw = self.img_size - image.shape[-1]
        image = nn.functional.pad(image, (0, padw, 0, padh))

        image_embeddings = self.image_encoder(image)
        all_masks = masks  # Rename for convenience.

        all_refined_masks = []
        for src_mask, category_id in zip(all_masks, category_ids):
            xp = 0 if category_id in self.box_only_ids else self.num_extra_points

            # Repeat a single mask `num_trials` times to perform refinement trials
            # within the same batch.
            src_mask = E.repeat(src_mask, "h w -> n h w", n=self.num_trials)

            box_prompt = self._get_box_prompt(src_mask)

            # Iteratively prompt SAM with points sampled from error regions of
            # predicted masks. This is same as SAM's training procedure. The first
            # iteration will only use a box prompt.
            point_prompts, mask_prompt = None, None

            for _ in range(xp + 1):
                # Pass all prompts: points, initial box, logits from prev step.
                sparse_embeddings, dense_embeddings = self.prompt_encoder(
                    point_prompts, box_prompt, mask_prompt
                )

                low_res_masks, _ = self.mask_decoder(
                    image_embeddings=image_embeddings,
                    image_pe=self.prompt_encoder.get_dense_pe(),
                    sparse_prompt_embeddings=sparse_embeddings,
                    dense_prompt_embeddings=dense_embeddings,
                    multimask_output=False,
                )
                refined_masks = nn.functional.interpolate(
                    low_res_masks,
                    (self.img_size, self.img_size),
                    mode="bilinear",
                    align_corners=False,
                )
                refined_masks = refined_masks[..., : input_size[0], : input_size[1]]

                # Use source mask if SAM returned empty mask (happens for tiny boxes).
                if (refined_masks > 0).sum() == 0:
                    refined_masks = src_mask[:, None, ...].float()

                # Update point prompts and mask prompt for next iteration.
                point_prompts = sample_point_from_error_region(
                    src_mask, refined_masks[:, 0], point_prompts
                )
                mask_prompt = low_res_masks

            # Resize the refine masks to original size, then ensemble the trials
            # by thresholding at zero, then taking a majority vote.
            refined_masks = nn.functional.interpolate(
                refined_masks, original_size, mode="bilinear", align_corners=False
            )
            refined_masks = (refined_masks > 0).float()
            refined_mask = E.reduce(refined_masks, "n 1 h w -> h w", "mean")
            refined_mask = refined_mask > 0.5

            # Remove spurious islands/holes for large enough masks.
            _area = self.min_mask_region_area
            if _area > 0 and refined_mask.sum() > 10 * _area:
                _mask = refined_mask.cpu().numpy()

                _mask, _ = amg.remove_small_regions(_mask, _area, mode="holes")
                _mask, _ = amg.remove_small_regions(_mask, _area, mode="islands")
                refined_mask = torch.from_numpy(_mask).to(refined_mask.device)

            all_refined_masks.append(refined_mask)

        all_refined_masks = torch.stack(all_refined_masks)
        return all_refined_masks

    def _get_box_prompt(self, mask: torch.Tensor):
        """
        Make a box prompt to SAM, which is a bounding box of mask that is expanded
        using random noise, same as SAM's training procedure.

        Noise values drawn from Gaussian distributions having zero mean and
        standard deviation equal to 10% of box edge size, up to maximum 10 pixels.
        """
        box_prompt = amg.batched_mask_to_box(mask.bool()).float()

        box_w = box_prompt[:, 2] - box_prompt[:, 0]
        box_h = box_prompt[:, 3] - box_prompt[:, 1]
        noise_std = torch.stack([box_w, box_h, box_w, box_h], dim=1)
        noise_std = torch.clamp(noise_std * 0.1, max=10.0)
        noise_mean = torch.zeros_like(box_prompt)

        random_noise = torch.normal(noise_mean, noise_std)

        box_prompt[:, :2] = box_prompt[:, :2] - random_noise[:, :2].abs()
        box_prompt[:, 2:] = box_prompt[:, 2:] + random_noise[:, 2:].abs()
        box_prompt = box_prompt.clamp(min=0.0, max=self.img_size - 1)
        return box_prompt


def sample_point_from_error_region(
    reference_masks: torch.Tensor,
    predicted_masks: torch.Tensor | None = None,
    previous_prompts: tuple[torch.Tensor, torch.Tensor] | None = None,
) -> tuple[torch.Tensor, torch.Tensor]:
    """
    Sample random points from the error regions between some reference masks
    (e.g. ground-truth) and predicted masks by SAM. Newly sampled points are
    labeled foreground (1) or background (0) depending on the pixel value in
    reference mask. This function simulates interactive segmentation setup for
    training SAM, as described in Segment Anything paper.

    Args:
        reference_masks: Batch of masks as a tensor of shape `(B, H, W)` containing
            pixel values in `{1, 0}` or `{True, False}` denoting foreground region.
        predicted_masks: Batch of masks predicted by SAM having same shape as the
            reference masks. This tensor may have real-valued logits, which will
            be internally binarized by thresholding at 0.
        previous_prompts: Optional tuple of `(point_coords, point_labels)` giving
            point prompts to SAM used in previous interactive iterations.

    Return:
        next_prompts: Tuple of `(point_coords, point_labels)` with newly sampled
            point co-ordinates and labels appended to `previous_prompts`.
    """
    # If predicted masks are not provided, assume that SAM predicted an empty mask.
    # This lets us sample a random point from anywhere inside the reference masks.
    if predicted_masks is None:
        predicted_masks = torch.zeros_like(reference_masks)

    points, point_labels = [], []
    for ref_mask, pr_mask in zip(reference_masks, predicted_masks):
        # Sample from the error region between given masks.
        error_region = torch.logical_xor(ref_mask > 0, pr_mask > 0)
        yx_choices = error_region.nonzero()

        # If there is no error region, sample from anywhere in GT mask.
        if len(yx_choices) == 0:
            yx_choices = ref_mask.nonzero()

        if len(yx_choices) == 0:
            yx_choices = torch.zeros((1, 2), device=ref_mask.device).long()

        idx = torch.randint(len(yx_choices), size=(1,)).item()
        point_xy = yx_choices[idx, [1, 0]]
        point_label = ref_mask[point_xy[1], point_xy[0]]

        points.append(point_xy)
        point_labels.append(point_label)

    points = E.rearrange(torch.stack(points), "b xy -> b 1 xy")
    point_labels = E.rearrange(torch.stack(point_labels).long(), "b -> b 1")

    # Append currently sampled points to previous prompts.
    if previous_prompts is not None:
        previous_points, previous_labels = previous_prompts
        points = torch.cat([previous_points, points], dim=1)
        point_labels = torch.cat([previous_labels, point_labels], dim=1)

    return (points, point_labels)
