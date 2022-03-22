'''
Desafio 111

Problema: Crie um pacote chamado utilidadesCeV que tenha dois módulos 
          internos chamados moeda e dado. Transfira todas as funções utilizadas 
          nos desafios 107, 108 e 109 para o primeiro pacote e mantenha tudo funcionando.


Resolucao do problema:
'''
from UtilidadesCeV.moeda import resumo

preco = float(input('Digite O valor desejado: '))
resumo(preco, 50, 30)
