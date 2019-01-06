#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  3 17:36:51 2019

@author: Gabriele Felici
"""
from stdativ2 import trie
from stdict import lzw_dict

def Compression(input_File, char):
    
    stringa_compressa = []
    if char == "D" or char == "d" :
        T = lzw_dict()
    
    elif char == "T" or char == "t" :
        T = trie()

    else :
        T = lzw_dict()        
        
    dim = len(input_File)
    counter = 0
    
    #ciclo che esamina ogni carattere   
    for C in input_File:
        #provo a cercare il prossimo carattere
        val = T.search(C)
        counter = counter + 1 #incremento il contatore dei caratteri
        
        if T.check() :
            stringa_compressa.append(val)
            val = T.search(C)
        
        if counter == dim :
            stringa_compressa.append(val)
    
    stringa_compressa.append(256);
    return stringa_compressa
    

test = Compression("BANANA_BANDANA", "T")
print(test)