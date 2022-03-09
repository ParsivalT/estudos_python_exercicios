from random import choice 
from time import sleep

sleep(2)

print('''>>>>>> Digite <<<<<<
(1) Para Pedra
(2) Para Papel
(3) Para Tesoura
-----------------''')


lista = ['Pedra','Papel','Tesoura']
computador = choice(lista)
j = int(input('>>>'))
print('>>>> Start <<<<<')
print('Jo')
sleep(2)
print('Quem')
sleep(2)
print('Po')
sleep(1)

if j == 1:
    j = 'Pedra'
    if j == 'Pedra' and computador == 'Tesoura':
        print(f'''
Voce Ganhou!
------------
Eu Escolhi: {computador}
-----------
Voce Escolheu {j}''')

    elif j == 'Pedra' and computador == 'Papel':
        print(f'''
Voce Perdeu!
------------
Eu Escolhi: {computador}
-----------
Voce Escolheu {j}''')
    
    elif j == 'Pedra' == computador: 
        print(f'''
Empate!
------------
Eu Escolhi: {computador}
-----------
Voce Escolheu {j}''')

elif j == 2:
    j = 'Papel'
    if j == 'Papel' == computador:
        print(f'''
Empate!
------------
Eu Escolhi: {computador}
-----------
Voce Escolheu {j}''')


    elif j == 'Papel' and computador == 'Pedra':
        print(f'''
Voce Ganhou!
------------
Eu Escolhi: {computador}
-----------
Voce Escolheu {j}''')

    else:
        print(f'''
Voce Perdeu!
------------
Eu Escolhi: {computador}
-----------
Voce Escolheu {j}''')

elif j == 3:
    j = 'Tesoura'
    if j == 'Tesoura' == computador:
        print(f'''
Empate!
------------
Eu Escolhi: {computador}
-----------
Voce Escolheu {j}''')

    elif j == 'Tesoura' and computador == 'Pedra':
        print(f'''
Voce Perdeu!
------------
Eu Escolhi: {computador}
-----------
Voce Escolheu {j}''')

    else:
        print(f'''
Voce ganhou!
------------
Eu Escolhi: {computador}
-----------
Voce Escolheu {j}''')

else:
    print(' Erro! Digite Novamente....')

