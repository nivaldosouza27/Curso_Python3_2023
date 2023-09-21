#### Valida CPF ####
import re
import os

while True:
    cpf_digitado = input ("Digite os 11 digitos seu CPF: ")
    os.system('cls')
    entrada_sequencial = cpf_digitado == cpf_digitado[0] * len(cpf_digitado)
    cpf_digitado_validado = re.sub (r'[^0-9]','', cpf_digitado)

    if len(cpf_digitado_validado) == 11 and (entrada_sequencial is False):
        print(f"Seu CPF é: {cpf_digitado_validado}")
        cpf_first_9 = cpf_digitado_validado[0:9]
        lista_soma = [10,9,8,7,6,5,4,3,2]
        lista_percorrer = [0,1,2,3,4,5,6,7,8]
        cpf_first_10 = cpf_digitado_validado[0:10]
        lista_soma_2 = [11,10,9,8,7,6,5,4,3,2]
        lista_percorrer_2 = [0,1,2,3,4,5,6,7,8,9]

        for percorre_cpf in lista_percorrer:
            if percorre_cpf == 0:
                soma_cpf_firt_9 = int(cpf_first_9[percorre_cpf]) * lista_soma[percorre_cpf]
                soma_total = soma_cpf_firt_9
                percorre_cpf += 1
                soma_cpf_firt_9 = 0
            else:
                soma_cpf_firt_9 = int(cpf_first_9[percorre_cpf]) * lista_soma[percorre_cpf]
                soma_total = soma_total + soma_cpf_firt_9
                percorre_cpf += 1
                soma_cpf_firt_9 = 0
        resultado_digito_1 = (soma_total * 10) % 11

        if resultado_digito_1 > 9:
            valida_digito_1 = 0
        else:
            valida_digito_1 = resultado_digito_1

        for percorre_cpf_2 in lista_percorrer_2:
            if percorre_cpf_2 == 0:
                soma_cpf_firts_10 = int(cpf_first_10[percorre_cpf_2]) * lista_soma_2[percorre_cpf_2]
                soma_total_2 = soma_cpf_firts_10
                percorre_cpf_2 += 1
                soma_cpf_firts_10 = 0
            else:
                soma_cpf_firts_10 = int(cpf_first_10[percorre_cpf_2]) * lista_soma_2[percorre_cpf_2]
                soma_total_2 = soma_total_2 + soma_cpf_firts_10
                percorre_cpf_2 += 1
                soma_cpf_firts_10 = 0
        resultado_digito_2 = (soma_total_2 * 10) % 11

        if resultado_digito_2 > 9:
            valida_digito_2 = 0
        else:
            valida_digito_2 = resultado_digito_2

        if (valida_digito_1 == int(cpf_digitado_validado[9])) and (valida_digito_2 == int(cpf_digitado_validado[10])):
            print("Seu CPF é valido")
        else:
            print("Seu CPF não é valido!")

    else:
        print(f"Seu CPF é: {cpf_digitado}")
        print('CPF Invalido! Digite um CPF 11 digitos válido:')
    
