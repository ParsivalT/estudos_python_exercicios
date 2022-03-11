'''
Desafio 53

Problema:  Crie um programa que leia uma frase qualquer e diga se ela 
           é um palíndromo, desconsiderando os espaços. Exemplos de palíndromos:

                    APOS A SOPA, 
                    A SACADA DA CASA, 
                    A TORRE DA DERROTA, 
                    O LOBO AMA O BOLO, 
                    ANOTARAM A DATA DA MARATONA.

Resolucao do problema:                 
'''
f = str(input('Digite A Frase: ')).upper().split()
f = ''.join(f)
i = f[::-1]

print(f'A Frase \33[36m{f}\033[m Ao Contrario Fica \033[31m{i}\033[m, tem Um Total De {len(f)} letras ')

if f == i:
    print('E um Palindromo!')

else:
    print('Nao E um Palindromo')
