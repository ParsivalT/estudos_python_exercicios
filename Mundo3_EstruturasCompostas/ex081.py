#Uma algoritimo que recebe varios valores, e em ordem decresente e se o numero 5 foi digitado
# for: Thiago 06/03/2022

lista = []

while True:

    print('--'*25)
    lista.append(int(input('Digite o valor desejado: ')))
    continua = str(input('Deseja continuar? [S/N]: ')).upper()

    while continua not in 'SN':

        continua = str(input('Deseja continuar? [S/N]: ')).upper()
    
    if continua == 'N':
        break

lista.sort(reverse = True)

print('='*30)
print(f'Voce digitou {len(lista)} elementos')
print(f'Os valores em ordem decrecente sao {lista}')

if 5 in lista:
    print('Voce Digitou o numero 5')
print('='*30)
