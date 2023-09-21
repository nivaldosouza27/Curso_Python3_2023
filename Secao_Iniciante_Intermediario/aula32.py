## Funções ##

lista_nomes = ['Helena', 'Maria', 'Jose', 'João', 'Pedro', 'Ricardo','Gabriel', 'Mariana', 'Carla', 'Barbara', 1, 2 ,3, 4]

def mensagem_texto (nome):
    print(f"Olá, {nome}")


for i in range(len(lista_nomes)):
    mensagem_texto (lista_nomes[i])