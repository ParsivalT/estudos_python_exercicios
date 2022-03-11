'''
desafio 84

Problema: Faça um programa que leia nome e peso de várias pessoas,
          guardando tudo em uma lista. No final, mostre:

                    A) Quantas pessoas foram cadastradas.
                    B) Uma listagem com as pessoas mais pesadas.
                    C) Uma listagem com as pessoas mais leves.
                    
Resolucao do problema:
'''
#definir as listas globais
dados = list()
pessoa = list()
pesado = leve = 0

#dados digitados pelo usuario
while True:

    print('='*30)
    pessoa.append(str(input('Nome: ')))
    pessoa.append(float(input('Peso: ')))
    dados.append(pessoa[:])

    if len(dados) == 1:
        pesado = leve = pessoa[1]

    if pessoa[1] > pesado:
        pesado = pessoa[1]

    if pessoa[1] < leve:
        leve = pessoa[1]


    pessoa.clear()
    continua = str(input('Deseja continuar? [S/N]: ')).strip().upper()

    while continua not in 'SN': 

        continua = str(input('Deseja continuar? [S/N]: ')).upper().strip()

    if continua == 'N':
        break

print('='*30)
print(f'Existem {len(dados)} pessoas cadastradas!')

print(f'Maior valor registrado: {pesado} que sao de: ', end=' ')

for p in dados:

    if p[1] == pesado:
        print([p[0]], end=' ')

print(f'\nMenor valor registrado: {leve} que sao de: ', end=' ')

for p in dados:
    
    if p[1] == leve:
        print([p[0]], end=' ')
print()
