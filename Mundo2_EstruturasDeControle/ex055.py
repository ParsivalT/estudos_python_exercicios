''' 
Desafio 55

Problema:  Faça um programa que leia o peso de cinco pessoas. 
           No final, mostre qual foi o maior e o menor peso lidos.
           
Solucao do problema:
'''
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
