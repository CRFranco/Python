#!/usr/bin/env python
# -*- coding: utf8 -*-

import pickle
import os


class Persistencia:
    _lista = []
    FILENAME = 'pessoas.dat'
    
    #TODO verificar por duplicatas
    def gravaPessoa(self, pessoa):
        self._lista.append(pessoa)
      
    
    def atualizaPessoa(self, pessoa):
        indice = 0 # variavel criada para achar o indice da pessoa a ser excluida
        for p in (self._lista):
            if(p.equals(pessoa)):
                self._lista.pop(indice)
                self._lista.append(pessoa)
            indice += 1   
    
    def lista(self):
        return self._lista
    
    def excluiPessoa(self, pessoa):
        indice = 0 # variavel criada para achar o indice da pessoa a ser excluida
        for p in (self._lista):
            if(p.equals(pessoa)):
                self._lista.pop(indice)
            indice += 1
    
    
    def persisteLista(self):
        pickle.dump(self._lista, open(self.FILENAME, 'wb'))
    
    def existePessoa(self, codigoASerBuscado):
            for p in (self._lista):
                if(p.codigo==codigoASerBuscado):
                    return True
            return False
        
    def recuperaPessoa(self, codigoASerBuscado):      
            for p in (self._lista):
                if(p.codigo==codigoASerBuscado):
                    return p
            return None
            
    def recuperaLista(self):
        if(os.path.exists(self.FILENAME)):
            self._lista = pickle.load(open(self.FILENAME, 'rb'))
        return self._lista
    
    
    
    
    
    
    