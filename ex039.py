'''Faca Um Programa que leia a idade de um jovem e iforme. de acordo com sua idade 
se ele ainda vai se alistar ao servico militar, se ea hora de se alistar. 
se ja passou do tempo do alistamento.

seu programa deve tambem mostrar o tempo que falta ou que passou do prazo!'''

from datetime import date #importei a biblioteca datetime para me auxiliar e para conseguir a data atual!

print('-=-'*20)
i = int(input('Digite A Sua data de nascimento: '))
print('~'*30)

a = date.today().year - i

if a == 18: 
    print('\033[36mVoce Tem 18 Anos Logo!')
    print('Voce Ja Tem Idade Para Ingrassar Ao Servico Militar!\033[m')

elif a > 18: 
    print(f'\033[31mVoce Deveria Ter Se Alistado A {a-18} Anos Atras!\033[m')

else:
    print(f'Ainda Falta {(a-18)* -1} Ano Para voce ingressar Ao servico militar!')
print('-=-'*20)
