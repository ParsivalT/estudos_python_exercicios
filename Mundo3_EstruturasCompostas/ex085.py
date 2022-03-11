'''
Desafio 85

Problema: Crie um programa onde o usuário possa digitar sete valores numéricos e 
          cadastre-os em uma lista única que mantenha separados os valores pares e 
          ímpares. No final, mostre os valores pares e ímpares em ordem crescente.
          
Resolucao do problema:
'''
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
