# Model Configs for Benchmarking

Each sub-directory contains Detectron2 config files (`LazyConfig` format) for
all model checkpoints from public Github repos building with Detectron2.

- `d2main`: Detectron2 model zoo (initial baselines).
- `d2lsj`: Detectron2 model zoo (new LSJ baselines).
- `vitdet`: https://github.com/facebookresearch/detectron2/tree/main/projects/ViTDet
- `convnext`: https://github.com/facebookresearch/convnext
- `mvitv2`: https://github.com/facebookresearch/detectron2/tree/main/projects/MViTv2
- `mask2former`: https://github.com/facebookresearch/Mask2Former

Additionally, `common` directory has config objects that are shared across many
config files.

### Note on config structure

Detectron2 lazy configs are described in the official Detectron2 documentation
[here](https://detectron2.readthedocs.io/en/latest/tutorials/lazyconfigs.html).
Each config file requires five objects: `dataloader`, `model`, `optimizer`,
`lr_multiplier`, `train`. Some configs may exclude two objects that are not
required for evaluation - `optimizer` and `lr_multiplier`.
