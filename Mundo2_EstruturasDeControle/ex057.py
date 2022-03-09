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

e = str(input('[M/F]'))[0]

while e not in 'MmFf':
    e = str(input('Digite uma opcao Valida: '))[0]
