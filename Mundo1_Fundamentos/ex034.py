salario = float(input('Digite O Seu Salario!: R$'))
if salario <= 1250.00: 
    aumento = salario * 15 / 100
    print(f'O Salario de R${salario:.2f} Com um aumento de 15% Passara A ser R${salario + aumento:.2f}')

else:
    aumento = salario * 10 / 100
    print(f'O Salario de R${salario:.2f} Com um aumento de 10% Passara A ser R${salario + aumento:.2f}')

 