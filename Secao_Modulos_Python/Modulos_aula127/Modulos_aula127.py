# import json
import string
import locale
from datetime import datetime
from pathlib import Path

CAMINHO_ARQUIVO = Path(__file__).parent / 'texto.txt'

locale.setlocale(locale.LC_ALL, '')


def converte_para_brl(numero: float) -> str:
    brl = 'R$ ' + locale.currency(numero, symbol=False, grouping=True)
    return brl


data = datetime(2023, 12, 28)
dados = dict(
    nome='João',
    valor=converte_para_brl(1_234_567),
    data=data.strftime('%d/%m/%Y'),
    empresa='N.S Informatica',
    telefone='+55 (34) 99950-9589'
)

# print(json.dumps(dados, indent=2, ensure_ascii=False))

with open(CAMINHO_ARQUIVO, 'r', encoding='utf-8') as arquivo:
    texto = arquivo.read()
    template = string.Template(texto)
    print(template.substitute(dados))
