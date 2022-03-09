#Fazer uma tabela de precos usando colecoes
print('=='*35)
print('\t\t\t  TABELA DE PRECOS')
print('=='*35)

produtos = ('Fone de Ouvido', 25.50, 'Mouse', 35.00, 'Notebook', 1500.00, 'Caixinha de Som', 20.00,
            'Case HD externo', 15.00, 'Teclado', 45.55, 'Controle PS3', 250.00, 'Oculos', 450.50)

for c in range(len(produtos)):
    if c % 2 == 0: 
        print(f'{produtos[c]:<15}|', end= '.'*43)
    
    else:
        print(f'|R$  {produtos[c]:.2f}')

print('=='*35)
