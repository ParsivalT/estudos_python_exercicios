"""
Desafio 114


Problema: Reescreva a função leiaInt() que fizemos no desafio 104, 
          incluindo agora a possibilidade da digitação de um número 
          de tipo inválido. Aproveite e crie também uma função leiaFloat() 
          com a mesma funcionalidade.
          

Resolucao do problema:
"""
def leiaInt(valor):

    while True:
        try:
            numero = int(input(valor))

        except (ValueError, TypeError):
            print('\033[31mErro! Digite um valor INTEIRO valido\033[m')
            continue

        except KeyboardInterrupt:
            print('\033[31m\nO usuario preferiu nao digitar esse valor!\033[m')
            return 0

        else:
            return numero


def leiaFloat(valor):

    while True:
        try:
            numero = float(input(valor))

        except (ValueError, TypeError):
            print('\033[31mErro! Digite um valor REAL valido\033[m')
            continue

        except KeyboardInterrupt:
            print('\033[31m\nO usuario preferiu nao digitar esse valor!\033[m')
            return 0

        else:
            return numero
            

inteiro = leiaInt('Digite um Valor Inteiro: ')
real = leiaFloat('Digite um valor Real: ')
print(f'Valor inteiro digitado: {inteiro}, valor real: {real}')
