#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  6 09:48:22 2018

@author: Gabriele Felici
"""
BYTEDIM = 8
 
     
def convertinbits(value, numbits):
    ''' Funzione che converte un valore intero in una stringa "0/1" '''   
    B = ''
    for _ in range(0,numbits):
        B = str(int(value)%2) + B
        value = int(value)/2
    return B

   
def convertinint(bits, numbits):
    ''' Funzione che converte una stringa "0/1" in un valore intero ''' 
    value = 0
    for i in range(0,numbits):
        bit = bits[numbits-1-i]
        value = value + (2**i) * int(bit)
    return value


def number_from_bytestring(bitstring):
    ''' Funzione che dato in ingresso una stringa rappresentante un byte, torna il valore numerico di quel byte '''
    v = 0
    power = [2**i for i in range(0,BYTEDIM)]
    for j in range(0,BYTEDIM):
        v = v + int(bitstring[j])*power[BYTEDIM-1-j]
    return v




