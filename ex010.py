#5,53
#crie um programa que leia quanto dinheiro uma pessoa tem e mostre quantos dolare ela pode comprar 
print('-=-'*20)
v = float(input('digite um valor: R$'))
print('~'*58)
d = 5.53
s = v / d 

print(f'Com: \033[36:4mR${v:.2f}\033[m voce consegue comprar \033[32:4m${s:.2f}\033[m')
print('-=-'*20)
