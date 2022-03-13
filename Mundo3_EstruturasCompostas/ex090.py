'''
Desafio 90

Problema: Faça um programa que leia nome e média de um aluno, guardando 
          também a situação em um dicionário. No final, mostre o conteúdo 
          da estrutura na tela.
          
Resolucao do problema:
'''
aluno = {}

print('='*33)
aluno['nome'] = str(input('Nome do Aluno: '))
aluno['media'] = float(input('Media: '))
print('='*33)

print(aluno)
print(f'\nO aluno: {aluno["nome"]} tem como media: {aluno["media"]}')
print('='*33)
