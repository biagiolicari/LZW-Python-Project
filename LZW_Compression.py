# -*- coding: utf-8 -*-
"""
Created on Sat Dec  8 20:18:23 2018

@author: Biagio
"""
"""
#COMPRESSIONE_LZW(INPUT):
#    STRINGA_txt_corrente = ""
#   TABELLA[da 0 a 255] = byte da 0 a 255
#   per ogni carattere C dell'INPUT:
#       STRINGA_txt_corrente = STRINGA_txt_corrente + C
#       SE STRINGA_txt_corrente NON e' presente in TABELLA:
#           STRINGA_PRESENTE = STRINGA_txt_corrente - ULTIMO CARATTERE
#           CODICE = Indice di STRINGA_PRESENTE in TABELLA
#           EMETTI CODICE come output
#           TABELLA = TABELLA + STRINGA_txt_corrente
#           STRINGA_txt_corrente = C
#           ... continua il ciclo col prossimo carattere ...
#   CODICE = Indice di STRINGA_txt_corrente in TABELLA
#   EMETTI CODICE come output
 """
 
from converter import convertinbits

def LZW_Compression(input_File):
    
    carattere = ""
    stringa_compressa = []
    dictionary_dim = 256
    dictionary = { chr(i) : i for i in range(dictionary_dim)} #Creiamo il dizionario con tutti i 256 codici ASCII esteso
    
        
    #ciclo che esamina ogni carattere   
    for C in input_File:
        txt_corrente = carattere + C #creo variabile @txt_corrente che conterra parte di testo
        
        #se @txt_corrente è gia presente nel dizionario allora carattere assume i valori in txt_corrente
        if txt_corrente in dictionary :
            carattere = txt_corrente
            
        #altrimenti aggiungiamo all'array @stringa_compressa ciò che è contenuto in @corrente, andando ad aggiungere txt_corrente al dizionario
        else :
            stringa_compressa.append(dictionary[carattere])
            dictionary_dim += 1
            dictionary[txt_corrente] = dictionary_dim
            carattere = C
    #svuotiamo il testo ancora presente in @carattere    
    if carattere != "" :     
        stringa_compressa.append(dictionary[carattere])
        
    #aggiungiamo 256 che rappresenta l'END
    stringa_compressa.append(256);
    print(dictionary)
    
    return stringa_compressa

'''Converte una lista di valori in un'unica stringa di testo '0/1' su 9 bit (MANCA ANCORA LO SWITCH A PIU BIT)''' 
def Conversion(values):
    S = ""
    for i in values:
        S = S + convertinbits(i,9)
    return S
        
            
test=LZW_Compression("BANANA_BANDANA_BANANA")
print(test)           
        
    
    