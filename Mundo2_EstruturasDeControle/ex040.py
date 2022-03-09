'''Crie um Programa Que leia duas notas de um aluno e calcule sua media. mostrando uma mensagem no
final de acordo com a media atingida!

-Media abaixo de 5.0:
REPROVADO!

-MEdia entre 5.0 e 6.9:

Media 7.0 ou superior: 
APROVADO!
''' 
print('-=-'*20)
n1 = float(input('Digite A primeira nota!: '))
n2 = float(input('Digite A Segunda nota!: '))
m = (n1 + n2)/2
print('~'*30)

print(f'A Media Do Aluno Foi {m}!')
if m >= 7.0:
    print('O Aluno foi \033[36mAPROVADO!\033[m')

elif m >= 5.0 and m <= 6.9:
    print('O Aluno ficou de \033[32mRECUPERACAO!\033[m')

elif m < 5: 
    print('O Aluno foi \033[31mREPROVADO!\033[m')

else:
    print('Numero Digitado \033[31mINVALIDO!\033[m')
print('-=-'*20)
