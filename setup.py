#!/usr/bin/env python3

from distutils.core import setup

setup(name='Lempel-Ziv-Welch',
      version='1.0.0',
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
      scripts = ['script/compress', 'script/uncompress'],
     )
