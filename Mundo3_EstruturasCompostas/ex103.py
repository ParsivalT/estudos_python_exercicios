'''
Desafio 103

Problema: Faça um programa que tenha uma função chamada ficha(), que receba 
          dois parâmetros opcionais: o nome de um jogador e quantos gols ele 
          marcou. O programa deverá ser capaz de mostrar a ficha do jogador, 
          mesmo que algum dado não tenha sido informado corretamente.

Resolucao do problema:          
'''
def ficha(nome, gol):

    dados = {'nome': nome, 'gols': gol}
    return dados


#programa principal
print('-'*30)
nome = str(input('Nome do jogador: '))
gols = str(input('Quantidade de gols: '))

if gols.isnumeric == True:
    gols = int(gols)

else:
    gols = 0

if nome.strip() == '':
    nome = '<desconhecido>'

dados = ficha(nome, gols)

print(f'O jogador {dados["nome"]} marcou {dados["gols"]} gol(s)!')
