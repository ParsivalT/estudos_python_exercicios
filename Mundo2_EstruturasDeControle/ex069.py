'''
Desafio 69 

Problema: Crie um programa que leia a idade e o sexo de várias pessoas. 
          A cada pessoa cadastrada, o programa deverá perguntar se o usuário 
          quer ou não continuar. No final, mostre:

                A) quantas pessoas tem mais de 18 anos.

                B) quantos homens foram cadastrados.

                C) quantas mulheres tem menos de 20 anos.

Resolucao do problema:
'''
homens = homens_18 = mulheres_20 = 0

print('--'*17)
print('\tCadastre Pessoas!')
print('--'*17)

while True:
    
    idade = int(input('\nIdade: '))
    sexo = str(input('Qual o Sexo? [M/F]: '))[0].upper()

    while sexo not in 'MmFf':

        print('Por favor, digite uma opcao valida!')
        sexo = str(input('Qual o Sexo? [M/F]: '))[0]

    continua = str(input('Deseja continuar? [S/N]: ')).upper()

    if sexo == 'F' and idade  < 20:
       mulheres_20 += 1 

    if sexo == 'M' and idade > 18:
        homens_18 += 1

    if sexo == 'M':
        homens += 1

    if continua == 'N':
        break 

    print('--'*17)  

print('-=-'*10)
print('\tESTATISTICAS!')
print('-=-'*10)

print(f'\033[1m\nExistem {mulheres_20} Mulheres com menos de 20 anos!')
print(f'Existem {homens_18} Homens com menos de 18 anos!')
print(f'Total de Homens cadastrados: {homens}\033[m')