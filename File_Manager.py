# -*- coding: utf-8 -*-
"""
Created on Wed Jan  2 12:38:29 2019

@author: Biagio
"""

import os

def Search_File() :

    for root, dirs, files in os.walk(os.getcwd()):
        for file in files:
            if file.endswith(".txt"):           
                f = open(os.path.join(root, file),"r")
                
                print(os.path.join(root, file))
                
                contenuto = f.read().split(',') 
                f.close()
                
                compressed = [int(i) for i in contenuto]
                return compressed
            
            
prova = Search_File()
print(prova)
                

            

  


            
            


            
            

    
            
            
            