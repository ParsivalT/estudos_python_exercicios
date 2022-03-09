print('Digite Os Valores Desejado E veja Se e Possivel Formar um Triangulo!')
print('='*30)
l1 = float(input('Digite O Primeiro Valor: '))
l2 = float(input('Digite O Segundo Valor: '))
l3 = float(input('Digite O Terceiro Valor: '))

if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l2 + l1:
    print('\033[36mE possivel \033[mformar Um Triangulo!')

else:
    print('\033[4:31mNao e Possivel \033[mformar Um Triangulo!')
print('='*30)

