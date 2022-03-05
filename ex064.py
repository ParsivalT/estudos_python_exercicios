# guarda os numeros digitados e depois os somalos 

print('-=-'*20)
numero = int(input('Digite um numero[999 para o programa]: '))
soma = 0

while numero != 999:

    if numero == 999:
        break

    else:

        soma += numero
        print('--'*10)
        
        numero = int(input('Digite um numero[999 para o programa]: '))
print('-=-'*20)       
print(f'a Soma dos numeros digitados E: {soma}')
print('-=-'*20)
