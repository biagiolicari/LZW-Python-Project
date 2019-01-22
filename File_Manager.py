# -*- coding: utf-8 -*-
"""
Created on Wed Jan  2 12:38:29 2019

@author: Biagio
"""

import os
from converter import convertinbits
from pathlib import Path

BYTEDIM = 8            
'''
def Search_File(name) :
    z=''
    abspath=""
    for root, dirs, files in os.walk(os.getcwd()):
        for file in files:
            if file == name : 
                if os.path.isfile :
                   abspath = os.path.join(root,file)                 
                   f = open(os.path.join(root, file),"rb")                   
                   for byte in f.read() :               
                       z += (convertinbits(byte,BYTEDIM))
                   f.close()
                                     
            
    return z,abspath   
'''
            
def decompress_file(filename) :
    z = ''
    f = open(os.path.abspath(filename),'rb')
    for byte in f.read() :
        z+=(convertinbits(byte,BYTEDIM))
        f.close()
    return z
    

def search_file(Name) :
    
    bin_code = []
    abspath = []

    for root,dirs,files in os.walk(os.getcwd()):
        for file in files:
            if file == Name and os.path.isfile(os.path.join(root,file)) :
                abspath.append(os.path.join(root,file))
                code = decompress_file(os.path.join(root,file)) 
                bin_code.append(code)
                break
            elif os.path.isdir(os.path.join(root,Name)):
                bin_code,abspath = search_dir(Name)
                       
        return bin_code,abspath

def search_dir(dirname) :
    #mposto la Path della directory da considerare, dove cercare i file lzw 
    p = Path(dirname)
    abspath = []
    bin_code = []
    #Uso la funzione rglob che mi permette di socrrere ricorsivamente le sottocartelle della Path alla ricerca di eventuali file lzw
    for p in p.rglob('*.Z') :
        abspath.append(p.resolve()) #aggiungo la path assoluta alla lista di ritorno
        dec = decompress_file(p.resolve()) #richiamo la funzione decompress_file per ogni elelemento lzw all'interno di una qualsiasi dir
        bin_code.append(dec) # aggiungo il testo decompresso ad una lista
        
    return bin_code,abspath
        
    
t,v=search_file('Compressed')
for i in t :
    print(i)

for i in v:
    print(i)
    
