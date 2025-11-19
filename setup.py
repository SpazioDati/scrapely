#!/usr/bin/env python
"""
Setup script for building Cython extensions.
All package metadata is defined in pyproject.toml.
"""
from setuptools import setup
from setuptools.extension import Extension
from Cython.Build import cythonize

try:
    import numpy as np
    include_dirs = [np.get_include()]
except ImportError:
    include_dirs = []

extensions = cythonize([
    Extension(
        "scrapely._htmlpage",
        ["scrapely/_htmlpage.pyx"],
        include_dirs=include_dirs,
    ),
    Extension(
        "scrapely.extraction._similarity",
        ["scrapely/extraction/_similarity.pyx"],
        include_dirs=include_dirs,
    ),
])

setup(ext_modules=extensions)
