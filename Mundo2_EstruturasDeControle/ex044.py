'''avista dinheiro/cheque:10% de desconto
avista no cartao:5% de desconto 
em 2x no cartao preco normal 
3x ou mais no cartao 20% de juros '''

print('-=-'*20)
p = float(input('Digite O Preco Do Produto: R$'))
print('~'*30)
print('''Escolha A Forma De Pagameto desejado(a)

>>>>>>>> Digite <<<<<<<<

(1) Avista Dinheiro/Cheque
(2) Avista no Cartao 
(3) Parcelado no Cartao ''')
print('~'*30)
f = int(input(':'))
print('~'*30)

if f == 3:
    print('Deseja Parcelar Em Quantas vezes ?')
    pa = int(input('x'))
    if pa <= 2:
        t = p / pa
        print(f'Total {pa} parcelas de  R${t:.2f}')

    else:
        t =(p + p*20/100) / pa
        print(f'Total {pa} parcelas de R${t:.2f}')

elif f == 2:
    t = (p-(p*5/100))
    print(f'O Valor Do Produto De R${p:.2f} foi para R${t:.2f}')

else:
    t = (p-(p*10/100))
    print('com 10% de DESCONTO')
    print(f'O Valor Do Produto De R${p:.2f} foi para R${t:.2f} ')

print('-=-'*20)
