#um professor quer escolher um de seus 4 alunos para apagar o quadro
#desemvolva um programa que leia o nome dos 4 e sortei um 

from random import choice
print('--'*30)
n1 = input('Digite o Primeiro Nome: ')
n2 = input('Digite o Segundo Nome: ')
n3 = input('Digite o Terceiro Nome: ')
n4 = input('Digite o Quarto Nome: ')

nomes = [n1, n2, n3, n4]
es = choice(nomes)
print('--'*30)
print(f'O Aluno(a) Escolhido Foi O(a) {es}')
print('--'*30)

