## percorrendo uma lista e mostrando na tela

lista = ['Maria','Helena', 'Luiz', 'Nivaldo', 'Souza', 'Martins']

for nome in lista:
    indice = lista.index(nome)
    print(f'"{indice}" - "{nome}"')