'''
Desafio 82

Problema:  Crie um programa que vai ler vários números e colocar em uma 
           lista. Depois disso, crie duas listas extras que vão conter apenas 
           os valores pares e os valores ímpares digitados, respectivamente. Ao 
           final, mostre o conteúdo das três listas geradas.
           
Resolucao do problema:
'''
lista = []
pares = []
impares = []

while True:

    print('='*30)
    lista.append(int(input('Digite um valor: ')))
    continua = str(input('Deseja continuar? [S/N]: ')).upper()

    while continua not in 'SN':

        continua = str(input('Deseja continuar? [S/N]: ')).upper()

    if continua == 'N':
        break


for pos, valor in enumerate(lista):
    if valor % 2 == 0:  #par
        pares.append(valor)

    if valor % 2 == 1:   #impar
        impares.append(valor)

print('='*30)
print(f'Lista original: {lista}\nPares: {pares}\nImpares: {impares}')
print('='*30)
