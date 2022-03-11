'''
Desafio 79

Problema:  Crie um programa onde o usuário possa digitar vários valores 
           numéricos e cadastre-os em uma lista. Caso o número já exista 
           lá dentro, ele não será adicionado. No final, serão exibidos todos 
           os valores únicos digitados, em ordem crescente.
           
Resolucao do problema:
'''
lista = []

while True:

    print('-='*20)
    valor = int(input('Digite um valor: '))

    if valor in lista:
        print('Erro! Digite outro valor')

    else:
        print('Valor adicionado com Sucesso!')
        lista.append(valor)

    continua = str(input('Deseja continuar? [S/N]: ')).upper()
    
    while continua not in 'SN':
        continua = str(input('Deseja continuar? [S/N]: ')).upper()
    
    if continua == 'N':
        break

lista.sort()
print('Valores digitados: ', end='')
print(*lista, sep= ',')
print('-='*20)
