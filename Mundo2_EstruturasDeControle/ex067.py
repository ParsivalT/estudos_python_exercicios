'''
Desafio 67

Problema: Faça um programa que mostre a tabuada de vários números, 
          um de cada vez, para cada valor digitado pelo usuário. 
          O programa será interrompido quando o número solicitado for negativo.
          
Resolucao do problema:
'''
numero = 0

while True:
    
    print('--'*10)
    numero = int(input('Digite: '))

    if numero >= 0:
        for c in range(0, 11):
            print(f'{numero} x {c} = {numero*c}')
    
    else:

        print('\nVolte sempre!')
        break
