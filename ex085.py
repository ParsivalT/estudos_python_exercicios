#For Thiago 08/03/2022
#Algoritimo que recebe varios valores diferentes e guarda em uma lista.
#logo em seguida mostra os mesmo separados entre IMPAR e PAR.


lista = [[],[],[]]

while True: 

    print('='*30)
    lista[0].append(int(input('Digite o Valor desejado: ')))
    continua = str(input('Deseja continuar? [S/N]: ')).upper().strip()
    
    if lista[0][-1] % 2 == 0:
        lista[1].append(lista[0][-1])

    if lista[0][-1] % 2 == 1:
        lista[2].append(lista[0][-1])


    while continua not in 'NS':

        continua = str(input('Deseja continuar? [S/N]: ')).upper().strip()

    if continua == 'N':
        break
print('='*30)
print(f'Valores digitados!: {lista[0]}')
print(f'Valores Pares: {lista[1]}')
print(f'Valores Impares: {lista[2]}')
print('='*30)
