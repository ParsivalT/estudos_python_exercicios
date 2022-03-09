#crie um algoritimo que leia o salario de um funcionario e mostre
#seu novo salario com 15% de almento

print('--'*30)
s = float(input('digite o valor do salario atual R$'))

a = (15*s)/100
print()
print(f'O valor de \033[32mR${s:.2f}\033[m com um almento de \033[36m15%\033[m E de \033[36mR${s+a:.2f}\033[m')
print('--'*30)
