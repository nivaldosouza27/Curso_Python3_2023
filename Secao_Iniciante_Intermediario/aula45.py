### Mapeamento de dados em List Comprehension #### Antes do For

produtos = [
    {'nome': 'p1', 'preco': 20},
    {'nome': 'p2', 'preco': 10},
    {'nome': 'p3', 'preco': 30},
]

novos_produtos = [
    {**produto, 'preco': produto['preco'] * 1.05}
    if produto['preco'] > 20 else {**produto}
    for produto in produtos
    if produto['preco'] > 10
]

## Filtros em List Comprehension ## Depois do For
lista = [n for n in range(10) if n < 5]
print(lista)
print(novos_produtos)