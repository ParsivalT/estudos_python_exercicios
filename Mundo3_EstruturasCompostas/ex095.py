'''
Desafio 95

Problema: Aprimore o desafio 93 para que ele funcione com vários jogadores, 
          incluindo um sistema de visualização de detalhes do aproveitamento 
          de cada jogador.
          
Resolucao do problema:
'''
print('=-'*30)
jogadores = {}
gols = []
time = []
total = 0

while True:

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
    gols.clear()
    total = 0
    time.append(jogadores.copy())
    continua = str(input('Deseja continuar? [S/N]: ')).upper().strip()

    while True:
        if continua in 'NS':
            break

        print('Erro! digite apenas S ou N!: ')
        continua = str(input('Deseja continuar? [S/N]: ')).upper().strip()

    if continua == 'N':
        break

#exibindo na tela, de maneiras diferente.
print('=-'*30)
print('cod ', end='')

for i in jogadores.keys():
    print(f'{i:<15}', end='')

print()
print('-'*40)

for k, v in enumerate(time):
    print(f'{k:>3} ', end='')

    for d in v.values():
        print(f'{str(d):<15}', end='')
        
    print()

print('-'*40)

while True:
    busca = int(input('Deseja consutar os dados de qual jogador?(999 encerra o program)'))

    if busca == 999:
        break

    if busca > len(time):
        print(f'Erro! nao existe jogador com codigo {busca}')

    else:
        print(f'   -- LEVANTAMENTO do JOGADOR {time[busca]["nome"]}: ')
        for i, g in enumerate(time[busca]["gols"]):
            print(f'   No jogo {i+1} fez {g} gols.')
    