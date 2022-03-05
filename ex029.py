'''fraca um programa que leia a velocidade de um veiculo e se 
ela for acima de 80km/h ele sera multado, valor da multa 7,00 pra cada km a mais '''

print('Por favor Informe a Velocidade Do Veiculo!')
print('--'*30)
v = float(input('Km/h: '))
if v >= 80:
    print('Voce Foi MULTADO!')
    m = (v - 80)* 7.00
    print(f'O Valor da multa: {m:.2f}')

else:
    print(f'Voce Nao Foi Multado!')

print('Tenha Um Bom Dia!')
print('--'*30)
