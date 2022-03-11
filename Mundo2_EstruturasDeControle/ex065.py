'''
Desafio 65

Problema: Crie um programa que leia vários números inteiros pelo teclado. 
          No final da execução, mostre a média entre todos os valores e qual 
          foi o maior e o menor valores lidos. O programa deve perguntar ao usuário 
          se ele quer ou não continuar a digitar valores.
          
Resolucao do problema: 
'''
from os import system 

numero = cont = maior = menor = total =  0 

while True:print(maior, menor ) #testeprint(maior, menor ) #testeprint(maior, menor ) #teste
    
    system('clear')
    print('='*20)

    cont += 1
    numero = int(input('Digite um numero: '))
    continuar = str(input('Deseja Continuar? [S/N]: ')).upper()
    total += numero
    
    if cont == 1:
        maior = numero
        menor = numero 

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

system('clear')
print('=='*24)
print(f'\033[1mA media dos valores digitado E: {total/cont:.1f}')
print(f'O maior numero digitado foi {maior} ja o menor foi: {menor}\033[m')
print('=='*24)