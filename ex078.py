'''Armazena 5 valores dentro de uma lista, logo em seguida mostra qual o maior e qual o menor
e as suas respectivas posicoes '''

lista = []
pos_maior = []
pos_min = []
mini = maxi = pos = 0

for c in range(1, 6):
    valor = int(input('Digite um numero: '))
    lista.append(valor)
    if c == 1:
        mini=  maxi = valor

    if valor < mini:
        mini = valor

    if valor > maxi:
        maxi = valor

for pos, valor in enumerate(lista):
    if valor == maxi:
        pos_maior.append(pos)
    
    if valor == mini:
        pos_min.append(pos)
print()
print(*lista, sep=',')

print('O maior valor digitado foi:', end= ' ')
for i in range(len(lista)):
    if lista[i] == maxi:
        print(lista[i], end='...')
print(f' Nas posicoes {pos_maior[:]}')

print('O menor valor digitado foi: ', end=' ')
for i in range(len(lista)):
    if lista[i] == mini:
        print(lista[i], end='...')
print(f' Nas posicoes {pos_min[:]}')

