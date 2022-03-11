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

