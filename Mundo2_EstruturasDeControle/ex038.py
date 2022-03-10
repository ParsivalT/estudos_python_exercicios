'''
Desafio 38

Problema: Escreva um programa que leia dois números inteiros e compare-os.
mostrando na tela uma mensagem:

– O primeiro valor é maior

– O segundo valor é maior

– Não existe valor maior, os dois são iguais

Resolucao do problema: 
'''

n1 = int(input('Digite O Primeiro Numero: '))
n2 = int(input('Digite O Segundo Numero: '))

if n1 > n2: 

    print(f'O Maior Valor digitado foi: {n1}')

elif n1 == n2: 

    print(f'Nao Existe Valor MAIOR Ou MENOR Os Dois Sao Iguais!')

else: 

    print(f'O Maior Valor Digitado foi: {n2}')
