

# with open ('aula99.txt', 'w') as arquivo:
#     ...

class MyOpen:
    def __init__(self, caminho_arquivo, modo) -> None:
        self.caminho_arquivo = caminho_arquivo
        self.modo = modo
        self._arquivo = None

    def __enter__(self):
        print('Abrindo Arquivo')
        self._arquivo = open(self.caminho_arquivo, self.modo, encoding='utf8')
        return self._arquivo

    def __exit__(self, class_exception, expection_, traceback_):
        print('Fechando Arquivo')
        self._arquivo.close()

        # print(class_exception)
        # print(expection_)
        # print(traceback_)
        #expection_.add_note('Minha Nota')
        raise ConnectionError('Não deu para conectar')
        # return True

with MyOpen('POO_aula99.txt', 'w') as arquivo:
    arquivo.write('Linha 1\n')
    arquivo.write('Linha 2\n', 123)
    arquivo.write('Linha 3\n')
    print('With', arquivo)