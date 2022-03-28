'''
Desafio 115

Problema: Crie um pequeno sistema modularizado que permita cadastrar pessoas pelo
                        seu nome e idade em um arquivo de texto simples.
                        O sistema só vai ter 2 opções: cadastrar uma nova pessoa e listar todas
                        as pessoas cadastradas.

Resolucao do problema:
'''
from ex115modulos.menu import menu
from ex115modulos.manipulacao_arquivos import *

arquivo = 'banco_dados.txt'

if not arquivoExiste(arquivo):
    criaArquivo('banco_dados.txt')

menu(True)
