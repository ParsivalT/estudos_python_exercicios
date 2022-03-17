"""
Desafio 104

Problema: Crie um programa que tenha a função leiaInt(), que vai funcionar 
          de forma semelhante ‘a função input() do Python, só que fazendo a 
          validação para aceitar apenas um valor numérico. Ex: 
          
                n = leiaInt(‘Digite um n: ‘)

Resolucao do problema:          
"""
def leiaInt(num):

    numero = input(num)
    while True:

        print('='*30)
        if  numero.isnumeric() == True and numero != float:
            break

        else:

            print('\033[31mErro! digite um numero inteiro!\033[m')
            numero = input(num)

    return numero


#programa principal
print('-'*30)
num = leiaInt('Digite um numero inteiro: ')
print(f'Voce digitou {num}')
