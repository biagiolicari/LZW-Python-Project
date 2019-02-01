#!/usr/bin/env python3

from distutils.core import setup

setup(name='Lempel-Ziv-Welch',
      version='1.0.0',
      description='Lempel-Ziv-Welch compressor and decompressor',
      author='mauro Leoncini',
      author_email='leoncini@unimore.it',
      url='https://github.com/Linguaggi-Dinamici-2018-Modulo-Python/',
      license='MIT',
      packages=['src','script'],
      scripts = ['script/compress.py', 'script/uncompress.py'],
     )
