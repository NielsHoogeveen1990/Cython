from setuptools import setup, find_packages
from Cython.Build import cythonize
import numpy as np


setup(
    name='Cython-package-1',
    version='1.1',
    author='Niels Hoogeveen',
    package_dir={'':'src'},
    packages=find_packages(where='src'),
    entry_points={'console_scripts': ['CYTHON = Cython_app.cli:main']},
    ext_modules = cythonize("src/Cython_app/Cython_package/primes.pyx"),
    include_dirs=np.get_include(),
)

# To compile Cython code:
# python setup.py build_ext --inplace