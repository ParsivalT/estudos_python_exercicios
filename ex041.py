'''A confederecao nascional de natacao presica de um programa que leia o 
ano de nascimento de um atleta e mostre sua categoria de acordo com a idade

ate 9 anos:MIRIM
ate 14 anos:INFANTIL
ate 19 anos:JUNIOR
ate 20 anos:SENIOR
acima:MASTER'''

from datetime import date
print('-=-'*20)
i = int(input('Digite o Ano De nascimento do Atleta: '))
i = date.today().year - i 
print('~'*30)

print(f'O Atleta Tem {i} Anos ')
if i <= 9:
    print('O Atleta E Mirim')

elif i > 9 and i <= 14:
    print('O Atleta E Infatil')

elif i > 14 and i <=19:
    print('O Atleta E Junior')

elif i > 19 and i <=20:
    print('O Atleta E Senior')

else:
    print('O Atleta E Senior!')
print('-=-'*20)
