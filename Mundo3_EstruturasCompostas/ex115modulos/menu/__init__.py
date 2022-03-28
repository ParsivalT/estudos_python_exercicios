'''
Modulo com  as fucoes do exercicio 115
'''
from time import sleep
from ex115modulos.manipulacao_arquivos import *
from os import system


cores = {'sem cor':'\033[m',
         'vermelho':'\033[31m',
         'verde':'\033[32m',
         'azul':'\033[36m'}

def leiaInt(valor):

    while True:
        try:
            numero = int(input(valor))

        except (ValueError, TypeError):
            print(f'{cores["vermelho"]}Erro! Digite um valor INTEIRO valido{cores["sem cor"]}')
            continue

        except KeyboardInterrupt:
            print('O usuario preferiu nao digitar esse valor!')
            return 0

        else:
            return numero


def menu(sistema=False):
    
    sistema_ligado = sistema
    while sistema_ligado:

        print('='*40)
        print(f'{"CADASTRO DE PESSOAS":^40}')
        print('='*40)

        print(f'{cores["verde"]}1{cores["sem cor"]} -- {cores["azul"]}Ver pessoas cadastradas{cores["sem cor"]}') 
        print(f'{cores["verde"]}2{cores["sem cor"]} -- {cores["azul"]}Cadastratar nova  Pessoa{cores["sem cor"]}')  
        print(f'{cores["verde"]}3{cores["sem cor"]} -- {cores["azul"]}Sair do sistema{cores["sem cor"]}')
        print(f'{cores["verde"]}4{cores["sem cor"]} -- {cores["vermelho"]}Para limpar dados{cores["sem cor"]}')
        print('='*40)

        opcao = leiaInt('>>> ')
    
        system('clear')
        if opcao == 3:

            # Desliga o sistema/ Sai do sistema
            print('Desligando sistema...')
            sleep(2)
            sistema_ligado = False

        elif opcao == 1:

            # Lista as pessoas cadastradas
            print('='*40)
            print(f'{"Ver pessoas cadastradas":^40}')
            print('='*40)
            sleep(1)
            
            leArquivo('banco_dados.txt')

        elif opcao == 2:

            # cadastra uma nova pessoas 
            print('='*40)
            print(f'{"Cadastrar nova pessoa":^40}')
            print('='*40)
            sleep(1)

            nome = str(input('Nome: ')).title().strip()
            idade = int(input('Idade: '))
            cadastraPessoa('banco_dados.txt', nome, idade)

        elif opcao == 4:

            # Limpa o o banco de dados
            print('Linpando banco de dados.')
            sleep(1)
            limpa('banco_dados.txt')

        else:
            print(f'{cores["vermelho"]}Erro, digite uma opcao valida!{cores["sem cor"]}')
        sleep(1)

