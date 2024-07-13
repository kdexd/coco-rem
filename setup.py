#!/usr/bin/env python
from setuptools import find_packages, setup

setup(
    name="coco_rem",
    version="0.1",
    python_requires=">=3.8",
    zip_safe=True,
    packages=find_packages(include=["coco_rem"]),
)
