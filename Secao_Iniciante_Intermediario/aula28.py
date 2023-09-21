######### LISTA DE COMPRAS While/IF/FOR ##########
import os

lista = []

while True:
    escolha_menu = input('Digite umas das opções para seguir: [i]Inserir [a]Apagar [l]Listar: ')
    
    if escolha_menu == "i":
        os.system('cls')
        if lista == []:
            escolha_inserir = input('Digite o item a ser adicionado: ')
            lista.append(escolha_inserir)
            print("Item adicionado com sucesso!!")
            print()
            print("Lista Atualizada")
            for nome in lista:
                indice = lista.index(nome)
                print(f'"{indice}" - "{nome}"')
        else:
            escolha_inserir = input('Digite o item a ser adicionado: ')
            lista.append(escolha_inserir)
            print("Item adicionado com sucesso!!")
            print()
            print("Lista Atualizada")
            for nome in lista:
                indice = lista.index(nome)
                print(f'"{indice}" - "{nome}"')
    
    elif escolha_menu == "a":
        os.system('cls')
        if lista == []:
            print("Não há itens na Lista")
        else:
            print("Lista Atual")
            print()
            for nome in lista:
                indice = lista.index(nome)
                print(f'"{indice}" - "{nome}"')
            try:
                indice_escolha_apagar = int(input("Escolha o indice de algum item para ser apagado: "))

                if indice_escolha_apagar < len(lista):
                    del lista[indice_escolha_apagar]
                    print("Item apagado com sucesso!!")
                    print()
                    print("Lista Atualizada")
                    for nome in lista:
                        indice = lista.index(nome)
                        print(f'"{indice}" - "{nome}"')
                else:
                    print("Indice fora dos limites da Lista!");
            except ValueError:
                print("Por favor digite um numero inteiro!");

    elif escolha_menu == "l":
        os.system('cls')
        if lista == []:
            print("Não há itens na Lista")
        else:
            print("Lista Atualizada")
            print()
            for nome in lista:
                indice = lista.index(nome)
                print(f'"{indice}" - "{nome}"')

    else:
        os.system('cls')
        print('Opção invalida!!')
    