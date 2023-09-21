import json

CAMINHO_ARQUIVO = 'POO_aula81_bd.json'

class Pessoa:
    def __init__(self, nome, sobrenome, idade, altura):
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade
        self.altura = altura

p1 = Pessoa('Nivaldo', 'Souza', 25, 1.88 )
p2 = Pessoa('Karoline', 'Rafaela', 24, 1.75 )
p3 = Pessoa('Heitor', 'Martins', 1, 0.75 )
p4 = Pessoa('Maria Liz', 'Martins', 1, 0.75 )
bd = [vars(p1), vars(p2), vars(p3), vars(p4)]

with open(CAMINHO_ARQUIVO, 'w', encoding='utf8') as arquivo:
    json.dump(bd, arquivo, indent=2, ensure_ascii=False)


