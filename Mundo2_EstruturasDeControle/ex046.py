'''
Desafio 46

Problema: Faça um programa que mostre na tela uma contagem regressiva para 
          o estouro de fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.
          
Resolucao do problema:
'''
from time import sleep 

print('-='*30)
print('A Contage Regressiva Esta Preste A Comecar!')
print('-='*30)

for c in range(10, 0,-1):
    print(c)
    sleep(2)

print('\033[36mFELIZ ANO NOVO\033[m')