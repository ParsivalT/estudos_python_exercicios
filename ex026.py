frase = str(input('Digite Algo: ')).strip()
q_letras = frase.upper().count('A')
p_letra = frase.upper().find('A') + 1
u_letra = frase.upper().rfind('A') + 1
print('Analizando..')
print('--'*30)
print(f'Dentro da frase existem {q_letras} Letras A')
print(f'A primeira Letra se encontra na posicao {p_letra}')
print(f'A Ultima Letra se encontra na posicao {u_letra}')
print('--'*30)
