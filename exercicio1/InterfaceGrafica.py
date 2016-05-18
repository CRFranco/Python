#!/usr/bin/env python
# -*- coding: utf8 -*-

from Persistencia import Persistencia
from Pessoa import Pessoa


persistencia = Persistencia()
persistencia.recuperaLista()

def lerPessoa():
    codigo = int(input('Codigo : '))
    nome = input('Nome : ')
    status = bool(input('Status : '))
    altura = float(input('Altura : '))
    return Pessoa(codigo, nome, status, altura)

def incluir():        
    persistencia.gravaPessoa(lerPessoa())

def alterar():
    codigoQuery = int(input('Digite o código da pessoa a ser alterada:'))
    if (persistencia.existePessoa(codigoQuery)):
        persistencia.atualizaPessoa(lerPessoa())
    else:
        print('Pessoa inexistente')
        
def excluir():
    codigoQuery = int(input('Digite o código da pessoa a ser excluida:'))
    if (persistencia.existePessoa(codigoQuery)):
        persistencia.excluiPessoa(Pessoa(codigoQuery))
    else:
        print('Pessoa inexistente')

def exibir():
    codigoQuery = int(input('Digite o código da pessoa a ser exibida:'))
    if (persistencia.existePessoa(codigoQuery)):
        pessoa = persistencia.recuperaPessoa(codigoQuery) 
        print(pessoa.toString())
    else:
        print('Pessoa inexistente')
        
def listar():
    lista = persistencia.lista()
    for p in lista:
        print(p.toString())
        

    

#-------------------------INTERFACE GRÁFICA------------------------------
#queria limpar a tela, mas não achei como
print('_______________________________________________________________')
print('CRUD CADASTROS \n')


sentinela = 1
while sentinela != 0:
    
    print('1 - incluir Pessoa:')
    print('2 - alterar Pessoa:')
    print('3 - excluir Pessoa:')
    print('4 - exibir Pessoa:')
    print('5 - listar Pessoas:')
    print('0 - encerrar o programa')
    sentinela = int(input('Escolha uma opcao:'))

    if (sentinela ==1):
        incluir()
    elif (sentinela==2):
        alterar()
    elif (sentinela==3):
        excluir()
    elif (sentinela==4):
        exibir()
    elif (sentinela==5):
        listar()
    elif (sentinela==0):
        persistencia.persisteLista()

    



