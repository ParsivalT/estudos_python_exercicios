#Mostra os 10 primeiros termos de uma PA

print('-=-'*20)
primeiro = int(input('Primeiro Termo: '))
razao = int(input('Razao: '))
termo = primeiro 
cont = 1
periodo = 10
fim = ''
print('--'*30)

while cont <= periodo :

    cont += 1 
    print(termo, end=' -> ')
    termo += razao 
    if cont > periodo:

        fim = str(input('Deseja Continuar? [S/N]: ')).upper().strip()
        if fim == 'S':

            print('--'*30)
            periodo += int(input('digite o numero desejado de termos: '))
        
        elif fim == 'N':
            break 

        else: 
            print('Digite uma Opcao valida!')
            

print('-=-'*20)
print(f'PA finalizada com {periodo} termos! ')
print('-=-'*20)
