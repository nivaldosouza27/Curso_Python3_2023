### Agregação de Objetos ####

# Relações entre classes: associação, agregação e composição
# Agregação é uma forma mais especializada de associação
# entre dois ou mais objetos. Cada objeto terá
# seu ciclo de vida independente.
# Geralmente é uma relação de um para muitos, onde um
# objeto tem um ou muitos objetos.
# Os objetos podem viver separadamente, mas pode
# se tratar de uma relação onde um objeto precisa de
# outro para fazer determinada tarefa.
# (existem controvérsias sobre as definições de agregação).


class Carrinho:
    def __init__(self) -> None:
        self._produtos = []

    def total(self):
        return print(sum([p.preco for p in self._produtos]))
    
    def inserir_produtos(self, *produtos):
        self._produtos.extend(produtos)

    def listar_produtos(self):
        print()
        for produto in self._produtos:
            print(produto.nome, produto.preco)
        print()

class Produto:
    def __init__(self, nome, preco) -> None:
        self.nome = nome
        self.preco = preco

carrinho = Carrinho()
p1 = Produto('Caneta', 1.50)
p2 = Produto('Lapis', 1.10)
p3 = Produto('Lapiseira', 6.50)

carrinho.inserir_produtos(p1,p2,p3)
carrinho.listar_produtos()
carrinho.total()