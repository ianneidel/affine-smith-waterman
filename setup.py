#!/usr/bin/python
__author__ = "Ian Neidel"
__email__ = "ian.neidel@yale.edu"
__copyright__ = "Copyright 2021"
__license__ = "GPL"
__version__ = "1.0.0"

import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='affine-smith-waterman',
    version='1.0',
    author='Ian Neidel',
    author_email='ian.neidel@yale.edu',
    description='An implementation of the Smith-Waterman algorithm, supporting an affine gap penalty',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/ianneidel/affine-smith-waterman',
    project_urls = {
        "Bug Tracker": "https://github.com/ianneidel/affine-smith-waterman/issues"
    },
    license='GPL',
    packages=['affine-smith-waterman'],
    install_requires=['numpy','pandas','argparse'],
)