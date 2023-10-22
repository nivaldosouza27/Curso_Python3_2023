import os
import pymysql
import dotenv
import random
from faker import Faker

dotenv.load_dotenv()

connection = pymysql.connect(
    host=os.environ['MYSQL_HOST'],
    user=os.environ['MYSQL_USER'],
    password=os.environ['MYSQL_PASSWORD'],
    database=os.environ['MYSQL_DATABASE'],
    cursorclass=pymysql.cursors.DictCursor
)

with connection:
    with connection.cursor() as cursor:
        sql = '''
        CREATE TABLE IF NOT EXISTS customers (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nome VARCHAR(50),
            idade INT
        )
        '''
        cursor.execute(sql)
    connection.commit()

    with connection.cursor() as cursor:
        deletando_tabela_sql = 'DELETE FROM customers'
        cursor.execute(deletando_tabela_sql)

        fake = Faker()
        for rand in range(10):
            nome = fake.name()
            idade = random.randint(18, 65)
            # print(f'Nome: {nome}, Idade:{idade}')

            inserir_dados_sql = f"INSERT INTO customers (nome, idade) \
                VALUES ('{nome}', {idade})"
            cursor.execute(inserir_dados_sql)
            # print(inserir_dados_sql)
    connection.commit()

    with connection.cursor() as cursor:
        sql = (
            'SELECT * FROM customers'
        )
        cursor.execute(sql)
        data5 = cursor.fetchall()

        for row in data5:
            print(row)
