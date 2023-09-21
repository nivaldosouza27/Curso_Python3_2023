nome = input("Digite o seu nome completo: ")
tamanho_nome = len(nome)
contador = (len(nome) - len(nome))
 
print(f'Seu nome tem {tamanho_nome} caracteres')
print(f'Seu novo nome é:')

while (contador) < tamanho_nome:
    new_name = f'*{nome[contador]}'
    contador += 1
    print(new_name,end="")