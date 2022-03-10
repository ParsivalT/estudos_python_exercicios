'''
Desafio 42

Problema: Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar
          que tipo de triângulo será formado:

            – EQUILÁTERO: todos os lados iguais

            – ISÓSCELES: dois lados iguais, um diferente

            – ESCALENO: todos os lados diferentes

Resolucao de problemas:
'''
l1 = float(input('Digite O Primeiro Valor: '))
l2 = float(input('Digite O Segundo Valor: '))
l3 = float(input('Digite O Terceiro Valor:'))
print('--'*20)
if l3 < l1 + l2 and l2 < l3 + l1 and l1 < l3 + l2:
    print('Os Segmentos acima Podem Formar um Triangulo ', end='')

    if l1 == l2 == l3:
        print('Equilatero!')

    elif l1 != l2 != l3 != l1:
        print('Escaleno!')

    else:
        print('Isosceles!')

else:
    print('Impossivel Formar um Triagulo com os Segmentos acima')

