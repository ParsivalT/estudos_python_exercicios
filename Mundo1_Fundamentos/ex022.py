print('--'*30)

nome = str(input('Digite Seu Nome Completo: '))
sep = nome.split()
u = ''.join(sep)
print()
print()
print(f'Nome Com Todas as letras minuscula: {nome.lower()}')
print(f'Nome Com Todas Maiusculas: {nome.upper()}')
print(f'O Nome Tem {len(u.strip())} Letras')
print(f'o Primeiro Nome tem {len(sep[0])} Letras')
print('--'*30)
