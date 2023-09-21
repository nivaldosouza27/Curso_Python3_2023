# os + shutil - Apagando, copiando, movendo e renomeando pastas com Python
# Vamos copiar arquivos de uma pasta para outra.
# Copiar -> shutil.copy
# Copiar Árvore recursivamente -> shutil.copytree
# Apagar Árvore recursivamente -> shutil.rmtree
# Apagar arquivos -> os.unlink
# Renomear/Mover -> shutil.move ou os.rename

import os
import shutil

HOME = os.path.expanduser('E:')
PASTA = os.path.join(HOME, 'Teste_Python')
PASTA_ORIGINAL = os.path.join(PASTA, 'Exemplo')
NOVA_PASTA = os.path.join(PASTA, 'Nova_pasta')
os.makedirs(NOVA_PASTA, exist_ok=True)

shutil.rmtree(NOVA_PASTA)
shutil.copytree(PASTA_ORIGINAL, NOVA_PASTA)
shutil.move(NOVA_PASTA, NOVA_PASTA + 'EITA')

# for root, dirs, files in os.walk(PASTA_ORIGINAL):
#     for file in files:
#         caminho_original = os.path.join(root, file)
#         caminho_new_dir = os.path.join(
#             root.replace(PASTA_ORIGINAL, NOVA_PASTA), file)
#         shutil.copy(caminho_original, caminho_new_dir)
