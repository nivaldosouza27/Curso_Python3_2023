pessoa = {
    'nome': 'Nivaldo',
    'sobrenome': 'Souza',
}

# Apaga um item do dicionario com a chave especificada
nome = pessoa.pop('nome') 
print(nome)
print(pessoa)

#Apaga o ultimo item adicionado no dicionario
ultima_chave = pessoa.popitem() 
print (ultima_chave)
print(pessoa)

#Atualiza os dados do dicionario com outro dicionario
pessoa.update({     
    'nome': 'Karoline',
    'sobrenome': 'Rafaela',
    'idade': 24
})

#update com parametros nomeados
pessoa.update(nome='Karoline', idade= 30) 
print(pessoa)

#update com parametros dentro de iteraveis
tupla = ('nome', 'Karoline'), ('sobrenome', 'Rafaela'), ('idade', 30)
lista = ['nome', 'Karoline'], ['sobrenome', 'Rafaela'], ['idade', 30]
pessoa.update(lista)
pessoa.update(tupla)
print(pessoa)