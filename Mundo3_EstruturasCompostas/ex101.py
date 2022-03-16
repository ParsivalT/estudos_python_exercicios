'''
Desafio 101 

Problema: Crie um programa que tenha uma função chamada voto() que vai 
          receber como parâmetro o ano de nascimento de uma pessoa, retornando 
          um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e 
          OBRIGATÓRIO nas eleições.
          
Resolucao do problema:
'''
from datetime import date


def voto(num):
    
    ano = date.today().year
    ano -= num

    if ano < 16:
        return 'NAO VOTA!'
   
    if ano >= 18:
        return 'VOTO OBRIGATORIO!'

    if ano >= 65 or ano >= 16 and ano < 18:
        return 'OPCIONAL!'


#programa principal
print('='*36)
ano = int(input('Digite o ano do seu nascimento: '))
idade = date.today().year - ano
print(f'Com {idade} anos: {voto(ano)}')
print('='*36)
