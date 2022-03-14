'''
Desafio 93

Problema: Crie um programa que gerencie o aproveitamento de um jogador 
          de futebol. O programa vai ler o nome do jogador e quantas partidas
          ele jogou. Depois vai ler a quantidade de gols feitos em cada partida.
          No final, tudo isso será guardado em um dicionário, incluindo o total de 
          gols feitos durante o campeonato.
          
Resolucao do problema:
'''

#definindo as variaveis.
print('=-'*30)
jogadores = {}
gols = []
total = 0
nome = str(input('Nome do jogador: '))
partidas = int(input(f'Quantas partidas {nome} jogou?: '))

#contando a quantidade de gols e coletado os mesmo
for c in range(partidas):
    gols.append(int(input(f'   - Quantos gols na {c+1} partida?: ')))
    total += gols[c]

#colocando os dados coletados dentro do dicionario.
jogadores['nome'] = nome
jogadores['gols'] = gols[:]
jogadores['total'] = total

#exibindo na tela, de maneiras diferente.
print('=-'*30)
print(jogadores)
print('=-'*30)

for k, v in jogadores.items():
    print(f'O campo {k} tem o valor {v}')

print('=-'*30)
print(f'O jogador {nome} jogou {partidas} partidas.')

for pos, valor in enumerate(gols):
    print(f'  -> Na partida {pos+1}, fez {valor} gols.')

print(f'Foi um total de {total} gols.')
print('=-'*30)
