#crie um algoritimo que leia um numero e mostre seu dobro,triplo e raiz quadrada. 

print('-=-'*20)
n = int(input('\033[36mdigite um numero:\033[m '))
print('~'*30)
d = n * 2 
t = n * 3 
r = n **(1/2) 

print(f'O dobro de \033[31m{n}\033[m E:\033[32m{d}\033[m\nja o Triplo E: \033[35m{t}\033[m\nEa raiz quadrada E: \033[7:107:30m{r:.3}\033[m')
print('-=-'*20)
