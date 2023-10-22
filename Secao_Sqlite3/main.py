import sqlite3
from pathlib import Path

ROOT_DIR = Path(__file__).parent
DB_NAME = 'db.sqlite3'
DB_FILE = ROOT_DIR / DB_NAME
TABLE_NAME = 'customers'

connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

# Criando a tabela
cursor.execute(
    f'CREATE TABLE IF NOT EXISTS {TABLE_NAME}'
    '('
    'id INTEGER PRIMARY KEY AUTOINCREMENT,'
    'name TEXT,'
    'weight REAL'
    ')'
)
connection.commit()


# Deletando os arquivos da tabela
cursor.execute(
    f'DELETE FROM  {TABLE_NAME} '
)
connection.commit()


# Inserindo valores na tabela
sql = (
    f'INSERT INTO {TABLE_NAME} '
    '(name, weight)'
    'VALUES '
    '(?,?)'
)
# cursor.execute(sql, ['Nivaldo', 10])
cursor.executemany(
    sql,
    [
        ('Maria', 20),
        ('João', 10),
        ('Pedro', 15),
        ('Luiz', 60),
        ('Carlos', 52),
        ('Ana', 21),
    ]
)
connection.commit()


cursor.close()
connection.close()
