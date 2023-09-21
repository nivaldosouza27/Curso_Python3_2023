# secrets gera numeros aleatorios seguros

import string as s
from secrets import SystemRandom as sr

# Gerando uma senha com 12 caracteres aleatorios
list_random = ''.join(sr().choices(
    s.ascii_letters + s.digits + s.punctuation, k=64))

print(list_random)


random = sr()
# Gera um numero aleatorio em uma intervalo especifico com passo
numero = random.randrange(10, 20, 2)
print(numero)

# Gera um numero aleatorio em uma intervalo especifico sem passo
numero_2 = random.randint(10, 20)
print(numero_2)

# Gera um numero aleatorio de float intervalo especifico sem passo
numero_3 = random.uniform(10, 20)
print(numero_3)
