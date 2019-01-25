#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 11 17:29:17 2019

@author: Gabriele Felici
"""
from stdati import trie_decompression,Dict_decompression
from converter import convertinint
from File_Manager import search
from converter import write
import os
from pathlib import Path

def Decompress_trie(bitstring):
    #MANCA IL CASO PARTICOLARE
   
    T = trie_decompression()
    numbits = 9
    val = convertinint(bitstring[0:numbits],numbits)
    string = chr(val)

    T.lastencoded = string
    T.lastnode = val
    indexiniziale = 0
    indexfinale = 9
    
    while val != 256:       
        if T.dim + 1 == 2**numbits:
            numbits = numbits+1      
        indexiniziale = indexfinale
        indexfinale = indexfinale + numbits
        valstring = bitstring[indexiniziale:indexfinale]
        val = convertinint(valstring, numbits)
 
        if val != 256:
            string = string + T.find(val)
    
    return string


def Decompress(filename):
    i = 0
    bin_cod,path = search(filename) #richiamo la funzione di ricerca file/dir
    
    for _ in bin_cod :
        dec = Decompress_trie(_) #ottengo stringa decompressa
        name = Path(path[i]) #estraggo path del file decompresso
        f = open(os.path.join(name.parent,name.stem+'.txt'), 'w') #creazione nuovo file decompresso
        f.write(dec)
        f.close()
        name.unlink() #rimuovo il file compresso
        i += 1

Decompress('C:/Users/Biagio/Desktop/Jupyter-notebooks-master/tr')