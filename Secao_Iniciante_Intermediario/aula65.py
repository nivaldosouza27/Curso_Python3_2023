"""
Considerando duas listas de inteiros ou floats (lista A e lista B)
Some os valores nas listas retornando uma nova lista com os valores somados:
Se uma lista for maior que a outra, a soma só vai considerar o tamanho da
menor.
Exemplo:
lista_a     = [1, 2, 3, 4, 5, 6, 7]
lista_b     = [1, 2, 3, 4]
=================== resultado
lista_soma  = [2, 4, 6, 8]
"""

lista01 = [1, 2, 3, 4, 5, 6, 7,10,54,87,60,45]
lista02 = [1, 2, 3, 4, 40, 46, 27,15,57,61,50,99]
nova_lista = [x+y for x,y in list(zip(lista01,lista02))]

print(lista01)
print(lista02)
print(nova_lista)

    


