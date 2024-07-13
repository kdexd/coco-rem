from __future__ import annotations

from functools import partial

import torch
from detectron2.layers.batch_norm import LayerNorm as LayerNorm2d
from detectron2.modeling.backbone import Backbone
from timm.models.layers import DropPath, trunc_normal_
from torch import nn


class Block(nn.Module):
    def __init__(self, dim, drop_path=0.0, layer_scale_init_value=1e-6):
        super().__init__()
        self.dwconv = nn.Conv2d(dim, dim, kernel_size=7, padding=3, groups=dim)
        self.norm = nn.LayerNorm(dim, eps=1e-6)

        self.pwconv1 = nn.Linear(dim, 4 * dim)
        self.act = nn.GELU()

        self.pwconv2 = nn.Linear(4 * dim, dim)
        self.gamma = (
            nn.Parameter(layer_scale_init_value * torch.ones((dim)), requires_grad=True)
            if layer_scale_init_value > 0
            else None
        )
        self.drop_path = DropPath(drop_path) if drop_path > 0.0 else nn.Identity()

    def forward(self, x):
        input = x
        x = self.dwconv(x)
        x = x.permute(0, 2, 3, 1)  # (N, C, H, W) -> (N, H, W, C)
        x = self.norm(x)
        x = self.pwconv1(x)
        x = self.act(x)
        x = self.pwconv2(x)
        if self.gamma is not None:
            x = self.gamma * x
        x = x.permute(0, 3, 1, 2)  # (N, H, W, C) -> (N, C, H, W)

        x = input + self.drop_path(x)
        return x


class ConvNeXt(Backbone):
    """
    A PyTorch impl of : `A ConvNet for the 2020s` - https://arxiv.org/abs/2201.03545
    """

    def __init__(
        self,
        in_chans: int = 3,
        depths: list[int] = [3, 3, 9, 3],
        dims: list[int] = [96, 192, 384, 768],
        drop_path_rate: float = 0.0,
        layer_scale_init_value: float = 1e-6,
        out_features: list[str] | None = None,
    ):
        """
        Args:
            in_chans: Number of input image channels.
            depths: Number of blocks at each stage.
            dims: Feature dimension at each stage.
            drop_path_rate: Stochastic depth rate.
            layer_scale_init_value: Init value for Layer Scale.
            out_features: Stage numbers of the outputs given to the Neck.
        """
        super().__init__()

        # stem and 3 intermediate downsampling conv layers
        self.downsample_layers = nn.ModuleList()
        stem = nn.Sequential(
            nn.Conv2d(in_chans, dims[0], kernel_size=4, stride=4),
            LayerNorm2d(dims[0], eps=1e-6),
        )

        self.downsample_layers.append(stem)
        for i in range(3):
            downsample_layer = nn.Sequential(
                LayerNorm2d(dims[i], eps=1e-6),
                nn.Conv2d(dims[i], dims[i + 1], kernel_size=2, stride=2),
            )
            self.downsample_layers.append(downsample_layer)

        self.num_layers = len(depths)
        num_features = [int(dims[i] * 2**i) for i in range(self.num_layers)]
        self.num_features = num_features
        self._out_features = out_features

        self._out_feature_strides = {}
        self._out_feature_channels = {}

        # 4 feature resolution stages, each consisting of multiple residual blocks
        self.stages = nn.ModuleList()
        dp_rates = [x.item() for x in torch.linspace(0, drop_path_rate, sum(depths))]
        cur = 0
        strides = [4, 4, 4, 4]
        for i in range(4):
            stage = nn.Sequential(
                *[
                    Block(
                        dim=dims[i],
                        drop_path=dp_rates[cur + j],
                        layer_scale_init_value=layer_scale_init_value,
                    )
                    for j in range(depths[i])
                ]
            )
            self.stages.append(stage)
            cur += depths[i]

            self._out_feature_channels[f"res{i + 2}"] = dims[i]
            self._out_feature_strides[f"res{i + 2}"] = strides[i] * 2**i

        norm_layer = partial(LayerNorm2d, eps=1e-6)
        for i_layer in range(4):
            layer = norm_layer(dims[i_layer])
            layer_name = f"norm{i_layer}"
            self.add_module(layer_name, layer)

        self.apply(self._init_weights)

    def _init_weights(self, m):
        if isinstance(m, (nn.Conv2d, nn.Linear)):
            trunc_normal_(m.weight, std=0.02)
            nn.init.constant_(m.bias, 0)

    def init_weights(self, pretrained=None):
        """Initialize the weights in backbone.
        Args:
            pretrained (str, optional): Path to pre-trained weights.
                Defaults to None.
        """

        def _init_weights(m):
            if isinstance(m, nn.Linear):
                trunc_normal_(m.weight, std=0.02)
                if isinstance(m, nn.Linear) and m.bias is not None:
                    nn.init.constant_(m.bias, 0)
            elif isinstance(m, nn.LayerNorm) or isinstance(m, LayerNorm2d):
                nn.init.constant_(m.bias, 0)
                nn.init.constant_(m.weight, 1.0)

        self.apply(_init_weights)

    def forward_features(self, x):
        outs = {}
        for i in range(4):
            x = self.downsample_layers[i](x)
            x = self.stages[i](x)

            if f"res{i + 2}" in self._out_features:
                norm_layer = getattr(self, f"norm{i}")
                x_out = norm_layer(x)
                out = x_out.contiguous()
                outs[f"res{i + 2}"] = out

        return outs

    def forward(self, x):
        x = self.forward_features(x)
        return x
