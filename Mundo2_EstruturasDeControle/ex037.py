'''
Desafio 86

Problema:  Escreva um programa em Python que leia um número inteiro qualquer
           e peça para o usuário escolher qual será a base de conversão: 

                1 para binário, 
                2 para octal 
                3 para hexadecimal.
                
Resolucao do problema:
'''
print('-=-'*10)
num = int(input('Digite Um Numero: '))
print('~'*30)

print('''Escolha Uma Das 3 Opcoes
[ 1 ] Para BINARIO
[ 2 ] Para OCTA
[ 3 ] Para EXADECIMAL''')
print('~'*30)

opc = int(input('>>> '))

if opc == 1:
    print(f'O Numero {num} Convertido Para Binario Fica: {bin(num)[2:]}')

elif opc == 2:
    print(f'O Numero {num} Convertido Para Octa Fica: {oct(num)[2:]}')

elif opc == 3: 
    print(f'O Numero {num} Convertido Para EXADECIMAL Fica: {hex(num)[2:]}')

else: 
    print('Opcao INVALIDA')
