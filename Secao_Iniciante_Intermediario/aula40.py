### Sistema de Perguntas e Respostas ####
import os

perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4'
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25'
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5'
    },
     {
        'Pergunta': 'Quanto é 20*9?',
        'Opções': ['160', '150', '160', '180'],
        'Resposta': '180'
    },
]

contador = 0
cont_acertos = 0
while contador < len(perguntas):

    chaves_dict = list(perguntas[contador].keys())
    values_dict = list(perguntas[contador].values())
    opcoes_dict = list(values_dict[1])
    resposta_dict = values_dict[2]
    
    print(f'{chaves_dict[0]} {contador+1}: {values_dict[0]}')
    print()
    print(f'{chaves_dict[1]}:')
    contador += 1

    for indice in enumerate(opcoes_dict):
        print(f'{indice[0]}) {indice[1]}')
        if indice[1] == resposta_dict:
            resposta_certa = indice[0]
    
    escolha_usuario = input("Escolha uma opção: ")
    escolha_usuario_digit = escolha_usuario.isdigit()
    os.system('cls')

    if  escolha_usuario_digit and (int(escolha_usuario) == resposta_certa):
        print("Voce Acertou!👏")
        cont_acertos += 1
    else:
        print("Voce errou!❌")

os.system('cls')
print("Parabens, Voce finalizou o Quiz:")
print(f"Voce acertou: {cont_acertos} de {len(perguntas)} questões")