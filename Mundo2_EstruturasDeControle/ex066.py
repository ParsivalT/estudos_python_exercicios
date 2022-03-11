'''
Desafio 66

Problema: Crie um programa que leia números inteiros pelo teclado. 
          O programa só vai parar quando o usuário digitar o valor 999, 
          que é a condição de parada. No final, mostre quantos números foram 
          digitados e qual foi a soma entre elas (desconsiderando o flag).
          
Resolucao do problema: 
'''
numero = total = cont = 0 

while True:
    
    numero = int(input('Digite os numeros(Digite 999 para sair): '))

    if numero != 999:
        total += numero
        cont += 1
    
    if numero == 999:
        break

print('=='*20)
print(f'A soma dos {cont} valores digitados foi: {total}')
print('=='*20)
