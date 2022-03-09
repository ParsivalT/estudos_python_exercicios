print('='*31)
numeros = ('Zero', 'Um', 'Dois', 'Tres', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezeseis', 'Dezessete', 'Dezoito','Dezenove', 'Vinte')
numero = int(input('Digite um numero Entre 0 e 20: '))

while numero > 20 or numero < 0:

    print('Digite um valor valido!')
    numero = int(input('Digite um numero Entre 0 e 20: '))

print('='*31)
print(f'O numero: {numero} por estenso fica: {numeros[numero]}')
print('='*31)
