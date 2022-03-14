'''
Desafio 38

Problema: Crie um programa que leia nome, ano de nascimento e carteira 
          de trabalho e cadastre-o (com idade) em um dicionário. Se por 
          acaso a CTPS for diferente de ZERO, o dicionário receberá também 
          o ano de contratação e o salário. Calcule e acrescente, além da idade, 
          com quantos anos a pessoa vai se aposentar.
          
Resolucao do Problema:
'''
from datetime  import date 

dados = {}

print('=='*30)
dados['nome'] = str(input('Digite o nome: ')).title()
dados['idade'] = date.today().year - int(input('Digite a data de nascimento: ')) 
dados['ctps'] = int(input('Carteira de trabalho(caso nao tenha digite 0): '))

if dados['ctps'] != 0:
    dados['ano_contratacao'] = int(input('Digite o ano da Contratacao: '))
    dados['salario'] = float(input('Salario: '))
    dados['aposentadoria'] = ((dados['ano_contratacao']+35)-date.today().year)+dados['idade']

print('=='*30)
for k, v in dados.items():
    print(f'  - {k} do trabalhador: {v}')
