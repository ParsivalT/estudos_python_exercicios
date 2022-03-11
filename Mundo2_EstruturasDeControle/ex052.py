'''
Desafio 52

Problema: Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

resolucao do problema:
'''
i = int(input('Digite O Numero que deseja checar: '))
cont = 0 

for c in range(1, i+1):

    if i % c == 0:
        print(f'\033[32m{c}', end=' ')

        cont += 1

    else:
         print(f'\033[m{c}', end=' ')

if cont <=2:
    print(f'\n\033[mO Numero {i} foi dividido {cont} vezes! e \033[36mPRIMO!\033[m')

else:
    print(f'\n\033[mO Numero {i} foi dividido {cont} vezes! \033[31mNAO E  PRIMO\033[m!')
