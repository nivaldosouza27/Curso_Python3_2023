class Pessoa:
    def __init__(self, nome, sobrenome) -> None:
        self.nome = nome
        self.sobrenome = sobrenome

class Cliente(Pessoa):
    ...

c1 =  Cliente('Nivaldo', 'Souza')
print(c1.nome, c1.sobrenome)