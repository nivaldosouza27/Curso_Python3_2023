import os
import shutil
from pathlib import Path
from zipfile import ZipFile

# Caminhos
CAMINHO_RAIZ = Path(__file__).parent
CAMINHO_ZIP_DIR = CAMINHO_RAIZ / 'Modulos_aula130_ZIP'
CAMINHO_COMPACTADO = CAMINHO_ZIP_DIR / 'aula130_compactado.zip'
CAMINHO_DESCOMPACTADO = CAMINHO_ZIP_DIR / 'aula130_descompactado'

shutil.rmtree(CAMINHO_ZIP_DIR, ignore_errors=True)
Path.unlink(CAMINHO_COMPACTADO, missing_ok=True)
shutil.rmtree(str(CAMINHO_COMPACTADO).replace('.zip', ''), ignore_errors=True)
shutil.rmtree(CAMINHO_DESCOMPACTADO, ignore_errors=True)


# Cria o diretorio para a aula
CAMINHO_ZIP_DIR.mkdir(exist_ok=True)


# Função que cria os arquivos nos diretorios
def criar_arquivos(qtd: int, zip_dir: Path):
    for i in range(qtd):
        texto = f'arquivo_{i}'
        with open(zip_dir / f'{texto}.txt', 'w') as arquivo:
            arquivo.write(texto)


criar_arquivos(10, CAMINHO_ZIP_DIR)

# Criando a pasta compactada
with ZipFile(CAMINHO_COMPACTADO, 'w') as zip:
    for root, dirs, files in os.walk(CAMINHO_ZIP_DIR):
        for file in files:
            zip.write(os.path.join(root, file), file)

# Lendo a pasta compactado
with ZipFile(CAMINHO_COMPACTADO, 'r') as zip:
    for arquivo in zip.namelist():
        print(arquivo)

# Desempacotando os arquivos
with ZipFile(CAMINHO_COMPACTADO, 'r') as zip:
    zip.extractall(CAMINHO_DESCOMPACTADO)
