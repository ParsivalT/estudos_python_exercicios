'''
Desafio 77

Problema:'''
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
