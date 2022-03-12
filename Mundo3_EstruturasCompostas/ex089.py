'''
Desafio 89

Problema: Crie um programa que leia nome e duas notas de vários alunos 
          e guarde tudo em uma lista composta. No final, mostre um boletim 
          contendo a média de cada um e permita que o usuário possa mostrar 
          as notas de cada aluno individualmente.
          
Resolucao do problema:
'''
banco_dados = []
aluno = []

while True:

    print('='*30)
    aluno.append(str(input('Nome: ')))
    aluno.append(float(input('Nota 1: ')))
    aluno.append(float(input('Nota 2: ')))

    banco_dados.append(aluno[:])
    aluno.clear()

    continua = str(input('Deseja continuar? [S/N]: ')).strip().upper()

    while continua not in 'SN':
        continua = str(input('Deseja continuar? [S/N]: ')).strip().upper()

    if continua == 'N':
        break

print('='*63)
print('\t\t\t Estatisticas')
print('='*63)

for c in range(len(banco_dados)):

    for i in range(len(banco_dados[c])):

        print(f'{c}  {banco_dados[c][0]:<18}|', end='.'*20)
        print(f'|Media do Aluno(a): {(banco_dados[c][1] + banco_dados[c][2])/2}')

        break

while True: 

    print('='*63)
    dados = int(input('Deseja acessar os dados de qual aluno?(999 encerra o programa!): '))

    if dados == 999:
        break

    else:
        print(f'\nO Aluno(a): {banco_dados[dados][0]} Tirou as notas: {banco_dados[dados][1], banco_dados[dados][2]}')
        