'''
Desafio 114

Problema: Crie um código em Python que teste se o site pudim está acessível 
          pelo computador usado.
          

Resolucao do problema:
'''
import requests

try:

    site = requests.get('http://www.pudim.com.br/')
    print('\033[36mO Site pudim esta funcionando!\033[m')

except:

    print('\033[31mTivemos um problema:')
    print('Infelizmente nao consegui acessar o site pudim :(\033[m')

