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
    
    
    def __str__(self):
        '''Stampa la lista di adiacenza. Viene usata da print().'''
        s = ""
        for i in range(0,len(self.__nodes)):
            s = s + self.__nodes[i][0].__str__() + " --> " + self.__nodes[i][1].__str__() + "\n"
        return s 
    
   
    def addnode(self, node): 
        '''Funzione che aggiunge un nodo alla lista'''
        self.__nodes.append((node,[]))
    
    
    #si sfrutta la sequenzialità dei nodi. Ogni valore del nodo sta al node+1 posto nella lista
    def addchildtonode(self, node, child, label):
        '''Funzione che permette di creare un arco da node a child con una label'''
        self.__nodes[node+1][1].append((child, label))
        

    def search(self, char):
        '''Funzione che cerca il prossimo carattere a partire dal nodo attuale.
       Ritorna il valore del nodo figlio del nodo attuale che ha come label
       nell' arco il carattere se questo arco esiste, modificando il nodo 
       attuale con il figlio, altrimenti torna il nodo, attuale e lo modifica 
       con -1, tornando così alla radice.'''
        
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
    
    
    def check(self):
        '''Funzione che torna True se ancora non si è ricominciato da capo nel trie '''
        #Il check è vero se siamo nella root, quindi se il valore di mynode = -1
        if self.__mynode == -1:
            return True
        else:
            return False
        
    
class lzw_dict() :
    '''Classe che implementa un dizionario, sfruttando la coppia <chiave,valore>, per implementare la compressione/decompressione di Lempel-Ziv-Welch'''

    def __init__(self) :
        self.__dim = 257 #END compreso
        self.__dict = {chr(i) : i for i in range(self.dim)} #costruisco il dizionario con coppia <chr(i),i)>
        self.__curr = ""
        self.__controllo = 0
        self.__value = 0
        self.__key = ""
        
        
        super().__setattr__('dict',self.__dict)
        super().__setattr__('dim',self.__dim)
        super().__setattr__('curr',self.__curr)
        super().__setattr__('controllo',self.__controllo)
        super().__setattr__('vaue',self.__value)
        super().__setattr__('key',self.__key)
        
        
    @property
    def controllo(self):
        return self.__controllo
    
    @controllo.setter
    def controllo(self, chk):
        self.__controllo = chk

    @property
    def value(self):
        return self.__value
    
    @value.setter
    def controllo(self, val):
        self.__value = val
    
    @property
    def key(self):
        return self.__key
    
    @key.setter
    def key(self, k):
        self.__key = k
    
    @property
    def dim(self):
        return self.__dim
    
    @dim.setter
    def dim(self, newdim):
        self.__dim = newdim
        
    @property
    def dict(self):
        return self.__dict
    
    @dict.setter
    def dict(self, newdict):
        self.__dict = newdict
 
    
    
    def __str__(self) :
        '''Funzione che stampa il dizionario'''
        return self.__dict


    def search(self, char) :
        self.__key = self.__curr + char 
        #se il valore di key è presente nel dizionario, ritorno col valore presente nel dizionario creato
        if self.__key in self.__dict : #         
           self.__curr = self.__key
           self.__controllo= 0
           self.__value = self.__dict[self.__key] 
        #altrimenti aggiungo tale valore al dizionario, andando ad impostare curr pari a "" per la prossima iterazione
        else :            
            self.__dict[self.__key] = self.__dim 
            self.__dim += 1
            self.__curr = ""
            self.__controllo = -1

        return self.__value
        



    def check(self) :
        if self.__controllo == -1 :
            return True
        else :
            return False
            

#Nella decompressione per ricostruire un path a partire da un valore è
#importante conoscere il padre di un nodo, che è unico.
class trie_uncompression:

    '''Il trie per la decompressione è un dizionario che associa a ogni nodo una
    coppia (father,label)'''
    def __init__(self):
        self.__lastencoded = ""
        self.__lastnode = -1
        self.__dim = 257
        self.__dict_for_trie = {i : (-1, chr(i)) for i in range(self.dim)}
        
        super().__setattr__('lastencoded',self.__lastencoded)
        super().__setattr__('last',self.__lastnode)
        super().__setattr__('dim',self.__dim)
        super().__setattr__('dict_for_trie',self.__dict_for_trie)
        
    @property
    def lastencoded(self):
        return self.__lastencoded
    
    @lastencoded.setter
    def lastencoded(self, encoded):
        self.__lastencoded = encoded
    
    @property
    def last(self):
        return self.__lastnode
    
    @last.setter
    def last(self, node):
        self.__lastnode = node
    
    @property
    def dim(self):
        return self.__dim
    
    @dim.setter
    def dim(self, newdim):
        self.__dim = newdim
        
    @property
    def dict_for_trie(self):
        return self.__dict_for_trie
    
    @dict_for_trie.setter
    def dict_for_trie(self, newdict):
        self.__dict_for_trie = newdict


    def __str__(self):
        return self.__dict_for_trie.__str__()
    
    def find(self,value):
        #condizione di proiezione
        if value == self.__dim:
            string = self.__lastencoded + self.__lastencoded[0]
            self.__lastencoded = string
            self.__dict_for_trie[value] = (self.__lastnode, string[0])
            self.__lastnode = value
            self.__dim = self.__dim + 1 
            return string
        
        edge = self.__dict_for_trie[value]
        string = edge[1] #prima label dell'arco
        while edge[0] != -1: #finche il padre dell'arco non è -1
            edge = self.__dict_for_trie[edge[0]] #guardo il nodo padre
            string = edge[1] + string
        
        self.__dict_for_trie[self.__dim] = (self.__lastnode, string[0])
        self.__dim = self.__dim + 1
        self.__lastencoded = string
        self.__lastnode = value
        return string
    
    
class Dict_uncompression:
    def __init__(self) :
        self.__dim = 257
        self.__dictionary = {i : chr(i) for i in range(self.dim)}
        self.__curr = ""
        self.__lastencoded = ""
            
        super().__setattr__('last') #ACCETTABILE???
        super().__setattr('dim',self.__dim)
        super().__setattr('dictionary',self.__dictionary)
        super().__setattr('curr',self.__curr)
        super().__setattr('lastencoded',self.__lastencoded)
        
    @property
    def last(self):
        return 
    
    @last.setter
    def last(self, node):
        return
    
    @property
    def dim(self):
        return self.__dim
    
    @dim.setter
    def dim(self, newdim):
        self.__dim = newdim
        
    @property
    def curr(self,newcurr):
        self.__curr = newcurr
        
    @curr.setter
    def curr(self):
        return self.__curr
    
    @property
    def lastencoded(self):
        return self.__lastencoded
    
    @lastencoded.setter
    def lastencoded(self, encoded):
        self.__lastencoded = encoded
        
    @property
    def dictionary(self):
        return self.__dict_for_trie
    
    @dictionary.setter
    def dictionary(self, newdict):
        self.__dict_for_trie = newdict
        
    def find(self,v) :
        if v in self.__dictionary:
            self.__curr = self.__dictionary[v]
            self.__dictionary[self.__dim] = self.__lastencoded+self.__curr[0]
            self.__dim += 1
            self.__lastencoded = self.__curr
            return self.__lastencoded
        else: #proiezione
            self.__dictionary[self.dim] = self.__lastencoded + self.__lastencoded[0]
            self.__dim += 1
            self.__curr = self.__dictionary[v]
            self.__lastencoded = self.__curr
            return self.__lastencoded
            
        
        