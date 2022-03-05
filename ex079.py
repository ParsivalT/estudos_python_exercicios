#algoritimo que guarde quantos valores o usuario quiser em uma lista 
#  for: Thiago 05/03/2022

lista = []

while True:

    print('-='*20)
    valor = int(input('Digite um valor: '))
    if valor in lista:
        print('Erro! Digite outro valor')

    else:
        print('Valor adicionado com Sucesso!')
        lista.append(valor)

    continua = str(input('Deseja continuar? [S/N]: ')).upper()
    while continua not in 'SN':
        continua = str(input('Deseja continuar? [S/N]: ')).upper()
    
    if continua == 'N':
        break

lista.sort()
print('Valores digitados: ', end='')
print(*lista, sep= ',')
print('-='*20)
