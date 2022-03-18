'''
Desafio 106

Problema: Faça um mini-sistema que utilize o Interactive Help do Python. 
          O usuário vai digitar o comando e o manual vai aparecer. Quando 
          o usuário digitar a palavra ‘FIM’, o programa se encerrará. Importante: 
            
            use cores.

            Aula Anterior

Resolucao do problema:      
'''
cores = ('\033[m',         # 0 -- Sem cor
         '\033[30;42m',    # 1 -- Verde
         '\033[31m',       # 2 -- Vermelho
         '\033[30;44m',    # 3 -- Roxo
        );

def ajuda(txt):

    print(cores[3], end='')
    help(txt)
    print(cores[0])

def cor(msg, cor=0):

    tamanho = len(msg) + 4
    print(cores[cor],end='')
    print('='* tamanho)
    print(f' {msg}')
    print('='*tamanho)
    print(cores[0],end='')


#programa principal
comando = ''

while True:

    cor('SISTEMA DE AJUDA PyHELP', 1)
    comando = str(input('Funcao ou Biblioteca >>> '))

    if comando.upper().strip() == 'FIM':
        break

    else:
        cor(f'Pesquisando o Comando {comando}', )
        ajuda(comando)
