# pessoa = {
#     'nome': 'Nivaldo',
#     'sobrenome': 'Souza',
# }

# (a1,a2), (b1,b2) = pessoa.items()

# print(a1,a2)
# print(b1,b2)

# for chave, valor in pessoa.items():
#     print(chave, valor)

pessoa = {
    'nome': 'Nivaldo',
    'sobrenome': 'Souza',
}

dados_pessoa = {
    'idade': 16,
    'altura': 1.60,
}

pessoa_completa = {**pessoa, **dados_pessoa}


def mostro_argumentos_nomeados(*args, **kwargs):
    for chave,valor in kwargs.items():
        print(chave, valor)

mostro_argumentos_nomeados()