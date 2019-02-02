#!/usr/bin/env python3

from distutils.core import setup

setup(name='Lempel-Ziv-Welch',
      version='1.0',
      description='Lempel-Ziv-Welch compressor and decompressor',
      author='Biagio Licari & Gabriele Felici',
      license='MIT',
      packages=['src'],
      scripts = ['script/compress', 'script/uncompress'],
     )
