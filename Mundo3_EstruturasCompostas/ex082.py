#recebe valores e os guarda em uma lista, depois os dividem e pares e impares
#for thiago 07/03/2022

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
