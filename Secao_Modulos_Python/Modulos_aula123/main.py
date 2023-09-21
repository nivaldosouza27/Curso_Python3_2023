from pathlib import Path

# Mostrando o caminho do projeto
caminho_projeto = Path().absolute()
# print(caminho_projeto)

# Mostrando o caminho do arquivo
caminho_arquivo = Path(__file__)
# print(caminho_arquivo)

# Mostrando a pasta superior ao caminho desejado
caminho_parent = caminho_arquivo.parent
# print(caminho_parent)

# Criando um novo caminho - **Não cria o arquivo**
new_file = caminho_parent / 'new_file.txt'
# print(new_file)

# deletar uma pasta
# new_folder.unlink()

# criar nova pasta
# new_file.touch()

# escrever algo no arquivo
# new_file.write_text('Hello World! \n\r')

# escrever varias linhas no arquivo com context manager
with new_file.open('a+') as file:
    file.write('Uma linha \n\r')
    file.write('Outra linha \n\r')
    file.write('Outra linha \n\r')
    file.write('Outra linha \n\r')
    file.write('Outra linha \n\r')

# ler e printar o arquivo
# print(new_file.read_text())

new_folder = caminho_parent / 'Teste'
new_folder.mkdir(exist_ok=True)

other_file = new_folder / 'other.txt'
other_file.touch()
other_file.write_text('Ola de novo')

new_folder_2 = caminho_parent / 'Teste_2'
new_folder_2.mkdir(exist_ok=True)

for i in range(10):
    file = new_folder_2 / f'file_{i}.txt'
    file.touch()

    if file.exists():
        file.unlink()
    else:
        file.touch()
    with file.open('a+') as text_file:
        text_file.write('Ola Mundo \n\r')
        text_file.write(f'file_{i}.txt')


def rmtree(root: Path, remove_root=True):
    for file in root.glob('*'):
        if file.is_dir():
            print('DIR', file)
            rmtree(file, False)
            file.rmdir()
        else:
            print('FILE', file)
            file.unlink()

    if remove_root:
        root.rmdir()


rmtree(new_folder_2)
