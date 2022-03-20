'''
Desafio 108

Problema: Adapte o código do desafio #107, criando uma função adicional 
          chamada moeda() que consiga mostrar os números como um valor monetário 
          formatado.
          
Resolucao do problema:
'''
import moeda


print('='*30)
num = float(input('Digite um Valor: '))
print('-'*30)

print(f'O dobro de R${moeda.moeda(num)} = {moeda.moeda(moeda.dobro(num))}')
print(f'A metade de R${moeda.moeda(num)} = {moeda.moeda(moeda.metade(num))}')
print(f'Com um aumento de 10% {moeda.moeda(num)} passa a ser {moeda.moeda(moeda.aumenta(num))}')
print(f'Com uma reducao de 10% {moeda.moeda(num)} passa a ser {moeda.moeda(moeda.diminui(num))}')
print('='*30)
