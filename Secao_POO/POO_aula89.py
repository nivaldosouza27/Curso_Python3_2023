### Composição de Objetos ####

# Relações entre classes: associação, agregação e composição
# Composição é uma especialização da agregação.
# Mas nela, quando o objeto "pai" for apagado, todas
# as referências dos objetos filhos também são
# apagadas.

class Cliente:
    def __init__(self, nome) -> None:
        self.nome = nome
        self.enderecos = []

    def inserir_enderecos(self, rua, numero):
        self.enderecos.append(Endereco(rua, numero))
    
    def listar_enderecos(self):
        for endereco in self.enderecos:
            print(f'Endereços: {endereco.rua}-{endereco.numero}')
    
    def listar_clientes(self):
        for endereco in self.enderecos:
            endereco = endereco
        print(f'Nome: {self.nome}\nEndereço: {endereco.rua}-{endereco.numero}')
           
class Endereco:
    def __init__(self, rua, numero) -> None:
        self.rua = rua
        self.numero =  numero


c1 = Cliente('Nivaldo de Souza Martins')
c1.inserir_enderecos('Rua de Pedra', 5000)
c1.listar_clientes()
print()
c2 = Cliente('Karoline Rafaela Fonseca Ramos')
c2.inserir_enderecos('Rua de Pedra', 400)
c2.listar_clientes()