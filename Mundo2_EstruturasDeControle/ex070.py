'''
Desafio 70

Problema: Crie um programa que leia o nome e o preço de vários produtos. 
          O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:

                A) qual é o total gasto na compra.

                B) quantos produtos custam mais de R$1000.

                C) qual é o nome do produto mais barato.
                
Resolucao do problema:
'''
from os import system

print('-=-'*20)
print(''' >>>>>>>>>>> \033[1mBem Vindo A Quitanda Do Seu Joao!\033[m <<<<<<<<<<<''')
print('-=-'*20)

produtos = []
preco = []
total = mil = 0

while True:
    
    print('--'*26)
    produtos.append(str(input('\nNome Do Produto: ')))
    preco.append(float(input('Preco: ')))
    print('--'*26)
    continua = str(input('Deseja continuar? [S/N]: ')).upper()

    if continua == 'N':
        break

#system('clear')
print('--'*26)
print('\033[31mCAIXA ENCERRADO!\033[m')

for c in range(len(preco)):
    total += preco[c]

    if preco[c] > 1000:
        mil += 1

menor = min(preco) # vejo qual o menor iten da lista usando o metodo min()
x = preco.index(menor) #pego a posicao do menor iten usando o idex()

print(f'\nTotal da Compra: R${total:.2f})\nO produto mais barato foi: \033[1m{produtos[x]}\033[m Custando: \033[36mR${menor:.2f}\033[m')

if mil == 1:
    print('Apenas 1 produto custou mais de R$1000,00')

else:
    print(f'{mil} Produtos valem mais de R$1000,00')

print('--'*26)
print('ITENS COMPRADOS:')

for c in range(len(produtos)):
    print(f'\n{produtos[c]}: {preco[c]:.2f}')
    
print('--'*26)
