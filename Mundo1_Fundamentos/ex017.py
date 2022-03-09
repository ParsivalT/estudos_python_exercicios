from math import hypot 

c1 = float(input('Digite a Primeira Medida: '))
c2 = float(input('Digite a Segunda Medida: '))

h = hypot(c1,c2)

print(f'A Soma dos quadrados dos Catetos {c1} e {c2}')
print(f'Resulta no valor {h:.2f}')
