'''
Desafio 98

Problema: Faça um programa que tenha uma função chamada contador(), 
          que receba três parâmetros: início, fim e passo. Seu programa 
          tem que realizar três contagens através da função criada:
          
                 a) de 1 até 10, de 1 em 1
                 b) de 10 até 0, de 2 em 2
                 c) uma contagem personalizada
          
Resolucao do problema:
'''
from time import sleep
import abc 

def contador(i,f,p):
    
    if p == 0:
        p = 1
    if p < 0:
        p *= -1

    if i < f:
        cont = i
        print('De 1 a 10 de 1 em 1:')

        while cont != f:

            sleep(0.7)
            print(cont, end=' ', flush=True)
            cont += p
        print('FIM')
        
    else:
        if i >= f:
            cont = i
            print('De 10 a 0 de 2 em 2:')

            while cont >= f:

                sleep(0.7)
                print(cont, end=' ', flush=True)
                cont -= p
            print('FIM')


print('='*24)
contador(1, 11, 1)
print('='*24)
contador(10, 0, 2)
print('='*24)

print('Sua vez de personalizar! \n')

i = int(input('Digite o inicio: '))
f = int(input('Digite o fim: '))
p = int(input('Digite o paso: '))

contador(i,f,p)
print('='*24)