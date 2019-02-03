#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  1 10:44:17 2019
@author: Biagio
"""

import argparse
import src.File_Manager, src.converter

parser = argparse.ArgumentParser()  # Creiamo il nostro parser
parser.add_argument('file',help='lista file o dir da comprimere con lzw',default = [], nargs = '+') #aggiungo l'argomento di tipo lista da usare per la compressione/decompressione file/dir
gruppo_r = parser.add_argument_group() # Creiamo il gruppo necessario per le opzioni ricorsive 
gruppo_stdati = parser.add_mutually_exclusive_group() #gruppo opzioni dict o trie
gruppo_v = parser.add_argument_group() #opzione verbose
gruppo_r.add_argument("-r", "--ricorsivo", action="store_true") #argomento -r che permette la ricerca ricorsiva se file = dir
gruppo_stdati.add_argument("-t","--trie", action="store_true") #argomento st_dati trie
gruppo_stdati.add_argument("-d","--dict", action="store_true")#argomento st_dati dict
gruppo_v.add_argument("-v","--verbose", action="store_true")

arg = parser.parse_args() #parse degli argomenti passati 

for _ in arg.file:

    if arg.ricorsivo and arg.trie :
        src.File_Manager.write_dir(_,'t')
    elif arg.ricorsivo and arg.dict:
        src.File_Manager.write_dir(_,'d')
    elif arg.ricorsivo :
        src.File_Manager.write_dir(_,'t')
    if arg.trie:
        src.File_Manager.write_file(_,'t')
    elif arg.dict :
        src.File_Manager.write_file(_,'d')
    else:
        src.File_Manager.write_file(_,'t')
