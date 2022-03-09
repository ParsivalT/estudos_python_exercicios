print('-=-'*20)
i = int(input('Digite o Numero que deseja saber o fatorial!: '))
cont = 1  # para uma multiplicacao limpa ao inves de 0 o contador comeca cm 1!
f = 0
print('--'*30)
print(f'{i}! = ', end='')
while i > 1:    #enquanto o numero digitado for maior que 1, execute o comando abaixo 
    cont *= i
    i -= 1
    print(i,end='')
    print(' x ' if i > 1 else ' = ', end='') # escreva na tela se o numero for maior que 1 

print(cont)
print('-==-'*20)