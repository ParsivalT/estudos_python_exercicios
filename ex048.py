multiplos = 0
for c in range(0, 501):
    i = c % 2 
    if i == 0 and i % 3 == 0:
        multiplos += c 

print(f'A Soma De Todos os numeros e {multiplos}')
