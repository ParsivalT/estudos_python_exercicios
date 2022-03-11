'''
Desafio 83

Problema: Crie um programa onde o usuário digite uma expressão qualquer 
          que use parênteses. Seu aplicativo deverá analisar se a expressão 
          passada está com os parênteses abertos e fechados na ordem correta
          
Resolucao do problema: 
'''
cont = 0 
lista = list(input('Digite sua expressao: '))

for c in lista:

    if c == '(':
        cont += 1

    if c == ')':
        cont -= 1

if cont == 0:
    print('Sua Expressao e valida!')
    
else:
    print('Sua Expressao Nao e valida!')