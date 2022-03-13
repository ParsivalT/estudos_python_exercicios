'''
Desafio 90

Problema: Faça um programa que leia nome e média de um aluno, guardando 
          também a situação em um dicionário. No final, mostre o conteúdo 
          da estrutura na tela.
          
Resolucao do problema:
'''
aluno = {}

print('='*33)
aluno['nome'] = str(input('Nome do Aluno(a): '))
aluno['media'] = float(input('Media: '))

if aluno['media'] >= 7:
    aluno['estado'] = '\033[36mAprovado\033[m'

elif aluno['media'] >= 5 and aluno['media'] < 7:
    aluno['estado'] = '\033[32mRecuperacao\033[m'

else:
    aluno['estado'] = '\033[31mReprovado\033[m'

print('='*33)
for k, v in aluno.items():
    print(f'- {k} do aluno: {v}')
print('='*33)
