'''
Desafio 59

Problema:  Crie um programa que leia dois valores e mostre um menu na tela:

[ 1 ] somar

[ 2 ] multiplicar

[ 3 ] maior

[ 4 ] novos números

[ 5 ] sair do programa

Seu programa deverá realizar a operação solicitada em cada caso.

Resolucao do problema:
'''
import os  #posso executar comandos no terminal com esse modulo 

ma = 0
m = 0 
v1 = int(input('Valor1: '))
v2 = int(input('Valor2: '))

while m != 5:
    
    m = int(input('''>>>>>>>DIGITE<<<<<<<

[1] para somar
[2] para multiplicar
[3] para saber qual o maior
[4] novos numeros 
[5] sair
-----------------------
: '''))
    print('-='*30)

    if m == 1:
        print(f'O Valor Da soma Entre {v1} e {v2} e: {v1+v2}')
    
    elif m == 2:
        print(f'Ao multiplicar {v1} e {v2} temos como resultado: {v1*v2}')

    elif m == 3:
        
        if v1 > v2:
            print(f'O maior valor e: {v1}')

        else:
            print(f'O maior valor e: {v2}')

    elif m == 4:
        print('Digite Os novos valores:')
        v1 = int(input('Valor1: '))
        v2 = int(input('Valor2: '))
    input('''
Prescione ENTER para continuar''')    
   
    os.system('clear')