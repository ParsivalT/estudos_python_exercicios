'''
Desafio 54

Problema:  Crie um programa que leia o ano de nascimento de sete pessoas. 
           No final, mostre quantas pessoas ainda não atingiram a maioridade 
           e quantas já são maiores.

Resolucao do problema:           
'''
maior = 0
menor = 0

for c in range(0, 8):
    i = int(input('Digite A Idade Da Pessoa: '))
    
    if i >= 18:
        maior += 1

    else:
        menor += 1

print(f'Dessas 7 pessoas {maior} Ja sao de maior! e {menor} Sao De menor!')
