# -*- coding: utf-8 -*-
from setuptools import setup

setup(
    name="create-pypi-cli",
    version="0.1.0",
    py_modules=["main"],
    install_requires=[
        "click",
    ],
    entry_points={
        "console_scripts": [
            "create-pypi-cli = main:main",
        ],
    },
)
