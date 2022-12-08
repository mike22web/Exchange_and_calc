from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QPushButton, QComboBox, QMainWindow
from PyQt5 import QtCore, QtGui
import sys
from calculator import Calculator
from converter import Converter


class Start(QMainWindow):
    def __init__(self):
        super().__init__()

        self.button_1 = QPushButton('Exchange', self)
        self.button_1.setStyleSheet('''background-color: #2c3c7a; color: #e0e3f0; font-size: 25px;''')
        self.button_1.resize(150, 70)
        self.button_1.move(115, 100)

        self.button_2 = QPushButton('Calculator', self)
        self.button_2.setStyleSheet('''background-color: #2c3c7a; color: #e0e3f0; font-size: 25px;''')
        self.button_2.resize(150, 70)
        self.button_2.move(115, 190)

        self.button_1.clicked.connect(self.converter)
        self.button_2.clicked.connect(self.calculator)

        self.start_window()

    def start_window(self):
        self.setGeometry(0, 300, 380, 380)
        self.setWindowTitle('Start')
        pal = self.palette()
        pal.setColor(QtGui.QPalette.Normal, QtGui.QPalette.Window, QtGui.QColor('#2d303a'))
        self.setPalette(pal)
        self.move(500, 50)
        self.show()

    def calculator(self):
        self.calc = Calculator_2()
        self.calc.show()
        self.hide()

    def converter(self):
        self.change = Converter_2()
        self.change.show()
        self.hide()


class Converter_2(Converter):
    def __init__(self):
        super().__init__()

        self.button_menu = QPushButton('Main Menu', self)
        self.button_menu.setStyleSheet('''background-color: #572d84; color: #e0e3f0; font-size: 25px;''')
        self.button_menu.resize(150, 50)
        self.button_menu.move(210, 380)

        self.button_menu.clicked.connect(self.main_menu)

    def main_menu(self):
        self.menu = Start()
        self.menu.show()
        self.hide()


class Calculator_2(Calculator):
    def __init__(self):
        super().__init__()

        self.button_menu = QPushButton('Main menu', self)
        self.button_menu.setStyleSheet('''background-color: #572d84; color: #e0e3f0; font-size: 15px;''')
        self.button_menu.resize(85, 50)
        self.button_menu.move(285, 320)

        self.button_menu.clicked.connect(self.main_menu)

    def main_menu(self):
        self.menu = Start()
        self.menu.show()
        self.hide()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Start()
    ex.show()
    sys.exit(app.exec())
