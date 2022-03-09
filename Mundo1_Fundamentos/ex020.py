#Criar uma lista 

from random import shuffle 

n1 = str(input('Digite Um nome: '))
n2 = str(input('Digite Um nome: '))
n3 = str(input('Digite Um nome: '))
n4 = str(input('Digite Um nome: '))

lista = [n1, n2, n3, n4]
shuffle(lista)

print(f'A ordem foi escolhida foi: {lista}')

