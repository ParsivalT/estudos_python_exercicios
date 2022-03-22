'''
Desafio 112

Problema: Dentro do pacote utilidadesCeV que criamos no desafio 111, 
          temos um módulo chamado dado. Crie uma função chamada leiaDinheiro() 
          que seja capaz de funcionar como a função imputa(), mas com uma validação 
          de dados para aceitar apenas valores que seja monetários.
          

Resolucao do problema:
'''
from UtilidadesCeV.moeda import resumo
from UtilidadesCeV.dados import leiaDinheiro

preco = leiaDinheiro('Digite o valor: ')
resumo(preco, 50, 30)
