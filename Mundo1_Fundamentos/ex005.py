#crie um programa que leia um numero inteiro e mostre o seu antecessor eo sucessor 

print('~'*20)
n = int(input('digite um numero: '))
print('~'*20)
n_an = n - 1 
n_su = n + 1 

print(f'O Antecessor Do Numero {n}\nAntecessor:\033[31m{n_an}\033[m\nSucessor:\033[36m{n_su}\033[m')
print('~'*20)
