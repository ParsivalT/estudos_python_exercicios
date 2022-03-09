#desemvolva um programa que leia as duas notas de um aluno, calcule e mostre sua media

print('-=-'*10)
nota1 = float(input('digite a \033[4mprimeira\033[m nota: '))
nota2 = float(input('digite a \033[4msegunda\033[m  nota: '))
print('~'*30)
m = (nota1 + nota2) / 2 

if m <= 6:
    print('\033[31mO Aluno Repetiu De Ano\033[m')
    print(f'A media do Aluno foi: \033[31m{m:.1f}\033[m')

else:
    print('O Aluno Passou de Ano')
    print(f'A media do Aluno foi: \033[36m{m:.1f}\033[m')
print('-=-'*10)
