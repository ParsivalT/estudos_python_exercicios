#sortei 5 valores aleatores e adicione a uma tupla 
#Logo em seguida Mostre os valores, qual o menor e qual o maior
from random import randint

n1 = n2 = n3 = n4 = n5 = 0
print('='*38)
for i in range(0, 6):

    if i == 1:
        n1 = randint(1,10)
    else:
        if i == 2:
            n2 = randint(1,10)
        else:
            if i == 3:
                n3 = randint(1,10)
            else:
                if i == 4:
                    n4 = randint(1,10)
                else:
                    if i == 5:
                        n5 = randint(1,10)                   

lista = (n1,n2,n3,n4,n5)

print(f'Os valores sorteados foram: ', end=' ')
for c in range(len(lista)):
    print(lista[c],end=' ')

print()
                   # Uma outra forma de saber qual o menor eo maior e max(lista)/min(lista)
                   # Economizaria linhas 
menor = lista[0]
maior = lista[0]
for x in range(len(lista)):

    if lista[x] > maior:
        maior = lista[c]

    else:
        if lista[x] < menor:
            menor = lista[x]

print(f'O maior valor Sorteado foi: {maior}')
print(f'O menor valor Sorteado foi: {menor}')
print('='*38) 

