from typing import Any


class Multiplicar:
    def __init__(self, multiplicador) -> None:
        self._multiplicador = multiplicador

    def __call__(self, func):
        def interna(*args, **kwargs):
            resultado = func(*args, **kwargs)
            multiplica = resultado * self._multiplicador
            return f'A multiplicacao é: {multiplica}'
        return interna

@Multiplicar(10)
def soma(x,y):
    resultado = x + y
    print('Soma é:', resultado)
    return resultado


teste1 = soma(2,8)
print(teste1)