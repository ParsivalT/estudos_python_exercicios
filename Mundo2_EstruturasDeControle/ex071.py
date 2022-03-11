'''
Desafio 71

Problema: Crie um programa que simule o funcionamento de um caixa eletrônico. 
          No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) 
          e o programa vai informar quantas cédulas de cada valor serão entregues. 
          
          OBS:
              considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
              
Resolucao do problema:
'''
print('='*34)
print('\t BANCO RACHADINHA')
print('='*34)

n50 = n20 = n10 = n1 = caixa = 0  #defino as variaveis  
valor = int(input('Qual o Valor do Saque?: R$'))  
caixa = valor 

while True:
    
    if caixa >= 50:
        caixa -= 50 
        n50 += 1

    elif caixa >= 20:
        caixa -= 20
        n20 += 1

    elif caixa >= 10:
        caixa -= 10
        n10 += 1

    elif caixa >= 1:
        caixa -= 1
        n1 += 1 

    else:
        break

if n50 > 0:
    print(f'Total de {n50} cedulas de R$50')

if n20 > 0: 
    print(f'Total de {n20} cedulas de R$20')

if n10 > 0:
    print(f'Total de {n10} cedulas de R$10')

if n1 > 0:
    print(f'Total de {n1} cedulas de R$1')

print('='*34)
