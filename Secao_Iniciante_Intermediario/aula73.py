# Criando arquivos com Python + Context Manager with
# Usamos a função open para abrir
# um arquivo em Python (ele pode ou não existir)
# Modos:
# r (leitura), w (escrita), x (para criação)
# a (escreve ao final), b (binário)
# t (modo texto), + (leitura e escrita)
# Context manager - with (abre e fecha)
# Métodos úteis
# write, read (escrever e ler)
# writelines (escrever várias linhas)
# seek (move o cursor)
# readline (ler linha)
# readlines (ler linhas)
# Vamos falar mais sobre o módulo os, mas:
# os.remove ou unlink - apaga o arquivo
# os.rename - troca o nome ou move o arquivo
# Vamos falar mais sobre o módulo json, mas:
# json.dump = Gera um arquivo json
# json.load

#definindo o caminho de onde está o arquivo texto 
import os

caminho_arquivo = 'C:\\Users\\nival\\OneDrive\\Área de Trabalho\\Projetos\\Python\\Projeto_Curso_Python\\testes\\aula73.txt'

#função que faz a abertura e fechamento do arquivo automaticamente
with open(caminho_arquivo, 'w+', encoding='utf8') as arquivo:
    #WriteLine escreve uma linha no arquivo
    arquivo.write('Linha 1\n')
    arquivo.write('Linha 2\n')

    #escreve varias linhas no arquivo, atraves de um iteravel
    arquivo.writelines(
        ('Linha 3\n', 'Linha 4\n', 'Linha 5\n')
    )
    arquivo.writelines(
        ('Meu nome é\n', 
         'Nivaldo de \n', 
         'Souza Martins\n')
    )
    #Comando seek faz com que o cursor de leitura do arquivo va para determinado ponto
    arquivo.seek(0,0)
    print('READLINE')
    arquivo.seek(0,0)

    #Lendo uma linha do arquivo com com a função readline(Depende de quantas vezes for chamada a função)
    print(arquivo.readline(), end='')
    print(arquivo.readline().strip())
    print(arquivo.readline().strip())
    print(arquivo.readline().strip())
    print(arquivo.readline().strip())
    print()
    
    #Lendo varias linhas de uma vez com a função redlines que retorna uma lista de linhas
    print('READLINES')
    arquivo.seek(0,0)
    for linha in arquivo.readlines():
        print(linha.strip())

#abrindo e fechando novamente o arquivo no modo read only
with open(caminho_arquivo, 'r') as arquivo:
   print()
   print('Lendo Função Read')
   print(arquivo.read())

'''
# Remove os arquivos
os.remove(caminho_arquivo)
os.unlink(caminho_arquivo)

#renomeia e move o arquivo para outro arquivo
os.rename(caminho_arquivo, 'aula73.2.txt')

'''