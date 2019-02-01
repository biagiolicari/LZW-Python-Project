#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  1 10:44:17 2019

@author: Biagio
"""

import argparse
import src.Uncompress

parser = argparse.ArgumentParser()  # Creiamo il nostro parser
parser.add_argument('file',help='lista file o dir da comprimere con lzw',type = str)
gruppo = parser.add_mutually_exclusive_group() # Creiamo il gruppo necessario per le visualizzazioni
gruppo.add_argument("-r", "--ricorsivo", action="store_true")

arg = parser.parse_args()


if arg.ricorsivo :
    src.Uncompress.Uncompress_file(arg.file,'t', True)
else:
    print('senza dir')
    src.Uncompress.Uncompress_file(arg.file,'t', False)