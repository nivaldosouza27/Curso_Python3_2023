## Dictionary Comprehension #####

produto = {
    'nome': 'Caneta Azul',
    'preco': 2.5,
    'categoria': 'Escritorio',
}

for chave, valor in produto.items():
    print(chave, valor)


dc = {
    chave: valor.upper()
    if isinstance(valor, str) else valor
    for chave, valor in produto.items()
    if chave != 'categoria' 
}


print(dc)