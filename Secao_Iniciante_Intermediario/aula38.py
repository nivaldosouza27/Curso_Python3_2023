import copy #biblioteca copy 

#definindo o dicionario
pessoa = {
    'nome': 'Nivaldo',
    'sobrenome': 'Souza',
    'idade': 25,
    'endereços': [
        "Rua Jeronimo Xavier",
        "Rua Ver. Pedro Ribeiro"
    ]
}

#quantidade de chaves no dicionario
print(len(pessoa)) 
# visualizar as chaves existentes
print(list(pessoa.keys())) 
#visualizar os valores de cada chave
print(list(pessoa.values())) 
#visualizar as chaves e os valores correspondentes
print(list(pessoa.items())) 
#definir um valor padrão a uma determinada chave, caso ela não tenha sido definida
print(pessoa.setdefault('Altura', 0)) 

# fazendo uma shallow copy ou copia rasa
pessoa2 = copy.copy(pessoa) 
pessoa2['nome'] = 'Nivaldinho'
pessoa2['endereços'] = ['Rua 1', 'Rua 2']

#fazendo uma deep copy ou copia profunda
pessoa3 = copy.deepcopy(pessoa) 
pessoa3['nome'] = 'Nivaldão'
pessoa3['endereços'] = ['Rua 3', 'Rua 4']

#imprimindo os valores das variaveis
print(f'Pessoa: {pessoa}')
print(f'Pessoa2: {pessoa2}')
print(f'Pessoa3: {pessoa3}')