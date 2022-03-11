'''
Desafio 61

Problema: Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, 
          mostrando os 10 primeiros termos da progressão usando a estrutura while.
          
Problema:
'''
print('-=-'*30)
primeiro = int(input('Digite O Primeiro termo: '))
razao = int(input('Digite A Razao: '))
con = 1 
termo = primeiro 

while con <= 10: 
    con += 1 
    print(termo, end= ' -> ')
    termo += razao
    
print('FIM')
