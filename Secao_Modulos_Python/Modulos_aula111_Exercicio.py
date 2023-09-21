# Exercício solucionado: calculando as datas e parcelas de um empréstimo
# Maria pegou um empréstimo de 1.000.000
# para realizar o pagamento em 5 anos.
# A data em que ela pegou o empréstimo foi
# 20/12/2020 e o vencimento de cada parcela
# é no dia 20 de cada mês.
# - Crie a data do empréstimo
# - Crie a data do final do empréstimo
# - Mostre todas as datas de vencimento e o valor de cada parcela

from datetime import datetime
from dateutil.relativedelta import relativedelta
import locale

locale.setlocale(locale.LC_ALL, 'pt_BR.utf8')

valor_emprestimo = 1000000
qtde_parcelas = 12
taxa_juros_mensal = 0.03
juros_mensal = valor_emprestimo * taxa_juros_mensal
valor_parcela_sem_juros = valor_emprestimo / qtde_parcelas
valor_parcela_juros = valor_parcela_sem_juros + juros_mensal
valor_total_emprestimo = valor_parcela_juros * qtde_parcelas
contador_parcelas = 1
data_inicial = datetime.now()
delta_pagamento = relativedelta(months=qtde_parcelas)
data_final = data_inicial + delta_pagamento


def mostrar_parcela():
    return print(
        f'Parcela: {contador_parcelas} - Vencimento: {data_formatada} \
- Valor Parcela: {valor_parcela_juros:,.2f}'
    )


print('\n')
print(f'Valor do Emprestimo: R${valor_emprestimo:,.2f}', end='\n')
print('-------------------')
print(f'Quantidade de Parcelas: {qtde_parcelas}', end='\n')
print('-------------------')
print(f'Valor parcela sem juros: R${valor_parcela_sem_juros:,.2f}', end='\n')
print('-------------------')
print(f'Valor juros por parcela: R${juros_mensal:,.2f}', end='\n')
print('-------------------')
print(f'Valor parcela com juros: R${valor_parcela_juros:,.2f}', end='\n')
print('-------------------')
print(f'Valor total do Emprestimo: R${valor_total_emprestimo:,.2f}', end='\n')
print('-------------------')
print('\n')

while data_inicial < data_final:
    data_formatada = data_inicial.strftime('%d/%m/%Y')
    mostrar_parcela()
    data_inicial += relativedelta(months=1)
    contador_parcelas += 1
