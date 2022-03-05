#faca um programa que leia a largura ea altura de uma paredem, calcule sua area ea quantidade
#de tinta nescessaria para pintar. sabendo que cada litro de tinta, pinta 2m²
print('-=-'*20)
l = float(input('digite a Largura: '))
a = float(input('digite a Altura: '))

area = l*a

print('-=-'*20)
print(f'O \033[1mdiametro\033[m de: \033[32m{area:.2f}m²\033[m')
print(f'A quantidade de tinta necessaria para pintar\n\033[32m{area:.2f}m²\033[m Sao de \033[33m{area/2}l\033[m')
print('-=-'*20)
