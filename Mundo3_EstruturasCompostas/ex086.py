'''
Desafio 086

Problema: Crie um programa que crie uma matriz 3x3 e preecha com valores lidos
          pelo teclado.
          no final, mostre a matriz na tela, com a formatacao correta
          
Resolucao do problema: 
'''
matriz = [[],[],[]]

#Alimentando a lista com valores.
for coluna in range(0, 3):

    for linha in range(0,3):
        matriz[coluna].append(int(input(f'Digite o valor para a posicao [{coluna},{linha}]: ')))

print('='*30)

#Exibindo a mensagem no console.
for coluna in range(0,3):

    for linha in range(0,3):
        print(f'[ {matriz[coluna][linha]:6^} ]', end=' ')

    print()    
