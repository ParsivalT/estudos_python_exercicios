'''
Desafio 81

Problema:  Crie um programa que vai ler vários números e colocar em uma lista.
           Depois disso, mostre:                                                      
                
                 A) Quantos números foram digitados.                                                    
                 B) A lista de valores, ordenada de forma decrescente.                                  
                 C) Se o valor 5 foi digitado e está ou não na lista.
                 
Resolucao do problema:
'''
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
