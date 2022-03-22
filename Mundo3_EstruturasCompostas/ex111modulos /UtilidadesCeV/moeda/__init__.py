#Funcoes!
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


def resumo(valor=0, a=0, r=0):
    """Recebe 3 parametros e os mostra formatado
        
      Valor: um numero, inteiro ou real 
      a: o valor que deseja aumentar ex: 50 = 50% de aumento
      r: valor que deseja diminur
      """

    print('='*31)
    print('     TABELA COM OS VALORES')
    print('='*31)

    print(f'Valor informado: \t{moeda(valor)}')
    print(f'O dobro do preco: \t{moeda(dobro(valor))}')
    print(f'A metade do preco: \t{moeda(metade(valor))}')
    print(f'{a}% de aumento: \t{moeda(aumenta(valor, a))}')
    print(f'{r}% de reducao: \t{moeda(diminui(valor, r))}')

    print('='*31)