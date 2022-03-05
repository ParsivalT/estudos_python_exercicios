import math

print('*'*30)
#obs: tem que converter para radiais antes de imprimir ou fazer o calculo
an = math.radians(float(input('Digite o Angulo: ')))

print(f'Seno: {math.sin(an):.2f}')
print(f'Coseno: {math.cos(an):.2f}')
print(f'Tangente: {math.tan(an):.2f}')
print('*'*30)
