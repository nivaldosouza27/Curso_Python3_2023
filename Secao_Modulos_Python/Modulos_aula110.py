# Formatando datas do datetime
# datetime.strftime('DATA', 'FORMATO')
# https://docs.python.org/3/library/datetime.html


from datetime import datetime

fmt = '%d/%m/%Y'

# Formatando a data com strftime retornando uma "STRING"
data = datetime.strptime('2022-12-13 05:50:50', '%Y-%m-%d %H:%M:%S')
data_formatada = data.strftime(fmt)
print(data_formatada)
