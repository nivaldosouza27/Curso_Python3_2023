try:
    print('abrir arquivo')
    45/0
except ZeroDivisionError as erro:
     print(erro)
except IndexError as erro:
     print(erro)
except NameError as erro:
     print(erro)
else:
     print('Não deu certo')
finally:
    print('fechar arquivo')