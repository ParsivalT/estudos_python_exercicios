'''
'''
from random import randint
from time import sleep


def sorteia(list):
    
    print('\033[1mSorteando 5 valores: ', end='')
    for c in range(5):
        aleatorio = randint(1,10)
        sleep(0.7)
        print(aleatorio, end=' ', flush=True)
        list.append(aleatorio)
    print(',PRONTO!\033[m')


def somapar(list):

    par = 0
    for valor in list:
        if valor % 2 == 0:
            par += valor

    print(f'\033[1mAo soma todos os valores pares de {list}, temos {par}\033[m')


#programa principal
print('=-'*30)

dados = []

sorteia(dados)
somapar(dados)

print('=-'*30)