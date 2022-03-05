# Mostra a tabuada do numero digitado, Termina ao digitar um numero negativo!
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
