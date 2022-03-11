'''
Desafio 56

Problema: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. 
          No final do programa, mostre: a média de idade do grupo, qual é o 
          nome do homem mais velho e quantas mulheres têm menos de 20 anos
          
Resolucao do problema:
'''
print('-=-'*30)

media_g = 0 
menos = 0
total_f = 0
total_m = 0 
maiornome = ''

for c in range(1,5):
    s = str(input('Sexo[M/F]: ')).upper()

    if s == 'F':
        total_f += 1
        nome = str(input('Nome: '))
        idade = int(input('Idade: '))
        media_g += idade

        if idade < 20:
            menos += 1
       
    elif s == 'M':
        total_m += 1
        nome = str(input('Nome: '))
        idade = int(input('Idade: '))
        media_g += idade 

        if total_m == 1:
            maior = idade 
            maiornome = nome

        if idade > maior:
            maior = idade 
            maiornome = nome
    else:
        print('Erro! Por Favor Digite certo!')
        break

    print('--'*30)

media_g = media_g / 4 

print(f'A Media de idade do grupo e: {media_g:.1f} anos')
print(f'Com {maior} anos {maiornome} eo homen mais velho')
print(f'{menos} mulheres tem menos de 20 anos')
