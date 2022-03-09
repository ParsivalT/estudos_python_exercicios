#checa se uma expressao matematica e valida ou nao!
#for Thiago 07/03/2022

cont = 0 
lista = list(input('Digite sua expressao: '))
for c in lista:
    if c == '(':
        cont += 1

    if c == ')':
        cont -= 1

if cont == 0:
    print('Sua Expressao e valida!')
    

else:
    print('Sua Expressao Nao e valida!')