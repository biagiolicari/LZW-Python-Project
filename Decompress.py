#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 11 17:29:17 2019

@author: Gabriele Felici
"""
from stdati import trie_decompression,Dict_decompression
from converter import convertinint
import File_Manager
from converter import write
import os
"""
def __init__(self) :
    self.dim = 256
    self.dictionary = { v : chr(v)  for v in range(dict_dim)}
    
    self.string = ""
    char = dictionary[values[0]]
    string = char 
    curr = ""
def find(self,values):

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
    
"""

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
