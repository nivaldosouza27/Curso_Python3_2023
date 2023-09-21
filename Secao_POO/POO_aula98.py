class Ponto:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        class_name = type(self).__name__
        return f'{class_name}(x={self.x}, y={self.y})'

    def __add__(self, other):
        novo_x = self.x + other.x
        novo_y = self.y + other.y
        return Ponto(novo_x, novo_y)
    
    def __gt__(self, other):
        resultado_self = self.x + self.y
        resultado_other = other.x + other.y
        return resultado_self > resultado_other

p1 = Ponto(4,2) 
p2 = Ponto(6,4)
p3 = p1 + p2
print(repr(p1))
print(p2)
print(p3)