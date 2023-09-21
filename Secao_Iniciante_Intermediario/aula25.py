## Jogo da Palavra secreta ##

import os

key_word = "joao"
size_key_word = len(key_word)
letras_acertadas = ''
numero_tentativas = 0

print(f'####### BEM VINDO AO JOGO DA PALAVRA SECRETA ######')
print()
print(f'SUA PALAVRA CHAVE CONTÉM {size_key_word} LETRAS')
print()
print(f'PALAVRA-CHAVE: {size_key_word * " * "}')
print()

while True:
    
    letra_digitada = input("DIGITE UMA LETRA: ")
    numero_tentativas += 1

    if len(letra_digitada) > 1:
        print("Digite apenas uma Letra")
        continue
    
    if letra_digitada in key_word:
        letras_acertadas += letra_digitada
    
    palavra_formada = ''
    for letra_secreta in key_word:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'
    print(f'PALAVRA-CHAVE: {palavra_formada}')
    
    if palavra_formada == key_word:
        os.system('cls')
        print('Voce Acertou!!')
        print(f'A palavra secreta era {key_word}')
        print('Numero de Tentativas: ', numero_tentativas)
        letras_acertadas = ''
        numero_tentativas = 0
        