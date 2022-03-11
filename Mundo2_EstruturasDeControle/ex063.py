'''
Desafio 63

Problema: Escreva um programa que leia um número N inteiro qualquer e 
          mostre na tela os N primeiros elementos de uma Sequência de Fibonacci.
          Exemplo:

                0 – 1 – 1 – 2 – 3 – 5 – 8
                
Resolucao do problema:
'''
print('=='*20)
print('Sequencia de Fibonacci!')

numero = int(input('Quantos termos voce deseja mostrar?: '))
t1 = 0
t2 = 1

print(f'Sequencia: {t1} -> {t2}', end=' -> ')

while numero > 0:

    t3 = t1 + t2
    t1 = t2
    t2 = t3
    numero -= 1

    print(f'{t3}', end =' -> ')
    
print('FIM\n')
print('=='*20)
