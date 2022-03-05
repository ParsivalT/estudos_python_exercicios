#faca um script que cheque o tipo do valor digitado e imprima na tela 

print('~'*20)
a = input('\033[36mdigite algo:\033[m')
print('-=-'*20)
print(f'\033[1mO tipo primitivo de desse valor e:\033[32m{type(a)}\033[m') #type mostra o tipo da variavel
print('~'*20)
print('\033[1mSomente espacos?\033[m \033[34m', a.isspace(),'\033[m')
print('~'*20)
print('E um numero decimal?\033[31m', a.isdecimal(), '\033[m')
print('~'*20)
print('E um numero?\033[31m', a.isnumeric(), '\033[m') 
print('-=-'*20)


'''p = input('Digite o Seu Nome: ')
if p.isnumeric() == True: 
    print('Nao Insira Numeros Nesse Campo!')'''
    