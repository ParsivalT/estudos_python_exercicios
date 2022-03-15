'''
Desafio 99

Problema: Faça um programa que tenha uma função chamada maior(), que 
          receba vários parâmetros com valores inteiros. Seu programa 
          tem que analisar todos os valores e dizer qual deles é o maior.
          
Resolucao do problema:
'''
from time import sleep

def maior(*num):
    
    if num:

        maior = cont = 0

        print('='*30)
        print('Analisando os valores...')
        for pos, valor in enumerate(num):
            sleep(0.7)
            print(valor, end=' ', flush=True) #sem o flush vira um buff visual

            if pos == 0:
                maior = valor

            if valor > maior:
                maior = valor
            cont += 1

        print()
        print(f'Foram informados {cont} valores ao todo')
        print(f'O maior valor encontrado foi: {maior}')
        

    else:
        print('\033[31mErro! nenhum valor foi informado!\033[m')


#programa principal
maior(2,5,7,8,14)   
maior(14,5,2,6)
maior(6)
maior()
