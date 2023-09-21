####ordenando uma lista aleatoria de inteiros####

# import random

# lista = []
# for i in range(10):
#     numero = random.randint(1,20)
#     lista.append(numero)
# lista.sort()
# print(lista)



### ordenando uma lista de dicionarios de stringg atraves de funções #######

lista = [
    {'nome': 'Nivaldo',  'sobrenome':   'Souza'},
    {'nome': 'Ana',      'sobrenome':   'Lucia'},
    {'nome': 'João',     'sobrenome':   'Martins'},
    {'nome': 'Maria',    'sobrenome':   'Ribeiro'},
    {'nome': 'José',     'sobrenome':   'Antonio'},
    {'nome': 'Pedro',    'sobrenome':   'Lazaro'},
]

def exibir_lista (lista):
    for item in lista:
        print(item)
    print()

lista_01 = sorted(lista, key=lambda item: item['nome'])
lista_02 = sorted(lista, key=lambda item: item['sobrenome'])

exibir_lista(lista_01)
exibir_lista(lista_02)



