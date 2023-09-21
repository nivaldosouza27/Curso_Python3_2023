# Criando datas com módulo datetime
# datetime(ano, mês, dia)
# datetime(ano, mês, dia, horas, minutos, segundos)
# datetime.strptime('DATA', 'FORMATO')
# datetime.now()
# https://pt.wikipedia.org/wiki/Era_Unix
# datetime.fromtimestamp(Unix Timestamp)
# https://docs.python.org/3/library/datetime.html
# Para timezones
# https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
# Instalando o pytz
# pip install pytz types-pytz
# datetime.timedelta e dateutil.relativetimedelta (calculando datas)
# Docs:
# https://dateutil.readthedocs.io/en/stable/relativedelta.html
# https://docs.python.org/3/library/datetime.html#timedelta-objects

from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
from pytz import timezone


data_str = '2022-04-20 07:49:23'
data_str_fmt = '%Y-%m-%d %H:%M:%S'

# Formatando uma string no formato de datetime
data_formatada = datetime.strptime(data_str, data_str_fmt)

# Mostrando a data atual, com ou sem timezone
data_hoje = datetime.now(timezone('Asia/Tokyo'))
data_hoje = datetime.now()

# Mostrando uma data atraves de numeros inteiros como parametros
data_int = datetime(2022, 9, 30, 7, 30, 15)

# Mostrando o TimeStamp da data atual
data_stamp = datetime.now().timestamp()

# Mostrando a diferença entre duas datas retornando o TimeDelta
print(data_int < data_hoje)

# Adicionando valores de data usando o TimeDelta
delta = timedelta(days=10, hours=2, minutes=40, seconds=50, )
print(data_hoje + delta)

# Adicionando valores de data usando o Relative TimeDelta
delta_relative = relativedelta(seconds=60)
print(data_hoje + delta_relative)

# Comparando valores de duas datas usando o Relative TimeDelta
delta_compare = relativedelta(data_hoje, data_formatada)
print(delta_compare)
