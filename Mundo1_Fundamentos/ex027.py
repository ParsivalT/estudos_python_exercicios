#crie um programa que diga o primeiro eo ultimo nome da pessoa

nome = str(input('Digite O Seu nome Completo: ')).strip()
print('Analizando...')
print('--'*30)
nome = nome.title().split()
print(f'Seu Primeiro Nome E: {nome[0]}')
print(f'Seu Ultimo Nome E: {nome[-1]}')
print('--'*30)
