from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QPushButton, QComboBox, QMainWindow, QLineEdit
from PyQt5 import QtCore, QtGui
import pandas as pd
import sys


class Converter(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        tab = pd.read_html("https://myfin.by/currency/minsk")
        result = tab[0]
        lst = result.values
        self.usd = lst[0][3]
        self.eur = lst[1][3]
        self.rub = lst[2][3]
        self.pln = lst[3][3]
        self.byn = 1

    def initUI(self):
        self.setGeometry(0, 300, 380, 440)
        self.setWindowTitle('Converter')
        pal = self.palette()
        pal.setColor(QtGui.QPalette.Normal, QtGui.QPalette.Window, QtGui.QColor('#2d303a'))
        self.setPalette(pal)

        self.amount = QLabel(self)
        self.amount.setText(' Enter the amount')
        self.amount.setStyleSheet('''background-color: #2c3c7a; color: #e0e3f0; font-size: 25px;''')
        self.amount.setGeometry(10, 20, 210, 50)

        self.lbl_am = QLineEdit(self)
        self.lbl_am.setText(' ')
        self.lbl_am.setStyleSheet('''background-color: #cfd1dc; color: #180e2f; font-size: 30px;''')
        self.lbl_am.setGeometry(230, 20, 130, 50)
        self.move(500, 50)

        self.base = QComboBox(self)
        self.base.addItems([' Base', ' USD ', ' EUR ', ' RUB ', ' PLN ', ' BYN '])
        self.base.setStyleSheet('''background-color: #2c3c7a; color: #e0e3f0; font-size: 25px;''')
        self.base.move(10, 90)

        self.lbl_base = QLabel(self)
        self.lbl_base.setText('0')
        self.lbl_base.setStyleSheet('''background-color: #76777c; color: #180e2f; font-size: 30px;''')
        self.lbl_base.setGeometry(130, 80, 230, 50)

        self.exchange_1 = QLabel(self)
        self.exchange_1.setText('')
        self.exchange_1.setStyleSheet('''background-color: #76777c; color: #180e2f; font-size: 30px;''')
        self.exchange_1.setGeometry(10, 140, 100, 50)

        self.label_1 = QLabel(self)
        self.label_1.setText('0')
        self.label_1.setStyleSheet('''background-color: #76777c; color: #180e2f; font-size: 30px;''')
        self.label_1.setGeometry(130, 140, 230, 50)

        self.exchange_2 = QLabel(self)
        self.exchange_2.setText('')
        self.exchange_2.setStyleSheet('''background-color: #76777c; color: #180e2f; font-size: 30px;''')
        self.exchange_2.setGeometry(10, 200, 100, 50)

        self.label_2 = QLabel(self)
        self.label_2.setText('0')
        self.label_2.setStyleSheet('''background-color: #76777c; color: #180e2f; font-size: 30px;''')
        self.label_2.setGeometry(130, 200, 230, 50)

        self.exchange_3 = QLabel(self)
        self.exchange_3.setText('')
        self.exchange_3.setStyleSheet('''background-color: #76777c; color: #180e2f; font-size: 30px;''')
        self.exchange_3.setGeometry(10, 260, 100, 50)

        self.label_3 = QLabel(self)
        self.label_3.setText('0')
        self.label_3.setStyleSheet('''background-color: #76777c; color: #180e2f; font-size: 30px;''')
        self.label_3.setGeometry(130, 260, 230, 50)

        self.exchange_4 = QLabel(self)
        self.exchange_4.setText('')
        self.exchange_4.setStyleSheet('''background-color: #76777c; color: #180e2f; font-size: 30px;''')
        self.exchange_4.setGeometry(10, 320, 100, 50)

        self.label_4 = QLabel(self)
        self.label_4.setText('0')
        self.label_4.setStyleSheet('''background-color: #76777c; color: #180e2f; font-size: 30px;''')
        self.label_4.setGeometry(130, 320, 230, 50)

        self.lbl_am.returnPressed.connect(self.enter_amount)
        self.base.activated.connect(self.choice)

    def choice(self):
        self.base_list = [' USD ', ' EUR ', ' RUB ', ' PLN ', ' BYN ']
        text = self.base.currentText()
        if text != ' Base':
            if text == ' USD ':
                self.choice_base = self.usd
            elif text == ' EUR ':
                self.choice_base = self.eur
            elif text == ' RUB ':
                self.choice_base = self.rub / 100
            elif text == ' PLN ':
                self.choice_base = self.pln / 10
            elif text == ' BYN ':
                self.choice_base = self.byn
            elif text == ' Base':
                self.choice_base = 0
            self.base_list.remove(text)
            self.exchange_1.setText(self.base_list[0])
            self.exchange_2.setText(self.base_list[1])
            self.exchange_3.setText(self.base_list[2])
            self.exchange_4.setText(self.base_list[3])
        else:
            self.choice_base = 0
            self.base_list.remove(' BYN ')
            self.exchange_1.setText(self.base_list[0])
            self.exchange_2.setText(self.base_list[1])
            self.exchange_3.setText(self.base_list[2])
            self.exchange_4.setText(self.base_list[3])
        if len(self.lbl_am.text()) > 1:
            self.calculation(self.lbl_am.text())

    def enter_amount(self):
        self.lbl_base.setText(self.lbl_am.text())
        if self.exchange_1.text() != '':
            self.calculation(self.lbl_am.text())
        else:
            self.base.activated.connect(self.choice)

    def calculation(self, summa):
        self.ex_dict = {self.exchange_1.text(): self.label_1,
                        self.exchange_2.text(): self.label_2,
                        self.exchange_3.text(): self.label_3,
                        self.exchange_4.text(): self.label_4}
        for key, val in self.ex_dict.items():
            if key == ' EUR ':
                res_eur = round((self.choice_base / self.eur * float(summa)), 2)
                val.setText(str(res_eur))
            elif key == ' USD ':
                res_usd = round((self.choice_base / self.usd * float(summa)), 2)
                val.setText(str(res_usd))
            elif key == ' PLN ':
                res_pln = round((self.choice_base / self.pln * float(summa) * 10), 2)
                val.setText(str(res_pln))
            elif key == ' RUB ':
                res_rub = round((self.choice_base / self.rub * float(summa) * 100), 2)
                val.setText(str(res_rub))
            elif key == ' BYN ':
                res_byn = round((self.choice_base * float(summa)), 2)
                val.setText(str(res_byn))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Converter()
    ex.show()
    sys.exit(app.exec())
