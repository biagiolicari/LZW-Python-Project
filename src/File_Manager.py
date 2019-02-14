#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  2 12:38:29 2019
@author: Biagio
"""

import os
from src.converter import convertinbits,number_from_bytestring
from pathlib import Path
from src.Compress import Compress,timer
from src.Uncompress import Uncompress,timer_uncompress
import shutil

#from Uncompress import Uncompress
BYTEDIM = 8
pattern = ['.z','.c','.cc','.xml','.html','.py','.htm','.cpp','.rtf','.json','.txt'] #pattern possibili da comprimere
pattern_compressed = ['.Z', '.z']    #pattern lzw 

'''funzione che nel caso in cui il file sia gia compresso con estensione .z, ne modifica l'estensione'''
def check_ext (path):  
        base = os.path.splitext(path)[0]
        os.rename(path,base+".Z")
        
'''funzione che ritorna la dim in bytes del file passato come argomento'''
def file_size(fname): 
    path = Path(fname)
    if path.is_file() :
        statinfo = os.stat(path)
        return statinfo.st_size
    elif path.is_dir() :
        dir_size = directory_size(path)
        return dir_size
    
'''funzione che ritorna la dimensione della dir passata come argomento, in bytes''' 
def directory_size(path):
    total_size = 0
    seen = set()

    for dirpath, dirnames, filenames in os.walk(path): #ricerca ricorsiva all'interno della dir
        for f in filenames:
            fp = os.path.join(dirpath, f)

            try:
                stat = os.stat(fp)
            except OSError:
                continue

            if stat.st_ino in seen:
                continue

            seen.add(stat.st_ino)

            total_size += stat.st_size
        return total_size  # size in byte

                   

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
         
''' Funzione che comprime una intera cartella con annesse subdir presenti all'interno contenenti file compatibili col pattern specificato '''
def write_dir(dirname,dt,verbose) :
    
    p = Path(dirname).resolve()

    for p in p.rglob('*'): #ricerca ricorsiva all'interno del dir Path specificato di file compatili per essere compressi
        if p.suffix == '.z' :
            check_ext(p)
        else :
            if p.suffix in pattern :
                try :
                    size_b = file_size(p) #size prima della compressione per ogni file preso in considerazione
                    f = open(p,'r')
                            
                    if verbose == False:
                        cod_compressed,bin_compressed = Compress(f.read(),dt)
                        
                    elif verbose == True:
                        compress_verbose = timer(Compress)
                        cod_compressed,bin_compressed = compress_verbose(f.read(),dt) #cod_compressed,bin_compressed = Compress(f.read(),dt) #richiamo la definizione di Compressione sul file specificato usando il dizionario o il trie
                   
                    write(bin_compressed,os.path.join(p.parent,p.stem)) #richiamo la funzione che scrive il file compresso
                    f.close()
                    newpath = p.with_suffix('.z')
                    size_a = file_size(newpath)
                    if size_b < size_a:
                        if verbose == True :
                            print("Il file : ", newpath.name, " risulta maggiore dell'originale")
                        newpath.unlink()
                    else:
                        shutil.copymode(p,newpath)
                        p.unlink()
                except IOError :
                    print('errore in apertura di ', p)
                
                                             

'''funzione che comprime un determinato file inerente al pattern impostato'''
def write_file(filename, dict_or_trie,verbose,ric):
    path = Path(filename).resolve()
    
    if path.is_dir() and ric == True : #nel caso in cui la modalita ricorsiva sia attiva e il file passato è una dir, chiamo la funzione write_dir()
        b_size = directory_size(path)
        write_dir(path,dict_or_trie,verbose)

        if verbose == True:
            a_size = directory_size(path)
            percent = (b_size - a_size)/b_size * 100
            print("Compressione avvenuta del {} %".format(percent))            
      
    elif path.is_file() :
        if path.suffix == '.z' or path.suffix == '.Z' :
            check_ext(path) #controllo se file è stato già compresso e nel caso modifico estensione

        else :
            try :
                size_before = file_size(path) #calcolo dimensione prima della compressione
                f = open(path,'r')
                
                if verbose == False: 
                    cod_compressed,bin_compressed = Compress(f.read(),dict_or_trie)
                if verbose == True: #se la modalita verbose è attiva applico il decoratore timer alla funzione compress
                    compress_verbose = timer(Compress)
                    cod_compressed,bin_compressed = compress_verbose(f.read(),dict_or_trie)
                    
                write(bin_compressed,os.path.join(path.parent,path.stem))#richiamo la funzione write
                f.close()
                newpath = path.with_suffix('.z') 
                size_after = file_size(newpath) #calcolo la dimensione del file post_compressione
                
                if size_before < size_after:
                    newpath.unlink() #se la dimensione pre-compressione è superiore elimino il file compresso
                    
                else:
                    shutil.copymode(path,newpath)
                    path.unlink()
                    
                if verbose == True:
                    if not newpath.exists():
                        print("Il file : ", newpath.name, " risulta maggiore dell'originale")
                        return 
                    percent = (size_before - size_after)/size_before * 100
                    print("Compressione avvenuta del {} %".format(percent))
                    
            except IOError as ex :
                print('Errore nel file : ', ex)
    else :
        print("Inserire correttamente le opzioni di ricerca " )
        return -1
            
    return 0

'''funzione di ricerca file nel caso in cui is_file() è true, ritorna il codice del file compresso e la sua path abs'''         
def search(filename):
    
    path = Path(filename).resolve()
       
    bin_code = []
    abspath = []
    
    if path.is_file() : #se il path rappresenta un file eseguo i controlli per l'estensione     
        if path.suffix in pattern_compressed :
            abspath.append(path)
            dec = read(path)
            bin_code.append(dec)
                
    elif path.is_dir() : #se il path è un dir si decomprimono tutti i file all'interno
        for p in path.rglob('*'):
            if p.suffix in pattern_compressed :
                abspath.append(p)
                dec = read(p)
                bin_code.append(dec)
        
    return bin_code,abspath

'''Funzione che dato un path, una delle st_dati possibili e un argomento -r permettere di decomprimere un/a file/dir'''
def Uncompress_file(filename,dt,r,verbose):
    i = 0
    
    filename = Path(filename).resolve()
    if filename.is_file() :
        bin_cod,path = search(filename) #richiamo la funzione di ricerca file/dir
        
    elif r == True and filename.is_dir() :
        bin_cod,path = search(filename)
        
    else :
        print("Inserire correttamente le opzioni di ricerca")
        return -1

    for _ in bin_cod :
        
        if verbose == True: 
            uncompress_verbose = timer_uncompress(Uncompress) #richiamo decoratore timer_uncompress nel caso in cui la modalita verbose sia attiva
            dec = uncompress_verbose(_,dt) #ottengo stringa decompressa
        elif verbose == False:
            dec = Uncompress(_,dt) #ottengo stringa decompressa
            
        name = Path(path[i]) #estraggo path del file decompresso
        f = open(os.path.join(name.parent,name.stem+'.txt'), 'w') #creazione nuovo file decompresso
        f.write(dec)
        f.close()
        shutil.copymode(name, os.path.join(name.parent,name.stem+'.txt'))
        name.unlink() #rimuovo il file compresso
        i += 1
       