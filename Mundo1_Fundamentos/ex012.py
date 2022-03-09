#faca um algoritimo que leia o preco de um produto e mostre seu
#novo preco, com 5% de desconto

print('--'*30)
print('\033[1m5% DE DESCONTO\033[m')
print('~'*20)
p = float(input('digite o preco do produto: R$'))

d = (5*p)/100
print()
print(f'Com o Desconto De \033[31mR${p:.2f}\033[m Vai Para \033[36mR${p-d:.2f}\033[m')
print('--'*30)
