'''
Desaafio 43

Problema:  Desenvolva uma lógica que leia o peso e a altura de uma pessoa,
           calcule seu Índice de Massa Corporal (IMC) e mostre seu status,
           de acordo com a tabela abaixo:

            – IMC abaixo de 18,5: Abaixo do Peso

            – Entre 18,5 e 25: Peso Ideal

            – 25 até 30: Sobrepeso

            – 30 até 40: Obesidade

            – Acima de 40: Obesidade Mórbida
            
Resolucao do problema:
'''
p = float(input('Digite Seu Peso: '))
a = float(input('Digite Sua Altura: '))
imc = p/(a * a)

print(f'IMC: {imc:.1f}')

if imc <= 18.4:
    print('Abaixo Do peso!')

elif imc <= 24.8:
    print('Peso Normal')

elif imc >= 25 and imc <= 29.9:
    print('Sobrepeso')

elif imc >= 30 and imc <= 34.9:
    print('Obesidade grau 1')

elif imc >= 35 and imc <= 39.9:
    print('Obesidade grau 2')

else:
    print('Obesidade grau 3')


'''IMC	Resultado
Menos do que 18,5	Abaixo do peso
Entre 18,5 e 24,9	Peso normal
Entre 25 e 29,9	    Sobrepeso
Entre 30 e 34,9	    Obesidade grau 1
Entre 35 e 39,9	    Obesidade grau 2
Mais do que 40	    Obesidade grau 3'''