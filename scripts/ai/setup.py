from setuptools import setup
from Cython.Build import cythonize

setup (
    ext_modules=cythonize("alpha_beta_pruning.pyx")
)