# os.walk para navegar de caminhos de forma recursiva
# os.walk é uma função que permite percorrer uma estrutura de diretórios de
# maneira recursiva. Ela gera uma sequência de tuplas, onde cada tupla possui
# três elementos: o diretório atual (root), uma lista de subdiretórios (dirs)
# e uma lista dos arquivos do diretório atual (files).

import os
from itertools import count
from Modulos_aula118 import formata_tamanho

caminho = os.path.join(
    'E:\\Arquivos e Midia\\PASTA TUDO\\Wallpapers game of Thrones')
counter = count()

for root, dirs, files in os.walk(caminho):
    the_counter = next(counter)
    print(the_counter, 'Pasta Atual', root)

    for dir_ in dirs:
        print('   ', the_counter, 'Dir', dir_)

    for file_ in files:
        caminho_completo = os.path.join(root, file_)
        tamanho_arquivo = os.path.getsize(caminho_completo)
        print('   ', the_counter, 'File', file_,
              formata_tamanho(tamanho_arquivo))
