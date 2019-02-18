#!/usr/bin/env python3

from distutils.core import setup
import platform
import sys

if platform.python_version() < '3.6' :
    sys.exit("Sorry, only Python 3.6 or > are supported (yet)")
    

setup(name='LZW compressor',
      version='1.0.0',
      python_requires = '>= 3.6.5',
      install_requires=[
            'argparse',
            'setuptools',
            'docutils.core',
            'distutils',
            'pathlib',
           ],
      description='Lempel-Ziv-Welch compressor and decompressor',
      author='Biagio Licari & Gabriele Felici',
      license='MIT',
      packages=['src'],
      scripts = ['script/Compress', 'script/Uncompress'],
     )
