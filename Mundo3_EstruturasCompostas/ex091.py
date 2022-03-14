'''
Desafio 91

Problema: Crie um programa onde 4 jogadores joguem um dado e tenham resultados 
          aleatórios. Guarde esses resultados em um dicionário em Python. No final, 
          coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número 
          no dado.
          
Resolucao do problema: 
'''
from random import randint
from time import sleep
from operator import itemgetter

print('='*30)

jogadores = {'Jogador1':(randint(1,6)), 'jogador2':(randint(1,6)),
             'Jogador3':(randint(1,6)), 'Jogador4':(randint(1,6))}

for k, v in jogadores.items():
    print(f'{k} tirou: {v} no dado')
    sleep(1)

print('='*30)
print('Rank dos jogadores!')
print('='*30)

rank = sorted(jogadores.items(), key=itemgetter(1), reverse=True)

for pos, valor in enumerate(rank):
    print(f'{pos+1} {valor[0]} com: {valor[1]}')
