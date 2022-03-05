#Pega o nome que foi digitado e exibe: Quantos caracteres o mesmo tem, Como fica tudo maiuscolo e minuscolo
#E quantas letras o primeiro nome tem

print('--'*30)

nome = str(input('Digite Seu Nome Completo: '))
sep = nome.split()  #uso esse metodo para dividir o nome e o sobre nome em uma lista!
u = ''.join(sep)  # agora eu junto essa lista  para poder eliminar todos os espacos do meio 
print('-=-'*20)
print()
print(f'\033[4mNome Com Todas as letras minuscula\033[m: {nome.lower()}')
print('..'*20)
print(f'\033[4mNome Com Todas Maiusculas\033[m: {nome.upper()}')
print('..'*20)
print(f'O Nome Tem \033[31m{len(u.strip())} Letras\033[m')
print('..'*20)
print(f'O Primeiro Nome tem \033[36m{len(sep[0])} Letras\033[m')
print('--'*30)
