#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 30 19:24:45 2018

@author: Gabriele Felici
"""
'''Codice python contenente le strutture dati utilizzazte dal compressore LZW.
    Ogni oggetto python che implementa la struttura dati deve implementare un
    metodo search(char) che cerca il valore del carattere/sequenza nella 
    struttura, e un metodo check che permette di controllare se l'ultimo valore
    non può essere aggiornato al nuovo valore corrispondente a stringa + char'''

class trie():
    ''' Classe che rappresenta un trie. Utilizza le liste di adiacenza.
        La struttura consiste in una lista contenente coppie di valori.
        Il primo valore indica il nodo, il secondo è la sua lista di adiacenza
        contenente ulteriori coppie di valori (child, label)'''
    
    def __init__(self):
        self.__nodes = []
        self.__dim = 257 #END compreso
        #self.__root = -1
        self.__mynode = -1
        self.__nodes.append((-1,[]))
        for i in range(0,self.__dim):
            self.__nodes[0][1].append((i,chr(i)))
            self.__nodes.append((i,[]))
        
        
        super().__setattr__('nodes',self.__nodes)
        super().__setattr__('dim',self.__dim)
        super().__setattr__('mynode',self.__mynode)
    
    @property
    def nodes(self):
        return self.__nodes
    
    @nodes.setter
    def nodes(self, nodes_list):
        self.__node = nodes_list
    
    @property
    def dim(self):
        return self.__dim
    
    @dim.setter
    def dim(self, newdim):
        self.__dim = newdim
    
    @property
    def mynode(self):
        return self.__mynode
    
    @mynode.setter
    def mynode(self, newmynode):
        self.__mynode = newmynode
    
    '''Stampa la lista di adiacenza. Viene usata da print().'''
    def __str__(self):
        s = ""
        for i in range(0,len(self.__nodes)):
            s = s + self.__nodes[i][0].__str__() + " --> " + self.__nodes[i][1].__str__() + "\n"
        return s 
    
    '''Funzione che aggiunge un nodo alla lista'''
    def addnode(self, node):
        self.__nodes.append((node,[]))
    
    '''Funzione che permette di creare un arco da node a child con una label'''
    #si sfrutta la sequenzialità dei nodi. Ogni valore del nodo sta al node+1 posto nella lista
    def addchildtonode(self, node, child, label):
        self.__nodes[node+1][1].append((child, label))
        
    '''Funzione che cerca il prossimo carattere a partire dal nodo attuale.
       Ritorna il valore del nodo figlio del nodo attuale che ha come label
       nell' arco il carattere se questo arco esiste, modificando il nodo 
       attuale con il figlio, altrimenti torna il nodo, attuale e lo modifica 
       con -1, tornando così alla radice.'''
    def search(self, char):
        #la lista dei figli non è vuota, cerco il valore con l'arco che ha label il carattere che cerco
        if self.__nodes[self.__mynode+1][1]:
            nodi_child = self.__nodes[self.__mynode+1][1] #ottengo la lista di adiacenza del node
            for i in range(0, len(nodi_child)):
                if nodi_child[i][1] == char:
                    self.__mynode = nodi_child[i][0]
                    return self.__mynode
        #se la lista di adiacenza del nodo attuale è vuota (il nodo attuale non ha figli)
        #o se non è stata trovata una label con il carattere cercato
        #aggiugo il figlio alla lista dei nodi, lo aggiungo come figlio del nodo attuale e
        #salvo il nodo attuale per il ritorno, modificando poi il nodo attuale con -1
        self.addnode(self.__dim)
        self.addchildtonode(self.__mynode, self.__dim, char)
        self.__dim = self.__dim + 1
        value = self.__mynode
        self.__mynode = -1
        return value
    
    '''Funzione che torna True se ancora non si è ricominciato da capo nel trie '''
    def check(self):
        #Il check è vero se siamo nella root, quindi se il valore di mynode = -1
        if self.__mynode == -1:
            return True
        else:
            return False
        
    
class lzw_dict() :
    '''Classe che implementa un dizionario, sfruttando la coppia <chiave,valore>, per implementare la compressione/decompressione di Lempel-Ziv-Welch'''

    def __init__(self) :
        self.dim = 257 #END compreso
        self.dict = {chr(i) : i for i in range(self.dim)} #costruisco il dizionario con coppia <chr(i),i)>
        self.curr = ""
        self.controllo = 0
        self.value = 0
        self.key = ""
 
    
    '''Funzione che stampa il dizionario'''
    def __str__(self) :
        return self.dict


    def search(self, char) :
        self.key = self.curr + char 
        '''se il valore di key è presente nel dizionario, ritorno col valore presente nel dizionario creato.'''
        if self.key in self.dict : #         
           self.curr = self.key
           self.controllo= 0
           self.value = self.dict[self.key] 
        #altrimenti aggiungo tale valore al dizionario, andando ad impostare curr pari a "" per la prossima iterazione
        else :            
            self.dict[self.key] = self.dim 
            self.dim += 1
            self.curr = ""
            self.controllo = -1

        return self.value
        



    def check(self) :
        if self.controllo == -1 :
            return True
        else :
            return False
            
'''Nella decompressione per ricostruire un path a partire da un valore è
importante conoscere il padre di un nodo, che è unico.
Il trie per la decompressione è un dizionario che associa a ogni nodo una
coppia (father,label)'''

class trie_uncompression:
    
    def __init__(self):
        self.lastencoded = ""
        self.lastnode = -1
        self.dim = 257
        self.dict_for_trie = {i : (-1, chr(i)) for i in range(self.dim)}
        
    def __str__(self):
        return self.dict_for_trie.__str__()
    
    def find(self,value):
        #condizione di proiezione
        if value == self.dim:
            string = self.lastencoded + self.lastencoded[0]
            self.lastencoded = string
            self.dict_for_trie[value] = (self.lastnode, string[0])
            self.lastnode = value
            self.dim = self.dim + 1 
            return string
        
        edge = self.dict_for_trie[value]
        string = edge[1] #prima label dell'arco
        while edge[0] != -1: #finche il padre dell'arco non è -1
            edge = self.dict_for_trie[edge[0]] #guardo il nodo padre
            string = edge[1] + string
        
        self.dict_for_trie[self.dim] = (self.lastnode, string[0])
        self.dim = self.dim + 1
        self.lastencoded = string
        self.lastnode = value
        return string
    
    def set_lastencoded(self, string):
        self.lastencoded = string
        
    def set_lastnode(self,node):
        self.lastnode = node
        
        
        
        
class Dict_uncompression:
    def __init__(self) :
        self.dim = 257
        self.dictionary = {i : chr(i) for i in range(self.dim)}
        self.curr = ""
        self.lastencoded = ""
        self.val = ""
            
    
    def find(self,v) :
        if v in self.dictionary:
            self.curr = self.dictionary[v]
            self.dictionary[self.dim] = self.lastencoded+self.curr[0]
            self.dim += 1
            self.lastencoded = self.curr
            return self.lastencoded
        else:
            self.dictionary[self.dim] = self.lastencoded + self.lastencoded[0]
            self.dim += 1
            self.curr = self.dictionary[v]
            self.lastencoded = self.curr
            return self.lastencoded
            

            
    def set_lastencoded(self,string):
        self.lastencoded = string
        
    def set_lastnode(self,val):
        self.curr=val
            
        
        