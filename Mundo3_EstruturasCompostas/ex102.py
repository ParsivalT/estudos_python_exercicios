'''
Desafio 102 

Problema: Crie um programa que tenha uma função fatorial() que receba 
          dois parâmetros: o primeiro que indique o número a calcular 
          e outro chamado show, que será um valor lógico (opcional) indicando 
          se será mostrado ou não na tela o processo de cálculo do fatorial.

Resolucao do problema:
'''
def fatorial(num, show=False):

    if show == False:

        c = num
        fatorial = 1

        while c > 0:

            fatorial *= c
            c -= 1

        return fatorial

    else: 

        c = num
        fatorial = 1

        while c > 1:
            
            fatorial *= c
            c -= 1
            print(c, end='')
            print(' x ' if c > 1 else ' = ', end='')

        print(fatorial)
    

print('-'*30)
fatorial(6, show=True)
