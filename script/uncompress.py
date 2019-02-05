#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  1 10:44:17 2019

@author: Biagio
"""

import argparse
import src.File_Manager

parser = argparse.ArgumentParser()  # Creiamo il nostro parser
parser.add_argument('file',help='lista file o dir da comprimere con lzw',type = str)
gruppo_r = parser.add_argument_group() # Creiamo il gruppo necessario per le opzioni ricorsive 
gruppo_stdati = parser.add_argument_group() #gruppo opzioni dict o trie
gruppo_v = parser.add_argument_group() #opzione verbose
gruppo_r.add_argument("-r", "--ricorsivo", action="store_true", help = 'opzione per la ricerca ricorsiva all interno di dir') #argomento -r che permette la ricerca ricorsiva se file = dir
gruppo_stdati.add_argument("-t","--trie", action="store_true", help = 'opzione per usare LZW tramite struttura Trie') #argomento st_dati trie
gruppo_stdati.add_argument("-d","--dict", action="store_true", help = 'opzione per usare LZW tramite struttura Dict')#argomento st_dati dict
parser.add_argument("-v","--verbose", action="store_true", help = 'opzione per visualizzare la verbose ')

arg = parser.parse_args() #parse degli argomenti passati 

if arg.trie :
    src.File_Manager.Uncompress_file(arg.file,'t',arg.ricorsivo,arg.verbose)
elif arg.dict :
    src.File_Manager.Uncompress_file(arg.file,'d',arg.ricorsivo,arg.verbose)
else:
    src.File_Manager.Uncompress_file(arg.file,'t',arg.ricorsivo,arg.verbose)

   
        