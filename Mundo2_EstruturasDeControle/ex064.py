'''
Desafio 64 

Problema: Crie um programa que leia vários números inteiros pelo teclado. 
          O programa só vai parar quando o usuário digitar o valor 999, que 
          é a condição de parada. No final, mostre quantos números foram digitados 
          e qual foi a soma entre eles (desconsiderando o flag).
          
Resolucao do problema: 
'''
print('-=-'*20)
numero = int(input('Digite um numero[999 para o programa]: '))
soma = 0

while numero != 999:

    if numero == 999:
        break

    else:
        soma += numero
        print('--'*10)
        
        numero = int(input('Digite um numero[999 para o programa]: '))

print('-=-'*20)       
print(f'a Soma dos numeros digitados E: {soma}')
print('-=-'*20)
