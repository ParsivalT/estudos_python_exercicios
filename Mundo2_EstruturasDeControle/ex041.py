'''
Desafio 41

Problema:  A Confederação Nacional de Natação precisa de um programa que leia
           o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:

                – Até 9 anos: MIRIM

                – Até 14 anos: INFANTIL

                – Até 19 anos: JÚNIOR

                – Até 25 anos: SÊNIOR

                – Acima de 25 anos: MASTER
                
Resolucao do problema:
'''

from datetime import date   #para pegar a data atual!

print('-=-'*20)
i = int(input('Digite o Ano De nascimento do Atleta: '))
i = date.today().year - i   #pego o ano atual e subtraio pelo (ano de nascimento)
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
