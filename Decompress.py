#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 11 17:29:17 2019

@author: Gabriele Felici
"""
from stdati import trie_decompression

def Decompress(values):
    dict_dim = 256
    dictionary = { v : chr(v)  for v in range(dict_dim)}
    
    string = ""
    char = dictionary[values[0]]
    string = char 
    curr = ""
    #caso particolare
    if values[1] >= 257:
        curr = char + char
        string = string + curr
        dict_dim = dict_dim + 1
        dictionary[dict_dim] = curr
    else:
        curr = dictionary[values[1]]
        string = string + curr # ho scritto i primi caratteri
        dict_dim = dict_dim + 1
        dictionary[dict_dim] = string
        
    lasttxt = string[1]
    for v in values[2:]:

        #lasttxt = curr #valore prima di curr
        
        if v in dictionary: #v dovrebbe SEMPRE essere nel dizionario
            curr = dictionary[v] #mi segno l'ultima stringa estratta
            string = string + curr
            dict_dim = dict_dim + 1
            dictionary[dict_dim] = lasttxt + curr[0]
            lasttxt = curr
            
        else:
            curr = lasttxt + lasttxt[0]
            string = string + curr
            dict_dim = dict_dim+1 #aggiungo il nodo
            dictionary[dict_dim] = curr
            lasttxt = curr
            
        #string = string + curr
        
    return string

def Decompress_trie(values):
    #MANCA IL CASO PARTICOLARE
    T = trie_decompression()
    string = chr(values[0])
    T.lastencoded = string
    T.lastnode = values[0]
    for v in values[1:]:
        string = string + T.find(v)
    return string