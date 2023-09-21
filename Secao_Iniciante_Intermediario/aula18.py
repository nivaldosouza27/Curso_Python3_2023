primeiro_nome = input("Digite o seu primeiro nome: ")
tamanho_nome = len(primeiro_nome)

if tamanho_nome > 1:
    if tamanho_nome <= 4:
        print('Seu nome é curto')
    elif tamanho_nome >= 5 and tamanho_nome <= 6:
        print('Seu nome é normal')
    elif tamanho_nome > 6:
        print('Seu nome é grande')
else:
    print("Digite mais de uma letra")