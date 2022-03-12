'''
Desafio 87

Problema: Aprimore o desafio anterior, mostrando no final:

            A) A soma de todos os valores pares digitados.
            B) A soma dos valores da terceira coluna.
            C) O maior valor da segunda linha.
            
Resolucao do problema:
'''
matriz = [[],[],[]]
pares = []
soma = soma_coluna = maior_linha = 0 

#Alimentando a lista com valores.
for coluna in range(0, 3):

    for linha in range(0,3):
        matriz[coluna].append(int(input(f'Digite o valor para a posicao [{coluna},{linha}]: ')))

soma_coluna = matriz[0][2] + matriz[1][2] + matriz[2][2]

print('=='*30)

#somando os valores pares 
for coluna in range(0, 3):
    for linha in range(0,3):

        if matriz[coluna][linha] % 2 == 0:
            soma += matriz[coluna][linha]
 
#Exibindo os valores no console.
for coluna in range(0,3):

    for linha in range(0,3):
        print(f'[ {matriz[coluna][linha]:7^} ]', end=' ')

    print()    

print('=='*30)
print(f'A soma de todos os valores PARES digitado foi: {soma}')
print(f'A Soma de todos os valores da Terceira coluna foi: {soma_coluna}')
print(f'O Maior valor encontrado na segunda coluna foi: {max(matriz[1])}')
print('=='*30)
