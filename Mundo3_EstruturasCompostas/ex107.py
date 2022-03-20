'''
Desafio 107

Problema: Exercício Python 107: Crie um módulo chamado moeda.py que tenha 
          as funções incorporadas aumentar(), diminuir(), dobro() e metade(). 
          Faça também um programa que importe esse módulo e use algumas dessas funções.
          
Resolucao do problema:
'''
import ex107_modulos.moeda


print('='*30)
num = int(input('Digite um Valor: '))
print('-'*30)

print(f'O dobro de R${num} = R${ex107_modulos.moeda.dobro(num)}')
print(f'A metade de R${num} = R${ex107_modulos.moeda.metade(num)}')
print(f'Com um aumento de 10% R${num} passa a ser R${ex107_modulos.moeda.aumenta(num)}')
print(f'Com uma reducao de 10% R${num} passa a ser R${ex107_modulos.moeda.diminui(num)}')
print('='*30)
