pessoa = {}

chave = 'nome_completo'
chave2 = 'sobrenome'
pessoa[chave] = 'Nivaldo de Souza'
pessoa[chave2] = 'Martins'


if pessoa.get(chave2) is None:
    print("Chave não existe")
else:
    print(f'{pessoa[chave]} {pessoa[chave2]}')