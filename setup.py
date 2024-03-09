# -*- coding: utf-8 -*-
import sys

from setuptools import find_packages, setup


def get_description(file_path, max_length=70):
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()
        sentences = content.replace(";", ".").split(".")
        description = sentences[0].strip()
        if len(description) > max_length:
            words = description.split()
            description = ""
            for word in words:
                if len(description) + len(word) + 1 <= max_length:
                    description += " " + word
                else:
                    break
            description = description.strip() + "..."
        return description


with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

description = get_description("README.md")

# Get the major version of Python
python_major_version = sys.version_info.major

setup(
    name="create-pypi-cli",
    version="0.1.1",
    packages=find_packages(),
    description=description,
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT",
    python_requires=f">={python_major_version}",
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
