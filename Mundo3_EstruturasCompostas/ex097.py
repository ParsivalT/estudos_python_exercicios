'''
Desafio 97 

Problema:  Faça um programa que tenha uma função chamada escreva(), 
           que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.                                  
           Ex:                                                                                                                                                                        
           escreva("Olá, Mundo!") Saída:
           ~~~~~~~~~~~                                                                       
           Olá, Mundo!
           ~~~~~~~~~~~

Resolucao do problema: 
'''
def escreva(txt):

    com = len(txt) + 4

    print('='*com)
    print(f'  {txt}')
    print('='*com)


escreva('Bem vindos!')
escreva('I love Python!')
escreva('Hello, word!')
