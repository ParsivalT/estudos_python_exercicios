'''
Desafio 110

Problema: Adicione o módulo moeda.py criado nos desafios anteriores, uma 
          função chamada resumo(), que mostre na tela algumas informações 
          geradas pelas funções que já temos no módulo criado até aqui.


Resolucao do problema:
'''
from moeda import resumo

preco = float(input('Digite O valor desejado: '))
resumo(preco, 50, 30)
