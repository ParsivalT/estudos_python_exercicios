'''
Desafio 109

Problema: Modifique as funções que form criadas no desafio 107 para que 
          elas aceitem um parâmetro a mais, informando se o valor retornado 
          por elas vai ser ou não formatado pela função moeda(), desenvolvida 
          no desafio 108.
          
Resolucao do problema:
'''
import moeda


print('='*30)
num = float(input('Digite um Valor: '))
print('-'*30)

print(f'O dobro de R${moeda.moeda(num)} = {moeda.dobro(num, True)}')
print(f'A metade de R${moeda.moeda(num)} = {moeda.metade(num, True)}')
print(f'Com um aumento de 10% {moeda.moeda(num)} passa a ser {moeda.aumenta(num, 10, True)}')
print(f'Com uma reducao de 10% {moeda.moeda(num)} passa a ser {moeda.diminui(num, 10, True)}')
print('='*30)
