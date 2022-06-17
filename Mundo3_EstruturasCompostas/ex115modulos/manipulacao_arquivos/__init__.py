cores = {'sem cor':'\033[m',
         'vermelho':'\033[31m',
         'verde':'\033[32m',
         'azul':'\033[36m'}


def arquivoExiste(arq):
    "Checa se o arquivo existe"

    try: 
        with open(arq, 'rt') as arquivo:
            return True
        
    
    except FileNotFoundError:
        return False
        
    
def criaArquivo(arq):
    "Cria um arquivo txt"

    try: 
        with open(arq, 'wt+') as arquivo:
            print(f'Arquivo {arq} criado com sucesso')

    except:
        print('Erro ao criar o arquivo!')

        
def leArquivo(arq):
    "Imprime na tela as pessoas cadastradas"

    try:
        arquivo = open(arq, 'rt')
        

    except:
        print('Erro ao abrir o arquivo')

    else:
        try:
	    
            print(f'{" Nome":<30}{"Idade":>8}')
            print('-'*40)
            for linha in arquivo:

                dado = linha.split(';')
                dado[1] = dado[1].replace('\n', '')
                print(f'|{dado[0]:<30}{dado[1]:>3} anos')

        except:
            print(f'{cores["vermelho"]}Houve um erro ao exibir as pessoas cadastradas....{cores["sem cor"]}')
    
    finally:
        arquivo.close()


def cadastraPessoa(arq, nome, idade):
    "Cadastra um pessoa"

    try:
        with open(arq, 'at') as arquivo:

            try:
                arquivo.write(f'{nome};{idade}\n')

            except:
                print(f'{cores["vermelho"]}Erro ao escrever o no arquivo!{cores["sem cor"]}')
    except:
        print(f'{cores["vermelho"]}Erro ao abrir o arquivo!{cores["sem cor"]}')


def limpa(arq):
    "limpa os dados contido dentro do arquivo .txt"
    try:
        with open(arq, 'wt+') as arquivo:
            dados = arquivo

    except:
        print('Houve um problema ao limpar os dados ')

    