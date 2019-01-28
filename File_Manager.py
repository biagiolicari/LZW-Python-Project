# -*- coding: utf-8 -*-
"""
Created on Wed Jan  2 12:38:29 2019

@author: Biagio
"""

import os
from converter import convertinbits,number_from_bytestring
from pathlib import Path
from Compress import Compress
#from Uncompress import Uncompress
BYTEDIM = 8
pattern = ['*.txt','*.c','*.cc','*.xml','*.html','*.py','*.htm','*.cpp', '*.z', '*.lzw'] #pattern possibili da comprimere
pattern_compressed = ['*.Z', '*.z', '*.lzw']    #pattern lzw        

'''Funzione che legge all'interno di un determinato file compresso e ritorna la stringbit da dare in pasto al decompressore '''        
def read(filename) :
    z = ''
    try :
        f = open(os.path.abspath(filename),'rb')
        try :
            for byte in f.read() :
                z+=(convertinbits(byte,BYTEDIM))
        except (ImportError, EOFError) as ex :
            print('errore imprevisto : ' , ex)
                
    except IOError as ioerr:
        print('File not found :', ioerr)
        
    finally :
        f.close()
        
    return z

''' Funzione che scrive su file la stringa compressa'''
def write(stringbits, filename):
     with open(filename+'.z', "wb") as f:
         if len(stringbits)%BYTEDIM != 0:
             for _ in range(0, BYTEDIM-(len(stringbits)%BYTEDIM)):
                 stringbits += '0' #aggiungo il padding se serve
         numbytes = int(len(stringbits)/BYTEDIM)
         bytevalues = []
         for i in range(0,numbytes):
             bytevalues.append(number_from_bytestring(stringbits[BYTEDIM*i:BYTEDIM*(i+1)]))
         f.write(bytes(bytevalues))
         
def search(filename):
    path = Path(filename).resolve()
    bin_code = []
    abspath = []
    
    if path.is_file() : #se il path rappresenta un file eseguo i controlli per l'estensione     
        for _ in pattern_compressed : #se il file rientra nelle etensioni previste si esegue la decompressione
            if path.suffix == _[1:] :
                abspath.append(path)
                dec = read(path)
                bin_code.append(dec)
                
    if path.is_dir() : #se il path è un dir si decomprimono tutti i file all'interno
        bin_code,abspath = search_dir(path)
        
    return bin_code,abspath

        
def search_dir(dirname) :
    #mposto la Path della directory da considerare, dove cercare i file lzw 
    p = Path(dirname)
    abspath = []
    bin_code = []
    for _ in pattern_compressed :
        #Uso la funzione rglob che mi permette di socrrere ricorsivamente le sottocartelle della Path alla ricerca di eventuali file lzw
        for p in p.rglob(_) :
            abspath.append(p.resolve()) #aggiungo la path assoluta alla lista di ritorno
            dec = read(p.resolve()) #richiamo la funzione decompress_file per ogni elelemento lzw all'interno di una qualsiasi dir
            bin_code.append(dec) # aggiungo il testo decompresso ad una lista
        
    return bin_code,abspath

''' Funzione che comprime una intera cartella con annesse subdir presenti all'interno contenenti file compatibili col pattern specificato '''
def write_dir(dirname,dt) :
    p = Path(dirname)
    
    for _ in pattern :
        for p in p.rglob(_): #ricerca ricorsiva all'interno del dir Path specificato di file compatili per essere compressi
            try :
                f = open(p,'r')
                cod_compressed,bin_compressed = Compress(f.read(),dt) #richiamo la definizione di Compressione sul file specificato usando il dizionario o il trie
                write(bin_compressed,os.path.join(p.parent,p.stem)) #richiamo la funzione che scrive il file compresso
                f.close()
                p.unlink() #elimino il file dato in pasto al compressore
            except IOError :
                print('errore in apertura di ', p)


def write_file(filename, dict_or_trie):
    path = Path(filename).resolve()
      
    if path.is_file() :
        try :
            f = open(path,'r')
            cod_compressed,bin_compressed = Compress(f.read(),dict_or_trie)
            write(bin_compressed,os.path.join(path.parent,path.stem))
            f.close()
            path.unlink()
        except IOError as ex :
            print('Errore nel file : ', ex)
         
    if path.is_dir() :
            write_dir(path,dict_or_trie)
            
    return 0


#write_file('Compressed','d')
            
