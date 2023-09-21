# Enviando email SMTP com Python

import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from pathlib import Path
from string import Template
from dotenv import load_dotenv

load_dotenv()


# Caminho Arquivo HTML
CAMINHO_HTML = Path(__file__).parent / 'aula129.html'


# Dados do Remetente e Destinatario
remetente = os.getenv('FROM_EMAIL', '')
destinatario = remetente
assunto_email = 'Assunto Privado'


# Configurações SMTP
smtp_server = os.getenv('SMTP_SERVER', '')
smtp_username = os.getenv('FROM_EMAIL', '')
smtp_password = os.getenv('EMAIL_PASSWORD', '')
smtp_port = 587


# Mensagem do Email
with open(CAMINHO_HTML, 'r', encoding='utf-8') as arquivo:
    texto_arquivo = arquivo.read()
    template = Template(texto_arquivo)
    texto_email = template.substitute(nome='Nivaldo')


# Transformar a mensagem em MIMEMultipart
mime_multipart = MIMEMultipart()
mime_multipart['from'] = remetente
mime_multipart['to'] = destinatario
mime_multipart['subject'] = assunto_email

corpo_email = MIMEText(texto_email, 'html', 'utf-8')
mime_multipart.attach(corpo_email)

# Envia o email
with smtplib.SMTP(smtp_server, smtp_port) as server:
    server.ehlo()
    server.starttls()
    server.login(smtp_username, smtp_password)
    server.send_message(mime_multipart)
    print('Email enviado com sucesso!!')
