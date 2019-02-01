#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  1 10:44:17 2019

@author: Biagio
"""

import argparse
import src.File_Manager, src.converter

parser = argparse.ArgumentParser()  # Creiamo il nostro parser
parser.add_argument('file',help='lista file o dir da comprimere con lzw',type = str)
gruppo = parser.add_argument_group() # Creiamo il gruppo necessario per le visualizzazioni
gruppo2 = parser.add_argument_group()
gruppo.add_argument("-r", "--ricorsivo", action="store_true")
gruppo2.add_argument("-t","--trie", action="store_true")
gruppo2.add_argument("-d","--dict", action="store_true")
gruppo.add_argument("-v","--verbose", action="store_true")

arg = parser.parse_args()


if arg.ricorsivo and arg.trie :
    src.File_Manager.write_dir(arg.file,'t')
elif arg.ricorsivo and arg.dict:
    src.File_Manager.write_dir(arg.file,'d')
elif arg.ricorsivo :
    src.File_Manager.write_dir(arg.file,'t')
if arg.trie and not arg.ricorsivo :
    src.File_Manager.write_file(arg.file,'t')
elif arg.dict and not arg.ricorsivo :
    src.File_Manager.write_file(arg.file,'d')
else:
    src.File_Manager.write_file(arg.file,'t')
    
    

