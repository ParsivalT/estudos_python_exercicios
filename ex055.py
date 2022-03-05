'''menor = 0
maior = 0 
pesos = [] 

for c in range(1, 6):
    p = float(input(f'Digite o Peso da {c} pessoa: '))
    pesos.append(p)
    if p > maior:
        maior = p 
        
    elif p < maior:
        menor = p

    else:
        menor = p
    for i in range(len(pesos)):
        if pesos[i] < menor:
            menor = pesos[i]
print('-=-4')           
print(f'O Maior peso registrado foi {maior} eo Menor foi {menor}')'''

'''Resposta do Professor'''


maior = 0
menor = 0

for c in range(1,6):
    p = float(input(f'Digite o Peso Da {c} Pessoa: '))
    if c == 1:
        maior = p
        menor = p
        
    else:
      
        if p > maior:
            maior = p 
            
        if p < menor:
            menor = p
            
print(f'O Maior valor regitrado foi {maior} eo meor {menor}')
