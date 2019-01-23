# -*- coding: utf-8 -*-
"""
Created on Wed Jan  2 12:38:29 2019

@author: Biagio
"""

import os
from converter import convertinbits,write
from pathlib import Path
from Compression import Compression

BYTEDIM = 8            
        
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
            if file == Name and os.path.isfile(os.path.join(root,Name)):
                bin_code,abspath = search_onlyfile(Name)

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

def write_dir(dirname,dt) :
    p = Path(dirname)
    for p in p.rglob('*.txt'):
        f = open(p,'r')
        cod_compressed,bin_compressed = Compression(f.read(),dt)
        write(bin_compressed,os.path.join(p.parent,p.stem))
        f.close()
        p.unlink()


def search_onlyfile(filename):
    p = Path.cwd()
    abspath = []
    bin_code=[]
    
    for p in p.rglob(filename) :
        abspath.append(p.resolve())
        dec = decompress_file(p.resolve())
        bin_code.append(dec)
    return bin_code,abspath
    


def write_file(filename, dict_or_trie):
    path = Path.cwd()
    
    for file in path.rglob(filename):
        if file.is_file() :
            f = open(file,'r')
            cod_compressed,bin_compressed = Compression(f.read(),dict_or_trie)
            write(bin_compressed,os.path.join(file.parent,file.stem))
            f.close()
            file.unlink()
        if file.is_dir() :
            write_dir(file,dict_or_trie)
    return 0



write_file('Compressed','d')
            
