n1 = int(input('Digite o Primeiro: '))
n2 = int(input('Digite o Segundo: '))
n3 = int(input('Digite o Terceiro: '))

menor = n3 
maior = n1

if n2 < n1 and n2 < n3:
    menor = n2 

if n1 < n2 and n1 < n3:
    menor = n1 

if n2 > n1 and n2 > n3:
    maior = n2

if n3 > n1 and n3 > n2: 
    maior = n3
print(f'O Maior Numero: {maior}')
print(f'O Menor Numero: {menor}')
