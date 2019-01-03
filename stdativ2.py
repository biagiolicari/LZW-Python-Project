#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 30 19:24:45 2018

@author: Gabriele Felici
"""
'''Classe che rappresenta un trie v2.0'''

class trie():
    ''' Classe che rappresenta un trie. Utilizza le liste di adiacenza.
        La struttura consiste in una lista contenente coppie di valori.
        Il primo valore indica il nodo, il secondo è la sua lista di adiacenza
        contenente ulteriori coppie di valori (child, label)'''
    
    def __init__(self):
        self.nodes = []
        self.dim = 257 #END compreso
        self.root = -1
        self.mynode = -1
        self.nodes.append((-1,[]))
        for i in range(0,self.dim):
            self.nodes[0][1].append((i,chr(i)))
            self.nodes.append((i,[]))
            
    '''Stampa la lista di adiacenza. Viene usata da print().'''
    def __str__(self):
        s = ""
        for i in range(0,len(self.nodes)):
            s = s + self.nodes[i][0].__str__() + " --> " + self.nodes[i][1].__str__() + "\n"
        return s 
    
    '''Funzione che aggiunge un nodo alla lista'''
    def addnode(self, node):
        self.nodes.append((node,[]))
    
    '''Funzione che permette di creare un arco da node a child con una label'''
    #si sfrutta la sequenzialità dei nodi. Ogni valore del nodo sta al node+1 posto nella lista
    def addchildtonode(self, node, child, label):
        self.nodes[node+1][1].append((child, label))
        
    '''Funzione che cerca il prossimo carattere a partire dal nodo attuale.
       Ritorna il valore del nodo figlio del nodo attuale che ha come label
       nell' arco il carattere se questo arco esiste, modificando il nodo 
       attuale con il figlio, altrimenti torna il nodo, attuale e lo modifica 
       con -1, tornando così alla radice.'''
    def search(self, char):
        #la lista dei figli non è vuota, cerco il valore con l'arco che ha label il carattere che cerco
        if self.nodes[self.mynode+1][1]:
            nodi_child = self.nodes[self.mynode+1][1] #ottengo la lista di adiacenza del node
            for i in range(0, len(nodi_child)):
                if nodi_child[i][1] == char:
                    self.mynode = nodi_child[i][0]
                    return self.mynode
        #se la lista di adiacenza del nodo attuale è vuota (il nodo attuale non ha figli)
        #o se non è stata trovata una label con il carattere cercato
        #aggiugo il figlio alla lista dei nodi, lo aggiungo come figlio del nodo attuale e
        #salvo il nodo attuale per il ritorno, modificando poi il nodo attuale con -1
        self.addnode(self.dim)
        self.addchildtonode(self.mynode, self.dim, char)
        self.dim = self.dim + 1
        value = self.mynode
        self.mynode = -1
        return value
    
    '''Funzione che torna True se ancora non si è ricominciato da capo nel trie '''
    def check(self):
        #Il check è vero se siamo nella root, quindi se il valore di mynode = -1
        if self.mynode == -1:
            return True
        else:
            return False