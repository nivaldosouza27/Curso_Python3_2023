## Função MUltiplica Numeros ###

def multiplica_args(*args):
    total = 1
    for numero in args:
        total *= numero
    return total

multiplicacao = multiplica_args(1,2,3,4,5)

print(multiplicacao)