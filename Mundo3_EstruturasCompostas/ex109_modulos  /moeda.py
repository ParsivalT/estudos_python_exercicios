


def dobro(valor=0, moedaf=False):
    '''Recebe um valor e multiplica o mesmo por 2'''

    resultado = valor * 2 

    if moedaf:
        resultado = moeda(resultado)

    return resultado

def metade(valor=0, moedaf=False):
    '''Recebe um valor e retorna a metade'''

    resultado = valor / 2

    if moedaf:
        resultado = moeda(resultado)

    return resultado

def aumenta(valor=0, taxa=0, moedaf=False):
    '''Recebe um valor e retorna o mesmo
       com um aumento de 10%'''

    resultado = valor + ((valor * taxa) / 100)

    if moedaf:
        resultado = moeda(resultado)

    return resultado


def diminui(valor=0, taxa=0, moedaf=False):
    '''Recebe um valor e retorna o mesmo
       com  10% menor '''

    resultado = valor - ((valor * taxa) / 100)

    if moedaf:
        resultado = moeda(resultado)
        
    return resultado


def moeda(valor=0, moeda='R$'):
    
    return f'{moeda}{valor:.2f}'.replace('.', ',')