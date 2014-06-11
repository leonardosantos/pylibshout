import sys
from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext
import os

os.environ['PKG_CONFIG_PATH'] += ':/app/.apt/usr/lib/pkgconfig:/app/.dpkg/usr/lib/x86_64-linux-gnu/pkgconfig/'
os.environ['C_INCLUDE_PATH'] += ':/app/.apt/usr/include/:/app/.dpkg/usr/include/'
os.environ['LIBRARY_PATH'] += ':/app/.apt/usr/lib/:/app/.dpkg/usr/lib/x86_64-linux-gnu/'

argv = []
argv.append(sys.argv[0])
argv.append('build_ext')
argv.append('--inplace')
sys.argv = argv

ext_modules = [Extension(
    "pylibshout", ["pylibshout.pyx"],
    libraries = ['shout'] #.h files
)]

setup(
    cmdclass = {'build_ext': build_ext},
    ext_modules = ext_modules,
)

#build it: python setup.py build_ext --inplace
#create distribution: python setup.py sdist
