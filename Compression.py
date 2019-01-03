#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  3 17:36:51 2019

@author: Gabriele Felici
"""
from stdativ2 import trie

def Compression(input_File):
    
    stringa_compressa = []
    T = trie()
        
    dim = len(input_File)
    counter = 0
    
    #ciclo che esamina ogni carattere   
    for C in input_File:
        #provo a cercare il prossimo carattere
        val = T.search(C)
        counter = counter + 1 #incremento il contatore dei caratteri
        
        if T.check():
            stringa_compressa.append(val)
            val = T.search(C) # riposiziono il nodo su quello attuale dalla root
       
        if counter == dim: # se ho cercato l'ultimo carattere
            stringa_compressa.append(val)
        
    stringa_compressa.append(256);
    
    return stringa_compressa
