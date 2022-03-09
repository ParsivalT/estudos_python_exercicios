'''crie um programa que faca com que o cumputador escolha um numero
eo exiba na tela '''
from time import sleep 
from random import randint 
print('--'*30)
print('Pensei Num numero Entre 1 e 10 Tente Adivinhar...')
print('--'*30)
nu = randint(1,10)

humano = int(input('Tente Adivinhar: '))
print('PROCESSANDO....')
sleep(2)
if humano == nu:
    print(f'Voce Ganhou, Eu pensei em {nu}')

else:
    print(f'Voce Perdeu, Eu pensei no Numero {nu}')
print('--'*30)

