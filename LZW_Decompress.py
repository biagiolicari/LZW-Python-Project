# -*- coding: utf-8 -*-
"""
Created on Fri Dec 21 12:36:53 2018

@author: Biagio
"""
def LZW_Decompress(compressed)  :
  dict_dim = 256
  dictionary = { c : chr(c)  for c in range(dict_dim)}
#decodifica primo elemento di compressed
  curr = dictionary.pop(compressed[0]) #prendo primo elemento compressed
  decompressed = curr
  carattere=""
  for C in compressed[1:] :      
    #se C non è nel dizionario aggiorno la aggiungo alla stringa altrimenti controllo il codice char
    if C not in dictionary:
      
      carattere += curr 
    else:
      carattere = dictionary[C]
      
      
    decompressed += carattere
    dict_dim +=1
    dictionary[dict_dim] = curr + carattere[0]
    curr = carattere
    
  return decompressed


        
test = [66, 65, 78, 258, 65, 95, 257, 78, 68, 260, 262, 260, 259]
decompressed = LZW_Decompress(test)
print (decompressed)