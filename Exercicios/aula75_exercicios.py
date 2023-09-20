# Exercício - Lista de tarefas com desfazer e refazer

#blibliotecas
import os
import json

#Variaveis 
lista_de_tarefas = []
lista_temp = []


#Função que retorna a lista
def listar_tarefas(list):
    print()
    if not list:
        print('Não há o que listar')
        print()
        return
    print(list)
    print()

#Função que desfaz a ultima tarefa feita
def desfazer_tarefa(list, lista_temp):
    print()
    if not list:
        print('Não há o que desfazer')
        print()
        return
    tarefa = list.pop()
    print(f'O item "{tarefa}" foi removido da lista')
    lista_temp.append(tarefa)
    listar_tarefas(lista_de_tarefas)

#Função que refazer a ultima tarefa desfeita
def refazer_tarefa(list, lista_temp ):
    print()
    if not lista_temp:
        print('Não há o que refazer')
        print()
        return
    tarefa = lista_temp.pop()
    print(f'O item "{tarefa}" foi readicionado a lista')
    list.append(tarefa)
    listar_tarefas(lista_de_tarefas)

#Função que adiciona uma tarefa na lista
def adicona_tarefas(string, list):
    print()
    string = string.strip()
    if not string:
        print('Voce não digitou uma tarefa')
        return
    list.append(string)
    print(f'O item "{string}" foi adicionado a lista')
    listar_tarefas(lista_de_tarefas)

#Função que adiciona e le dados em umarquivo JSON
def ler(tarefas, caminho_arquivo):
    dados = []
    try:
        with open(caminho_arquivo, 'r', encoding='utf8') as arquivo:
            dados = json.load(arquivo)
    except FileNotFoundError:
        print('Arquivo não existe')
        salvar(tarefas, caminho_arquivo)
    return dados


def salvar(tarefas, caminho_arquivo):
    dados = tarefas
    with open(caminho_arquivo, 'w', encoding='utf8') as arquivo:
        dados = json.dump(tarefas, arquivo, indent=2, ensure_ascii=False)
    return dados


CAMINHO_ARQUIVO = 'aula75.json'
tarefas = ler([], CAMINHO_ARQUIVO)
tarefas_refazer = []


while True:
    print('Comandos: listar, desfazer, refazer')
    string = input('Digite um comando: ')
     
## Solução curta com string em um dicionario chamando os metodos das funções lambdas
    comandos = {
        'listar': lambda: listar_tarefas(lista_de_tarefas),
        'desfazer': lambda: desfazer_tarefa(lista_de_tarefas, lista_temp),
        'refazer': lambda: refazer_tarefa(lista_de_tarefas, lista_temp),
        'clear': lambda: os.system('cls'),
        'adicionar': lambda: adicona_tarefas(string, lista_de_tarefas),
    }
    comando = comandos.get(string) if comandos.get(string) is not None else comandos['adicionar']
    comando()
    salvar(lista_de_tarefas, CAMINHO_ARQUIVO)

##Salvando a lista uma base de dados JSON


### Seleção com strings condicionais IF

    # if string == 'listar':
    #     listar_tarefas(lista_de_tarefas)
    
    # elif string == 'desfazer':
    #     desfazer_tarefa(lista_de_tarefas, lista_temp)
    #     listar_tarefas(lista_de_tarefas)
        
    # elif string == 'refazer':
    #     refazer_tarefa(lista_de_tarefas, lista_temp)
    #     listar_tarefas(lista_de_tarefas)
       
    # elif string == 'clear':
    #     os.system('cls')

    # else:
    #     adicona_tarefas(string, lista_de_tarefas)
    #     listar_tarefas(lista_de_tarefas)