#escreva um programa para aprovar um emprestimo bancario para comprar uma casa.
#o programa vai perguntar o valor da casa. o salario do comprador e em quatos anos  ele vai pagar.
# o valor das prestacoes nao pode exeder 30% do salario 

print('-=-'*20)
casa = float(input('Digite O Valor Do Emprestimo: R$'))
s = float(input('Digite O Salario Do comprador: R$'))
a = int(input('Em quantos Anos Pretende Pagar?: '))
print('~'*30)
v = casa / (a*12)
sa = s * 30 / 100

if v > sa: 
    print('\033[31mEmprestimo NEGADO!\033[m') 
    print(f'Para Um Emprestimo De R${casa} O Valor  Mensal A Ser Pago E De \033[31mR${v:.2f}\033[m!')
else:
    print('\033[36mEmprestimo Aprovado!\033[m')
    print(f'Para Um Emprestimo De R${casa} O Valor Mensal A Ser Pago E De \033[36mR${v:.2f}\033[m')
print('~'*30)
