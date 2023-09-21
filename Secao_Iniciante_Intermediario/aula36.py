
def criar_multiplicador(multiplicador):
   def multiplicar(numero):
      return numero * multiplicador
   return multiplicar


duplicado = criar_multiplicador(2)
triplicado = criar_multiplicador(3)
quadruplicado = criar_multiplicador(4)

print(f'{duplicado(2)} {triplicado(2)} {quadruplicado(2)}')
