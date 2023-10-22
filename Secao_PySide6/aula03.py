# Trabalhando com classes e Heranças no PySide 6

import sys
from PySide6.QtWidgets import (QApplication, QPushButton, QWidget, QGridLayout,
                               QMainWindow)
from PySide6.QtCore import Slot


class MyWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Window Detail
        self.setWindowTitle('My First Window')

        # Central Widget
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.central_widget.setStyleSheet('background: grey')

        # Botão 1
        self.botao1 = self.make_buttom('Texto do Botão 1')
        self.botao1.clicked.connect(self.second_action_toggled)

        # Botão 2
        self.botao2 = self.make_buttom('Texto do Botão 2')

        # Botão 3
        self.botao3 = self.make_buttom('Texto do Botão 3')

        # Grid Layout
        self.grid_layout = QGridLayout()
        self.central_widget.setLayout(self.grid_layout)
        self.grid_layout.addWidget(self.botao1, 1, 1)
        self.grid_layout.addWidget(self.botao2, 2, 1)
        self.grid_layout.addWidget(self.botao3, 3, 1)

        # Status Bar
        self.status_bar = self.statusBar()
        self.status_bar.showMessage('Mostar Mensagem')

        # Menu Bar
        self.menu = self.menuBar()
        self.first_menu = self.menu.addMenu('Qualquer coisa')
        self.first_action = self.first_menu.addAction('Primeira Ação')
        self.first_action.triggered.connect(self.change_message_statusBar)

        # Segundo Menu
        self.second_action = self.first_menu.addAction('Segunda Ação')
        self.second_action.setCheckable(True)
        self.second_action.toggled.connect(self.second_action_toggled)
        self.second_action.hovered.connect(self.second_action_toggled)

    # Funções de Slot que aparece no menu
    @Slot()
    def change_message_statusBar(self):
        self.status_bar.showMessage('O meu slot foi executado')

    @Slot()
    def second_action_toggled(self):
        print('Está Marcado?', self.second_action.isChecked())

    def make_buttom(self, text):
        btn = QPushButton(text)
        btn.setStyleSheet(
            'font-size: 40px; color:white; background: grey')
        return btn


if __name__ == '__main__':
    # Criando a aplicação
    app = QApplication(sys.argv)

    # Instanciando e exibindo o main window da aplicação
    window = MyWindow()
    window.show()

    # executando o loop da aplicacao
    app.exec()
