'''
Desafio 73

Problema:  73: Crie uma tupla preenchida com os 20 primeiros colocados 
           da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. 
           Depois mostre:

                a) Os 5 primeiros times.

                b) Os últimos 4 colocados.

                c) Times em ordem alfabética.

                d) Em que posição está o time da Chapecoense.
                
Resolucao do problema: 
'''
times = ('America-MG', 'Athletico-PR', 'Atletico-GO', 'Atletico-MG',
         'Avai', 'Botafogo', 'Ceara SC', 'Corinthias', 'Coritiba',
         'Cuiaba', 'Flamengo', 'Fluminense', 'Fortaleza', 'Goias',
         'Internacional', 'Juventude', 'Palmeiras', 'Bragantino', 
         'Santos', 'Sao Paulo')

print('='*46)
print(f'Os 5 primeiros Sao: {times[:5]}')
print('='*46)
print(f'Os ultimos 4 colocados Sao: {times[-5:-1]}')
print('='*46)
print(f'Em ordem alfabetica: {sorted(times)}')
print('='*46)
print('O Avai esta na posicao {}'.format(times.index('Avai')))
print('='*46)
