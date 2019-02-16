#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 11 17:29:17 2019

@author: Gabriele Felici
"""
from src.stdati import trie_uncompression,Dict_uncompression
from src.converter import convertinint
import time

def timer_uncompress(func):
    def inner(*args, **kwargs):
        t1 = time.time()
        f = func(*args, **kwargs)
        t2 = time.time()
        print('Uncompress Algorithm took {} seconds'.format(t2-t1))
        return f
    return inner


def Uncompress(bitstring,td):
    '''Funzione che data in input una strina di bit 0/1, ricava il valore numerico
    su una porzione n_bit(inizialmente 9) e, mediante le strutture dati, ricostruisce
    il testo.
    Per ogni valore si utilizza la find, che restituisce la sequenza associata al valore.'''
    
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
