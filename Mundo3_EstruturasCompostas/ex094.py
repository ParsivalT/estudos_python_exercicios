'''
Desafio 94

Problema: Crie um programa que leia nome, sexo e idade de várias pessoas, 
          guardando os dados de cada pessoa em um dicionário e todos os dicionários 
          em uma lista. No final, mostre: 
                
                A) Quantas pessoas foram cadastradas 
                B) A média de idade 
                C) Uma lista com as mulheres 
                D) Uma lista de pessoas com idade acima da média
                
Resolucao do problema:
'''

#definindo as variaveis
pessoa = {}
mulheres = []
dados = []
acima_media = {}
media = soma = 0

#coletando os dados
while True:

    print('='*30)
    pessoa['nome'] = str(input('Nome: '))
    pessoa['idade'] = int(input('idade: '))
    pessoa['sexo'] = str(input('Sexo [M/F]: ')).upper().strip()
    soma += pessoa['idade']

    while pessoa['sexo'] not in 'FM':
        pessoa['sexo'] = str(input('Digite apenas F ou M: ')).upper().strip()

    if pessoa['sexo'] == 'F':
        mulheres.append(pessoa.copy())

    dados.append(pessoa.copy())
    continua = str(input('Deseja continuar? [S/N]: ')).upper().strip()

    while continua not in 'SN':
        continua = str(input('Digite apenas S ou N: ')).upper().strip()

    if continua == 'N':
        break

media = soma / len(dados)

print('=-'*20)
print(f'  - Um total de {len(dados)} pessoas foram cadastradas!')
print(f'  - A media de idade foi: {media:5.2f}')
print('  - Mulheres cadastradas: ',end='')

for p in dados:
    if p['sexo'] in 'F':
        print(f'{p["nome"].title()} ', end='')

print('\n  - Pessoas que estao acima da media: \n')

for p in dados:
    if p['idade'] >= media:
        print('    ', end='')

        for k, v in p.items():
            print(f'{k} = {v}; ', end='')

        print()

print('<< FIM >>')