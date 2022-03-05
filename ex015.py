#aluguel de carro 

print('--'*30)
d = int(input('Por quantos dias o carro foi alugado? Dia: '))
k = float(input('Quantos quilometros foram percoridos? km: '))

t = (d * 60) + (k * 0.15)

print(f'O total a pagar e De: R${t:.2f}')
print('Obrigado por Alugar Com A nossa Empresa')
print('--'*30)
