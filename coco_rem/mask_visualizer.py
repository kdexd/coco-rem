from __future__ import annotations

import itertools
from typing import Callable, Optional

import cv2
import matplotlib.colors as mplc
import numpy as np
import pycocotools.mask as mask_util
import torch
from detectron2.utils.visualizer import VisImage
from torch.nn.functional import max_pool2d

# Nice colors, taken from `colorblind` palette of the `seaborn` library with
# very minor modifications for aesthetics.
NICE_COLORS = [
    (0.0039, 0.4509, 0.6980),  # blue
    (0.8905, 0.5607, 0.0196),  # orange
    (0.0078, 0.6196, 0.4509),  # green
    (0.9400, 0.2200, 0.1000),  # red
    (0.6500, 0.3500, 0.9000),  # purple
    (0.6980, 1.0000, 0.3500),  # lime green
    (0.5019, 0.8705, 0.9176),  # cyan
    (0.7921, 0.5686, 0.3803),  # brown
    (0.9843, 0.6862, 0.8941),  # pink
    (0.9254, 0.8823, 0.2001),  # gold
]


def binarize_mask(mask_or_polygons, height: int, width: int):
    """
    Convert input masks of any format to a binary mask (np.uint8 array with 1
    as foreground and 0 as background).
    """
    m = mask_or_polygons
    if isinstance(m, dict):
        # RLEs
        assert "counts" in m and "size" in m
        if isinstance(m["counts"], list):  # uncompressed RLEs
            h, w = m["size"]
            assert h == height and w == width
            m = mask_util.frPyObjects(m, h, w)
        mask = mask_util.decode(m)[:, :]

    if isinstance(m, list):  # list[ndarray]
        m = mask_util.frPyObjects(m, height, width)
        m = mask_util.merge(m)
        mask = mask_util.decode(m)[:, :]

    if isinstance(m, np.ndarray):  # assumed to be a binary mask
        assert m.shape[1] != 2, m.shape
        assert m.shape == (
            height,
            width,
        ), f"mask shape: {m.shape}, target dims: {height}, {width}"
        mask = m.astype("uint8")

    return mask


def _create_text_labels(classes, class_names, is_crowd=None):
    labels = None
    if classes is not None:
        if class_names is not None and len(class_names) > 0:
            labels = [class_names[i] for i in classes]
        else:
            labels = [str(i) for i in classes]

    if labels is not None and is_crowd is not None:
        labels = [l + ("|crowd" if crowd else "") for l, crowd in zip(labels, is_crowd)]
    return labels


class MaskVisualizer:
    """Visualizer for labeled masks of COCO-format instance annotations."""

    def __init__(self, img_rgb: np.ndarray, class_names: list[str] | None = None):
        """
        Args:
            img_rgb: a numpy array of shape (H, W, C), where H and W correspond to
                the height and width of the image respectively. C is the number of
                color channels. The image is required to be in RGB format since that
                is a requirement of the Matplotlib library. The image is also expected
                to be in the range [0, 255].
            class_names: List of names to associate with object class IDs of masks.
        """
        self.img = np.asarray(img_rgb).clip(0, 255).astype(np.uint8)
        self.class_names = class_names
        self.output = VisImage(self.img)
        self.cpu_device = torch.device("cpu")

        # too small texts are useless, therefore clamp to 12
        self._default_font_size = max(
            np.sqrt(self.output.height * self.output.width) // 90, 12
        )

    def draw_dataset_dict(
        self,
        dic,
        draw_labels: bool = True,
        label_suffix_formatter: Optional[Callable] = None,
    ):
        """
        Draw annotations/segmentations in Detectron2 Dataset format.

        Args:
            dic (dict): annotation/segmentation data of one image, in Detectron2 Dataset format.

        Returns:
            output (VisImage): image object with visualizations.
        """
        annos = dic.get("annotations", None)
        if annos:
            if "segmentation" in annos[0]:
                masks = [x["segmentation"] for x in annos]
            else:
                masks = None

            if draw_labels:
                category_ids = [x["category_id"] for x in annos]
                labels = _create_text_labels(
                    category_ids,
                    class_names=self.class_names,
                    is_crowd=[x.get("iscrowd", 0) for x in annos],
                )

                if label_suffix_formatter is not None:
                    labels = label_suffix_formatter(dic, labels)
            else:
                labels = None

            self.overlay_instances(labels=labels, masks=masks)

        return self.output

    def overlay_instances(self, labels=None, masks=None, alpha=0.7):
        """
        Args:
            labels (list[str]): the text to be displayed for each instance.
            masks (masks-like object): Supported types are:

                * :class:`detectron2.structures.PolygonMasks`,
                  :class:`detectron2.structures.BitMasks`.
                * list[list[ndarray]]: contains the segmentation masks for all objects in one image.
                  The first level of the list corresponds to individual instances. The second
                  level to all the polygon that compose the instance, and the third level
                  to the polygon coordinates. The third level should have the format of
                  [x0, y0, x1, y1, ..., xn, yn] (n >= 3).
                * list[ndarray]: each ndarray is a binary mask of shape (H, W).
                * list[dict]: each dict is a COCO-style RLE.

        Returns:
            output (VisImage): image object with visualizations.
        """
        num_instances = 0
        if masks is not None:
            masks = [
                binarize_mask(x, self.output.height, self.output.width) for x in masks
            ]
            if num_instances:
                assert len(masks) == num_instances
            else:
                num_instances = len(masks)

        if labels is not None:
            assert len(labels) == num_instances

        assigned_colors = list(
            itertools.islice(itertools.cycle(NICE_COLORS), num_instances)
        )

        if num_instances == 0:
            return self.output

        # Display in largest to smallest order to reduce occlusion.
        areas = np.asarray([x.sum() for x in masks])

        sorted_idxs = np.argsort(-areas).tolist()
        # Re-order overlapped instances in descending order.
        labels = [labels[k] for k in sorted_idxs] if labels is not None else None
        masks = [masks[idx] for idx in sorted_idxs] if masks is not None else None
        assigned_colors = [assigned_colors[idx] for idx in sorted_idxs]

        for i in range(num_instances):
            color = assigned_colors[i]
            text = labels[i] if labels is not None else ""
            self.draw_binary_mask(masks[i], color, text=text, alpha=alpha)

        return self.output

    def draw_text(self, text: str, x: float, y: float) -> VisImage:
        # fmt: off
        self.output.ax.text(
            x, y, text, size=self._default_font_size, family="sans-serif",
            bbox={"facecolor": "white", "alpha": 1.0, "pad": 1.0, "edgecolor": "none"},
            verticalalignment="top", horizontalalignment="center",
            color="black", zorder=10,
        )
        # fmt: on
        return self.output

    def draw_binary_mask(self, binary_mask, color, text=None, alpha=0.7):
        """
        Args:
            binary_mask: numpy array of shape (H, W), where H is the image height
                and W is the image width. Each value in the array is either a 0
                or 1 value of uint8 type.
            color: color of the mask. Refer to `matplotlib.colors` for a full list
                of formats that are accepted. If None, will pick a random color.
            text: A string to draw on the object.
            alpha: blending co-efficient. Smaller values => more transparent masks.

        Returns:
            output (VisImage): image object with mask drawn.
        """
        color = mplc.to_rgb(color)

        mask = binary_mask.astype("uint8")  # opencv needs uint8
        shape2d = (binary_mask.shape[0], binary_mask.shape[1])

        # TODO: Use Path/PathPatch to draw vector graphics:
        # https://stackoverflow.com/questions/8919719/how-to-plot-a-complex-polygon
        rgba = np.zeros(shape2d + (4,), dtype="float32")
        rgba[:, :, :3] = color
        rgba[:, :, 3] = (mask == 1).astype("float32") * alpha
        self.output.ax.imshow(
            rgba, extent=(0, self.output.width, self.output.height, 0)
        )

        # Find mask boundary using dilation, then visualize as a black border.
        mask_tensor = torch.from_numpy(mask).float().unsqueeze(0)
        dilated = max_pool2d(mask_tensor, kernel_size=3, stride=1, padding=1)
        boundary = (dilated - mask_tensor)[0].numpy()
        boundary_rgba = np.zeros(shape2d + (4,), dtype="float32")
        boundary_rgba[:, :, 3] = boundary
        self.output.ax.imshow(
            boundary_rgba, extent=(0, self.output.width, self.output.height, 0)
        )

        if text is not None:
            # TODO sometimes drawn on wrong objects. the heuristics here can improve.
            _num_cc, cc_labels, stats, _ = cv2.connectedComponentsWithStats(
                binary_mask, 8
            )
            if stats[1:, -1].size == 0:
                return
            largest_component_id = np.argmax(stats[1:, -1]) + 1

            # draw text on the largest component, as well as other large components.
            for cid in range(1, _num_cc):
                if cid == largest_component_id or stats[cid, -1] > 100000:
                    center = np.median((cc_labels == cid).nonzero(), axis=1)[::-1]
                    self.draw_text(text, *center)

        return self.output

    def get_output(self):
        return self.output
