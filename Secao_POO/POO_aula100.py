from contextlib import contextmanager

@contextmanager
def my_open(caminho_arqivo, modo):
    try:
        print('Abrindo Arquivo')
        arquivo = open(caminho_arqivo, modo, encoding='utf8')
        yield arquivo
    except Exception as e:  
        print('Ocorreu Erro', e)
    finally:
        print('Fechando arquivo')
        arquivo.close()

with my_open('POO_aula100.txt', 'w') as arquivo:
    arquivo.write('Linha 1\n')
    arquivo.write('Linha 2\n', 123)
    arquivo.write('Linha 3\n')
    print('With', arquivo)



    