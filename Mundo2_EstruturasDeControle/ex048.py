'''
Desafio 48

Problema: Faça um programa que calcule a soma entre todos os números 
          que são múltiplos de três e que se encontram no intervalo de 1 até 500.
          
Resolucao do problema:
'''
multiplos = 0

for c in range(0, 501):
    i = c % 2 
    
    if i == 0 and i % 3 == 0:
        multiplos += c 

print(f'A Soma De Todos os numeros e {multiplos}')
