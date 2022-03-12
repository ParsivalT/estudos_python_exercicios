'''
Desafio 88 

Problema: Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
          O programa vai perguntar quantos jogos serão gerados e vai sortear 6 
          números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
          
Resolucao do problema:
'''
from random import sample
from time import sleep

palpites = []
valor = int(input('Quantos valores deseja sortear?: '))

for c in range(valor):
    palpites.append(sample(range(1,60), 6))

print('='*49)       
print('>'*14 + ' Os palpites foram ' + '<'*15)
print('='*49)

for c in range(len(palpites)):
    print(f'{c+1}º palpite: {sorted(palpites[c])}')
    sleep(1)
    
print('='*49)