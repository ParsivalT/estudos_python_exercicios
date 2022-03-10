'''
Desafio 36

problema:  Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
           Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
           A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
           
Resolucao do Problema:
'''
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
