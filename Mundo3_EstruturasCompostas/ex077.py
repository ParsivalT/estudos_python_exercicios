'''
Desafio 77

Problema:  Crie um programa que tenha uma tupla com várias palavras (não usar acentos). 
           Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
           
Resolucao do problema:
'''
palavras = ('python', 'caxinha', 'agenda', 'pokemon', 'avenida')
vogais = ('a', 'e', 'i', 'o', 'u')
palavra = ''

for c in range(len(palavras)):
    palavra = palavras[c]
    print(f'Dentro da palavra: \033[1m{palavras[c].upper()}\033[m tem as vogais: ', end=' ')

    for i in range(len(vogais)):

        if vogais[i] in palavra:
            print(f'\033[1m{vogais[i]:}\033[m',end=' ')
        
    print()
print()
