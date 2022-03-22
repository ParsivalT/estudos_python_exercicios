def leiaDinheiro(valor):
    """-> Validador de dinheiro:"""

    valido = False

    while not valido:
        num = str(input(valor)).strip()
        
        if num.isalpha() or num == '':
            print(f'\033[31mERRO! \"{num}\" nao e um preco valido!\033[m')

        else:
            valido = True

    if ',' in num:
        num = num.replace(',','.')
        return float(num)

    else:
        return float(num)