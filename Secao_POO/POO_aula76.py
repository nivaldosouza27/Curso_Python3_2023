class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

p1 = Pessoa('Nivaldo', 'Souza')
# p1.nome = 'Nivaldo'
# p1.sobrenome = 'Souza'

p2 = Pessoa('Karoline', 'Rafaela')
# p2.nome = 'Karoline'
# p2.sobrenome = 'Rafaela'


print(p1.nome)
print(p1.sobrenome)
print(p2.nome)
print(p2.sobrenome)

