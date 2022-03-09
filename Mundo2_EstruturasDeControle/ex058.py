#jogo de adivinhar o numero de 1 a 10 que foi escolhido peloo programa!

from random import randint
from time import sleep 

n = randint(1,10)  
# aqui ele escolhe o numero
p = 0 
#aqui ele marca/conta o numero de tentativas feitas pelo jogador 
j = 0
#aqui e guardado o numero que o jogador digita!

print('-=-'*20)
print('-----Vou Pensar num Numero de 1 a 10 -----')
print()
sleep(2)
print('Pensando..')
print()
sleep(2)
print('Pensando...')
print()
print('Pronto, Agora tente Adivinhar!')

while j != n:
    j = int(input('Qual Numero Voce Acha Que eu Pensei?: '))
    if j != n:
        p += 1 
        print('>>>>>>> \033[31mTente de Novo!\033[m <<<<<<<<')
    print('--'*30)

print(f'''>>>>>>>  \033[36mVoce Acertou!\033[m <<<<<<<<
numero que eu escolhi foi: {n}
numero de vezes que voce tentou: {p}''')


