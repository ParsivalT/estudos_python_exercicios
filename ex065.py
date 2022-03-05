# soma todos os valores digitados, e mostra a media, maior e menor valor digitado!
from os import system 

numero = cont = maior = menor = total =  0 
continuar = ''

while True:
    
    print('-=-'*10)

    system('clear')
    cont += 1
    numero = int(input('Digite um numero: '))
    continuar = str(input('Deseja Continuar? [S/N]: ')).upper()
    total += numero
    
    if cont == 1:

        maior = numero
        menor = numero 
        print(maior, menor ) #teste

    if numero > maior:

        maior = numero

    if numero < menor:

        menor = numero

    while continuar not in 'SN':
        
        system('clear')
        print('**'*10)

        print('Por favor Digite uma opcao valida!')
        continuar = str(input('Deseja Continuar? [S/N]: ')).upper()
        

    if continuar == 'N':
        break
print(f'\033[1mA media dos valores digitado E: {total/cont:.1f}')
print(f'O maior numero digitado foi {maior} ja o menor foi: {menor}\033[m')