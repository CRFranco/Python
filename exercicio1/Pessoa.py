#!/usr/bin/env python
# -*- coding: utf8 -*-

class Pessoa:
    
    def __init__(self, cd, nm=None, st=None, alt=None):
        self.codigo = cd
        self.nome = nm
        self.status = st
        self.altura = alt
    
    # TODO verificar se o tipo é o mesmo, mas não achei como :( 
    def equals(self, pessoa):
        if(self.codigo == pessoa.codigo):
            return True;
        return False;
    
    def toString(self):
        return self.codigo ,", Nome: ",self.nome

    
   
            
