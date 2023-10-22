# QApplication e QPushButton de PySide6.QtWidgets
# QApplication -> O Widget principal da aplicação
# QPushButton -> Um botão
# PySide6.QtWidgets -> Onde estão os widgets do PySide6

import sys
from PySide6.QtWidgets import (QApplication, QPushButton, QWidget, QGridLayout,
                               QMainWindow)
from PySide6.QtCore import Slot

# Iniciando a aplicação
app = QApplication(sys.argv)
window = QMainWindow()
central_widget = QWidget()
central_widget.setStyleSheet('background: black')
window.setCentralWidget(central_widget)

# Estilizando a minha windows principal
window.setWindowTitle('Minha Janela Bonita')


# Criando um widget do tipo botao
botao1 = QPushButton('Botao1')
botao1.setStyleSheet('font-size: 40px; color:white; background: grey')

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
layout.addWidget(botao1, 1, 1)
layout.addWidget(botao2, 2, 1)
layout.addWidget(botao3, 3, 1)


# Função que aparece no menu
@Slot()
def slot_example(status_bar):
    status_bar.showMessage('O meu slot foi executado')


@Slot()
def other_slot(checked):
    print('Está Marcado?', checked)


@Slot()
def thrid_slot(action):
    def inner():
        other_slot(action.isChecked())
    return inner


# Status Bar
status_bar = window.statusBar()
status_bar.showMessage('Mostar Mensagem')

# Menu Bar
menu = window.menuBar()
first_menu = menu.addMenu('Qualquer coisa')
first_action = first_menu.addAction('Primeira Ação')
first_action.triggered.connect(lambda: slot_example(status_bar))

# Segundo Menu
second_action = first_menu.addAction('Segunda Ação')
second_action.setCheckable(True)
second_action.toggled.connect(other_slot)
second_action.hovered.connect(thrid_slot(second_action))

botao1.clicked.connect(thrid_slot(second_action))


# Exibindo o main window da aplicação
window.show()

# executando o loop da aplicacao
app.exec()
