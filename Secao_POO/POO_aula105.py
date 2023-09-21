# dataclasses - O que são dataclasses?
# O módulo dataclasses fornece um decorador e funções para criar métodos como
# __init__(), __repr__(), __eq__() (entre outros) em classes definidas pelo
# usuário.
# Em resumo: dataclasses são syntax sugar para criar classes normais.
# Foi descrito na PEP 557 e adicionado na versão 3.7 do Python.
# doc: https://docs.python.org/3/library/dataclasses.html
from dataclasses import dataclass, asdict


@dataclass
class Pessoa:
    nome: str
    sobrenome: str
    idade: int = 0

    def __post_init__(self):
        print('Post Init')

    @property
    def nome_completo(self):
        return f'{self.nome} {self.sobrenome}'

    @nome_completo.setter
    def nome_completo(self, valor):
        nome, sobrenome = valor.split()
        self.nome = nome
        self.sobrenome = sobrenome


if __name__ == '__main__':
    p1 = Pessoa('Luiz', 'Otavio')
    p1.nome_completo = 'Maria Helena'
    print(p1)
    print(asdict(p1))
    print(p1.nome_completo)
