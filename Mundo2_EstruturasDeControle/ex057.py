'''
Desafio 57 

Problema:  Faça um programa que leia o sexo de uma pessoa, mas só aceite
           os valores ‘M’ ou ‘F’. Caso esteja errado, peça a digitação novamente
           até ter um valor correto.
           
Resolucao do problema:
'''
e = str(input('[M/F]'))[0]

while e not in 'MmFf':
    e = str(input('Digite uma opcao Valida: '))[0]

'''print('-=-'*30)
c = ''

while c != 'M' and c != 'F':
    c = str(input('Sexo [M/F]: ')).upper()
    if c != 'M' and c != 'F':
        print('-='*20)
        print('ERRO! Digite Uma Opcao Valida')
print('~'*20)
print(f'Opcao Digitada {c}')'''
#-------------------------------

#versao melhorada 
