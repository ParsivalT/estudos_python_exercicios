#escreva um programa que leia um valor em metros e o exiba convertido em centimetros e em milimetros
 
print('-=-'*20)
m = float(input('digite o valor em metros: '))
print('~'*58)
c = m * 100 
mi =  m * 1000

print(f'{m}m convertidos para \033[1mCentimetros\033[m = {c:.0f}cm\nconvertido em \033[1mMilimetros\033[m = {mi:.0f}mm')
print('-=-'*20)
