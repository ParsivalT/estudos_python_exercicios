#Faca um programa que leia um numero e diga se o ano e ou nao bixessexto!

from datetime import date

ano = int(input('Digite o ano Que deseija analisar! Para analisar o ano Atual digite 0!: '))

if ano == 0:
    ano = date.today().year

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O Ano {ano} e BIXESSETO!')

else:
    print(f'O Ano {ano} Nao e BIXESSETO!')
