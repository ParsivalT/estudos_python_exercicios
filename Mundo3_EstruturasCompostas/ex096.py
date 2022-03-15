'''
Desafio 96

Problema: Faça um programa que tenha uma função chamada área(), que receba 
          as dimensões de um terreno retangular (largura e comprimento) e mostre 
          a área do terreno
          
Resolucao do problema:
'''
def area(l, c):
    dim = l * c
    return dim


print('=-'*20)
print('  VERIFIQUE O TAMANHO DO SEU TERRENO!')
print('=-'*20)

largura = float(input('Largura do terreno: '))
comprimento = float(input('Comprimento do terreno: '))
print(f'A area do terreno: {area(largura, comprimento)}')   
