from random import randint

computador = randint(1,11)
jogador = ''
pontos = 0
escolha = ''

while True:
    
    print('-=-'*20)
    escolha = str(input('Impar ou Par [I/P]: '))[0].upper().title()
    jogador = int(input('Digite um numero: '))
    
    if (computador + jogador)% 2 == 0:
       
        print(f'Jogador: {jogador} computador {computador} tem como resultado {jogador + computador} deu PAR')
        
        if escolha == 'P':
        
            print('\033[36mVoce Ganhou\033[m')  
            pontos += 1 

        else:

            print('\033[31mVoce Perdeu, Tente outra vez....\033[m')
            break
    
    elif (computador + jogador)% 2 == 1:

        print(f'Jogador: {jogador} computador: {computador} tem como resultado {jogador + computador} deu IMPAR')

        if escolha == 'I':

            print('\033[36mVoce Ganhou\033[m')
            pontos += 1

        else:

            print('--'*20)
            print('\033[31mVoce Perdeu, Tente outra vez....\033[m')
            break

print(f'\033[36mVitorias consecultivas: {pontos}\033[m')
