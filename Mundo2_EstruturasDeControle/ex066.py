numero =  0 
total = 0 
while True:

    print('--'*10)
    numero = int(input('Digite os numeros: '))
    if numero != 999:
        
        total += numero
    
    if numero == 999:
        break

print('-=-'*10)
print(f'A soma de  todos valores digitados: {total}')
print('-=-'*10)
