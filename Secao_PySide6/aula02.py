# QApplication e QPushButton de PySide6.QtWidgets
# QApplication -> O Widget principal da aplicação
# QPushButton -> Um botão
# PySide6.QtWidgets -> Onde estão os widgets do PySide6

import sys
from PySide6.QtWidgets import (QApplication, QPushButton, QWidget, QGridLayout,
                               QMainWindow)
from PySide6.QtGui import QIcon

my_icon = QIcon()
my_icon.addFile('icon.jpg')

# Iniciando a aplicação
app = QApplication(sys.argv)
window = QMainWindow()
central_widget = QWidget()
central_widget.setStyleSheet('background: black')
window.setCentralWidget(central_widget)

# Estilizando a minha windows principal
window.setWindowTitle('Minha Janela Bonita')
window.setWindowIcon(my_icon)


# Criando um widget do tipo botao
botao = QPushButton('Botao1')
botao.setStyleSheet('font-size: 40px; color:white; background: grey')

# Criando um widget do tipo botao2
botao2 = QPushButton('Botao 2')
botao2.setStyleSheet('font-size: 40px; color:white; background: grey')

# Criando um widget do tipo botao2
botao3 = QPushButton('Botao 3')
botao3.setStyleSheet('font-size: 40px; color:white; background: grey')

# Criando uma layout para adicionar widgets na central
layout = QGridLayout()
central_widget.setLayout(layout)  # setando o layout na central

# adicionando um wiget(botao) no layout
layout.addWidget(botao, 1, 1)
layout.addWidget(botao2, 2, 1)
layout.addWidget(botao3, 3, 1)


# Função que aparece no menu
def slot_example(status_bar):
    status_bar.showMessage('O meu slot foi executado')


# Status Bar
status_bar = window.statusBar()
status_bar.showMessage('Mostar Mensagem')

# Menu Bar
menu = window.menuBar()
primeiro_menu = menu.addMenu('Qualquer coisa')
primeira_acao = primeiro_menu.addAction('Primeira Ação')
primeira_acao.triggered.connect(lambda: slot_example(status_bar))


# Exibindo o main window da aplicação
window.show()

# executando o loop da aplicacao
app.exec()
