num = int(input('Digite um Numero: '))
u = num // 1 % 10
d = num // 10 % 10 
c = num // 100 % 10
m = num // 1000 % 10
print('Analisando...')
print(f'{u} E Unidade')
print(f'{d} E Dezena ')
print(f'{c} E Centena')
print(f'{m} e Milhar')