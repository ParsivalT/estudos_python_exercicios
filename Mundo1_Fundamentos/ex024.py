#crie um programa que leia o nome de uma cidade e veja se ela comeca com (SANTOS)

cidade = str(input('Em Que Cidade Voce Nasce?: ')).strip()
cidade = cidade.lower()
print('santos' in cidade)
