print('-='*30)
print('>>>>>>>> 10 Termos de uma PA <<<<<<<<')
print('~'*20)
a1 = int(input('Primeiro Termo: '))
razao = int(input('digite A Razao: '))

ac = 0
for c in range(0,10):
   ac = a1 + razao * c
   print(f'{ac}', end = ' - ')    


