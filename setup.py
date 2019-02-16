#!/usr/bin/env python3

from distutils.core import setup
import sys

if not sys.version_info.major >= 3 :
    sys.exit("Sorry, only Python 3 is supported (yet)")
    

setup(name='Lempel-Ziv-Welch',
      version='1.0.0',
      python_requires = '>= 3.5.2',
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
