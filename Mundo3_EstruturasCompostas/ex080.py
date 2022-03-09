#Ordenar uma lista sem o sort!
# for: Thiago 06/03/2022

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