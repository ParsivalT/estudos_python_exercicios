#mostra uma PA 

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
