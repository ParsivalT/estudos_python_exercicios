'''Qualquer Numero PAR dividido Por 2, Sobra 1
Qualquer Numero Impar Dividido Por 2 Sobra 0 '''
print('-=-'*30)
numero = int(input('Digite Um Numero Para Saber Se E IMPAR ou PAR '))
resultado = numero % 2 
if resultado == 0:
    print(f'O Numero {numero} E Par')
else:
    print(f'O Numero {numero} E impar')
print('-=-'*30)
