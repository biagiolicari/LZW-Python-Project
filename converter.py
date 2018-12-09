#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  6 09:48:22 2018

@author: Gabriele Felici
"""

''' Funzione che converte un valore intero in una stringa "0/1" '''        
def convertinbits(value, numbits):
    B = ''
    for _ in range(0,numbits):
        B = str(int(value)%2) + B
        value = int(value)/2
    return B

''' Funzione che converte una stringa "0/1" in un valore intero '''    
def convertinint(bits, numbits):
    value = 0
    for i in range(0,numbits):
        bit = bits[numbits-1-i]
        value = value + (2**i) * int(bit)
    return value

