print('-=-'*20)
num = int(input('Digite Um Numero: '))
print('~'*20)
print('''Escolha Uma Das 3 Opcoes
[ 1 ] Para BINARIO
[ 2 ] Para OCTA
[ 3 ] Para EXADECIMAL''')
print('~'*30)
opc = int(input())

if opc == 1:
    print(f'O Numero {num} Convertido Para Binario Fica {bin(num)[2:]}')

elif opc == 2:
    print(f'O Numero {num} Convertido Para Octa {oct(num)[2:]}')

elif opc == 3: 
    print(f'O Numero {num} Convertido Para EXADECIMAL {hex(num)[2:]}')

else: 
    print('Opcao INVALIDA')
