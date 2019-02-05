#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 11 17:29:17 2019

@author: Gabriele Felici
"""
from src.stdati import trie_uncompression,Dict_uncompression
from src.converter import convertinint
import time

def timer(func):
    def inner(*args, **kwargs):
        t1 = time.time()
        f = func(*args, **kwargs)
        t2 = time.time()
        print('Runtime took {} seconds'.format(t2-t1))
        return f
    return inner


def Uncompress(bitstring,td):
    #MANCA IL CASO PARTICOLARE
    
    if td == 't' or 'T' or 'trie' :
        T = trie_uncompression()
    elif td == 'd' or 'D' or 'dict' :
        T = Dict_uncompression()
    else:
        T = trie_uncompression()
        
    numbits = 9
    val = convertinint(bitstring[0:numbits],numbits)
    string = chr(val)

    T.lastencoded = string
    T.last = val #nel caso del trie salva l'ultimo nodo, nel dict non fa nulla
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
