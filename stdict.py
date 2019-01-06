# -*- coding: utf-8 -*-
"""
Created on Fri Jan  4 10:23:26 2019

@author: Biagio
"""
class lzw_dict() :

    def __init__(self) :
        self.dim = 257
        self.dict = {chr(i) : i for i in range(self.dim)}
        self.curr = ""
        self.conta = 0
        self.value = 0
        self.key = ""
 
    

    def __str__(self) :
        return self.dict


    def search(self, char) :
        self.key = self.curr + char
        
        if self.key in self.dict : 
           self.curr = self.key
           self.conta= 0
           self.value = self.dict[self.key]

            
        else :
            
            self.dict[self.key] = self.dim
            self.dim += 1
            self.curr = ""
            self.conta = -1

        return self.value
        


    
    def check(self) :
        if self.conta == -1 :
            return True
        else :
            return False
            
   
            
                   