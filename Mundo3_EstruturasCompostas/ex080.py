'''
Desafio 80

Problema:  Crie um programa onde o usuário possa digitar cinco valores 
           numéricos e cadastre-os em uma lista, já na posição correta 
           de inserção (sem usar o sort()). No final, mostre a lista ordenada 
           na tela.
           
Resolucao do problema:
'''
lista = []
lista1 = []

for c in range(6):
    valor = int(input('Digite o valor desejado: '))

    if c == 0 or valor > lista[-1]:
        lista.append(valor)
        print('Valor adicionado ao final da lista!')
        
    if valor < lista[0]:
        lista.insert(0, valor)
    
    pos = 0 

    while pos < len(lista):

        if valor < lista[pos]:
            lista.insert(pos, valor)
            print(f'Valor adicionado a posicao: {pos}')
            break    

        pos += 1

print(f'\nResultado {lista}')
