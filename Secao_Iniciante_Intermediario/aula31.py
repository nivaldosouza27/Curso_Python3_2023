### Gerador de CPF ###

import random

cpf_digitado_validado = ''
for i in range(9):
        cpf_digitado_validado += str(random.randint(0,9))
lista_soma = [10,9,8,7,6,5,4,3,2]
lista_percorrer = [0,1,2,3,4,5,6,7,8]
cpf_first_10 = cpf_digitado_validado
lista_soma_2 = [11,10,9,8,7,6,5,4,3,2]
lista_percorrer_2 = [0,1,2,3,4,5,6,7,8,9]

for percorre_cpf in lista_percorrer:
    if percorre_cpf == 0:
        soma_cpf_firt_9 = int(cpf_digitado_validado[percorre_cpf]) * lista_soma[percorre_cpf]
        soma_total = soma_cpf_firt_9
        percorre_cpf += 1
        soma_cpf_firt_9 = 0
    else:
        soma_cpf_firt_9 = int(cpf_digitado_validado[percorre_cpf]) * lista_soma[percorre_cpf]
        soma_total = soma_total + soma_cpf_firt_9
        percorre_cpf += 1
        soma_cpf_firt_9 = 0
resultado_digito_1 = (soma_total * 10) % 11

if resultado_digito_1 > 9:
    valida_digito_1 = 0
else:
    valida_digito_1 = resultado_digito_1

cpf_first_10 = cpf_digitado_validado+str(valida_digito_1)
soma_total_2 = 0

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

print(f'Seu CPF Gerado é: {cpf_digitado_validado}{valida_digito_1}{valida_digito_2}')