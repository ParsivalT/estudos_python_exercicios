'''
Desafio 39

Problema: Faça um programa que leia o ano de nascimento de um jovem e informe, 
          de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, 
          se é a hora exata de se alistar ou se já passou do tempo do alistamento. 
          Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

Resolucao do problema:
'''
from datetime import date #importei a biblioteca datetime para me auxiliar e para conseguir a data atual!

print('-=-'*10)
data_nascimento = int(input('Digite o ano em que voce nasceu: '))
print('~'*30)

a = date.today().year - data_nascimento

if a == 18: 
    print('\033[36mVoce Tem 18 Anos Logo!')
    print('Voce Ja Tem Idade Para Ingrassar Ao Servico Militar!\033[m')

elif a > 18: 
    print(f'\033[31mVoce Deveria Ter Se Alistado A {a-18} Anos Atras!\033[m')

else:
    print(f'Ainda Falta {(a-18)* -1} Ano Para voce ingressar Ao servico militar!')
print('-=-'*10)
