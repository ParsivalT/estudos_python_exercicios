'''
Desafio 101 

Problema: Crie um programa que tenha uma função chamada voto() que vai 
          receber como parâmetro o ano de nascimento de uma pessoa, retornando 
          um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e 
          OBRIGATÓRIO nas eleições.
          
Resolucao do problema:
'''
def voto(num):
    from datetime import date

    atual = date.today().year
    idade = atual - num 

    if idade < 16:
        return f'Com {idade} anos: NAO VOTA!'
   
    if idade >= 18:
        return f'Com {idade} anos: VOTO OBRIGATORIO!'

    if idade >= 65 or idade >= 16 and idade < 18:
        return f'Com {idade} anos: OPCIONAL!'


#programa principal
ano = int(input('Digite o ano de nascimento: '))
print(voto(ano))
