print('-=-'*10)
n1 = n2 = n3 = n4 = n5 = 0
for c in range(1,6):
    numeros = int(input(f'Digite os valores: '))
    if c == 1:
        n1 = numeros
    else:
        if c == 2:
            n2 = numeros
        else:
            if c == 3:
                n3 = numeros
            else:
                if c == 4:
                    n4 = numeros
                else:
                    if c == 5:
                        n5 = numeros
                    
lista = (n1,n2,n3,n4,n5)

print('-=-'*10)
print(f'O numero 9 apareceu: {lista.count(9)} vezes')
if 3 in lista:
    print(f'O numero 3 apareceu na posicao: {lista.index(3)}')
else:
    print('O numero 3 Nao apareceu nenhuma')
print('Os numeros pares digitados foram:', end=' ')

for c in range(len(lista)):
    if lista[c] % 2 == 0:
        print(lista[c], end=' ')
        
print()