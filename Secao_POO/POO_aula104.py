import enum

Direcoes = enum.Enum('Direcoes', ['ESQUERDA', 'DIREITA'])
print(Direcoes(1), Direcoes['ESQUERDA'], Direcoes.ESQUERDA)


def mover(direcao: Direcoes):
    if not isinstance(direcao, Direcoes):
        raise ValueError('Direcao não encontrada')
    print(f'Movendo para {direcao}')


mover(Direcoes.DIREITA)
mover(Direcoes.ESQUERDA)
mover('lado')
