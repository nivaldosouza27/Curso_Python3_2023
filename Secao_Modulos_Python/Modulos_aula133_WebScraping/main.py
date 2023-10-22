import requests
from bs4 import BeautifulSoup

url = 'https://www.uol.com.br/'
response = requests.get(url)
raw_html = response.text
parsed_html = BeautifulSoup(raw_html, 'html.parser')

# print(parsed_html.title.text)

titulo_materia = parsed_html.select('#lnjmf6mz')

print(titulo_materia)
