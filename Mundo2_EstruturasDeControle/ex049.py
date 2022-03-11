'''
Desafio 49

Problema:  Refaça o DESAFIO 9, mostrando a tabuada de um número que 
           o usuário escolher, só que agora utilizando um laço for.
           
Resolucao do problema: 
'''
print('-=-'*30)
print('>>>>>TABUADA<<<<<')

n = int(input('Digite O Numero Para ver A Tabuada Dele: '))

for c in range(1,11):
    print(f'{n} x {c:2} = {n*c}')