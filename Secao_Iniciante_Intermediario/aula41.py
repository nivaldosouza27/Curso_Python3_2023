## Conjuntos em Pyhton ###

import random

set_1 = set()
set_2 = set()

for i in range(5):
    numero = random.randrange(1,20)
    set_1.add(numero)
for i in range(5):
    numero = random.randrange(1,20)
    set_2.add(numero)

set_3 = set_1 | set_2
set_4 = set_1 & set_2
set_5 = set_1 - set_2
set_6 = set_1 ^ set_2


print(f'Primeiro set:             {set_1}')
print(f'Segundo set:              {set_2}')
print(f'Set União:                {set_3}')
print(f'Set Repete Intersecção:   {set_4}')
print(f'Set Somente Esquerda:     {set_5}')
print(f'Set Diferença Simetrica:  {set_6}')


