'''
Desafio 105

Problema: Faça um programa que tenha uma função notas() que pode receber 
          várias notas de alunos e vai retornar um dicionário com as seguintes 
          informações:
          
                    – Quantidade de notas 
                    – A maior nota
                    – A média da turma
                    – A situação (opcional)
                    
Resolucao do problema:
'''
def notas(*valores, sit=False):
    """
    Recebe varios paramentros, calcula a media e retorna os mesmo em um dicionario
    """
    media = 0
    for c in valores:
        media += c

    aluno = {}
    aluno['total'] = len(valores)
    aluno['maior'] = max(valores)
    aluno['menor'] = min(valores)
    aluno['media'] = media // len(valores)

    if sit:
        if aluno['media'] < 5:
            aluno['situacao'] = 'Ruim'

        if aluno['media'] >= 5 and aluno['media'] <7:
            aluno['situacao'] = 'Media'

        if aluno['media'] >=7:
            aluno['situacao'] = 'Boa'

        return aluno

    else:
        return aluno


#programa principal
aluno = notas(7, 5.8, 6.5, sit=True)
print(aluno)
