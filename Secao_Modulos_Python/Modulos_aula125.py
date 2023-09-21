# random tem geradores de números pseudoaleatórios
# Obs.: números pseudoaleatórios significa que os números
# parecem ser aleatórios, mas na verdade não são. Portanto,
# este módulo não deve ser usado para segurança ou uso criptográfico.
# O motivo disso é que quando temos uma mesma entrada e um mesmo algorítimo,
# a saída pode ser previsível.
# doc: https://docs.python.org/pt-br/3/library/random.html

import random
import time

# Valor que inicia a aleatoreidade do modulo
# por padrão são usados os microsegundos da hora atual
aleatorio = random.seed(time.time())
print(f'Esse é o seed: {time.time()}')

aleatorio = random.seed()
print(f'Esse é o seed: {aleatorio}')

# Gera um numero aleatorio em uma intervalo especifico com passo
numero = random.randrange(10, 20, 2)
print(numero)

# Gera um numero aleatorio em uma intervalo especifico sem passo
numero_2 = random.randint(10, 20)
print(numero_2)

# Gera um numero aleatorio de float intervalo especifico sem passo
numero_3 = random.uniform(10, 20)
print(numero_3)

# Gera um metodo para embaralhar uma lista
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
           11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
random.shuffle(numeros)
print(numeros)

# Retirar trechos de valores aleatorios de uma lista(não repete)
novos_nomes = random.sample(numeros, k=2)
print(novos_nomes)

# Retirar trechos de valores aleatorios de uma lista(repete)
novos_nomes = random.choices(numeros, k=2)
print(novos_nomes)

# Retira um valor aleatorio de uma lista
print(random.choice(numeros))
