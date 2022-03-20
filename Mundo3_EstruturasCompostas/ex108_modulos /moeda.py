


def dobro(valor=0):
    '''Recebe um valor e multiplica o mesmo por 2'''

    resultado = valor * 2 
    return resultado

def metade(valor=0):
    '''Recebe um valor e retorna a metade'''

    resultado = valor / 2
    return resultado

def aumenta(valor=0, taxa=0):
    '''Recebe um valor e retorna o mesmo
       com um aumento de 10%'''

    resultado = valor + ((valor * taxa) / 100)
    return resultado
def diminui(valor=0, taxa=0):
    '''Recebe um valor e retorna o mesmo
       com  10% menor '''

    resultado = valor - ((valor * taxa) / 100)
    return resultado


def moeda(valor=0, moeda='R$'):
    
    return f'{moeda}{valor:.2f}'.replace('.', ',')