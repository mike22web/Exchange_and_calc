from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QPushButton
from PyQt5 import QtCore, QtGui
import sys


class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.my_input = []
        self.operand_1 = []
        self.operand_2 = []
        self.operation = []
        self.memory = []
        self.memory_window()
        self.many_operation = []
        self.flag = False
        self.point_on = False
        self.memory_on = False

    def initUI(self):
        self.setGeometry(0, 300, 380, 380)
        self.setWindowTitle('My C@lculat0r :)')
        pal = self.palette()
        pal.setColor(QtGui.QPalette.Normal, QtGui.QPalette.Window, QtGui.QColor('#2d303a'))
        # pal.setColor(QtGui.QPalette.Inactive, QtGui.QPalette.Window, QtGui.QColor('#ff0000'))
        self.setPalette(pal)

        self.label = QLabel(self)
        self.label.setText('0')
        self.label.setStyleSheet('''background-color: #76777c; color: #180e2f; font-size: 29px;''')
        # self.label.resize(300, 75)
        self.label.setGeometry(10, 10, 360, 75)
        self.move(500, 50)

        self.label_mem = QLabel(self)
        self.label_mem.setText('')
        self.label_mem.setStyleSheet('''background-color: #76777c; color: #180e2f; font-size: 20px;''')
        # self.label.resize(300, 75)
        self.label_mem.setGeometry(10, 10, 30, 20)
        self.move(500, 50)

        self.num_1 = QPushButton('1', self)
        self.num_1.setStyleSheet('''background-color: #2c3c7a; color: #e0e3f0; font-size: 25px;''')
        self.num_1.resize(50, 50)
        self.num_1.move(10, 100)

        self.num_2 = QPushButton('2', self)
        self.num_2.setStyleSheet('''background-color: #2c3c7a; color: #e0e3f0; font-size: 25px;''')
        self.num_2.resize(50, 50)
        self.num_2.move(65, 100)

        self.num_3 = QPushButton('3', self)
        self.num_3.setStyleSheet('''background-color: #2c3c7a; color: #e0e3f0; font-size: 25px;''')
        self.num_3.resize(50, 50)
        self.num_3.move(120, 100)

        self.div = QPushButton('/', self)
        self.div.setStyleSheet('''background-color: #2c3c7a; color: #e0e3f0; font-size: 25px;''')
        self.div.resize(50, 50)
        self.div.move(175, 100)

        self.div_2 = QPushButton('//', self)
        self.div_2.setStyleSheet('''background-color: #2c3c7a; color: #e0e3f0; font-size: 25px;''')
        self.div_2.resize(50, 50)
        self.div_2.move(230, 100)

        self.mem = QPushButton('MRC', self)
        self.mem.setStyleSheet('''background-color: #2c3c7a; color: #e0e3f0; font-size: 25px;''')
        self.mem.resize(85, 50)
        self.mem.move(285, 100)

        self.num_4 = QPushButton('4', self)
        self.num_4.setStyleSheet('''background-color: #2c3c7a; color: #e0e3f0; font-size: 25px;''')
        self.num_4.resize(50, 50)
        self.num_4.move(10, 155)

        self.num_5 = QPushButton('5', self)
        self.num_5.setStyleSheet('''background-color: #2c3c7a; color: #e0e3f0; font-size: 25px;''')
        self.num_5.resize(50, 50)
        self.num_5.move(65, 155)

        self.num_6 = QPushButton('6', self)
        self.num_6.setStyleSheet('''background-color: #2c3c7a; color: #e0e3f0; font-size: 25px;''')
        self.num_6.resize(50, 50)
        self.num_6.move(120, 155)

        self.mul = QPushButton('*', self)
        self.mul.setStyleSheet('''background-color: #2c3c7a; color: #e0e3f0; font-size: 25px;''')
        self.mul.resize(50, 50)
        self.mul.move(175, 155)

        self.square = QPushButton('xʸ', self)
        self.square.setStyleSheet('''background-color: #2c3c7a; color: #e0e3f0; font-size: 30px;''')
        self.square.resize(50, 50)
        self.square.move(230, 155)

        self.mem_plus = QPushButton('M +', self)
        self.mem_plus.setStyleSheet('''background-color: #2c3c7a; color: #e0e3f0; font-size: 25px;''')
        self.mem_plus.resize(85, 50)
        self.mem_plus.move(285, 155)

        self.num_7 = QPushButton('7', self)
        self.num_7.setStyleSheet('''background-color: #2c3c7a; color: #e0e3f0; font-size: 25px;''')
        self.num_7.resize(50, 50)
        self.num_7.move(10, 210)

        self.num_8 = QPushButton('8', self)
        self.num_8.setStyleSheet('''background-color: #2c3c7a; color: #e0e3f0; font-size: 25px;''')
        self.num_8.resize(50, 50)
        self.num_8.move(65, 210)

        self.num_9 = QPushButton('9', self)
        self.num_9.setStyleSheet('''background-color: #2c3c7a; color: #e0e3f0; font-size: 25px;''')
        self.num_9.resize(50, 50)
        self.num_9.move(120, 210)

        self.plus = QPushButton('+', self)
        self.plus.setStyleSheet('''background-color: #2c3c7a; color: #e0e3f0; font-size: 25px;''')
        self.plus.resize(50, 50)
        self.plus.move(175, 210)

        self.percent = QPushButton('%', self)
        self.percent.setStyleSheet('''background-color: #2c3c7a; color: #e0e3f0; font-size: 25px;''')
        self.percent.resize(50, 50)
        self.percent.move(230, 210)

        self.mem_minus = QPushButton('M -', self)
        self.mem_minus.setStyleSheet('''background-color: #2c3c7a; color: #e0e3f0; font-size: 25px;''')
        self.mem_minus.resize(85, 50)
        self.mem_minus.move(285, 210)

        self.sqrt = QPushButton('√', self)
        self.sqrt.setStyleSheet('''background-color: #2c3c7a; color: #e0e3f0; font-size: 25px;''')
        self.sqrt.resize(50, 50)
        self.sqrt.move(10, 265)

        self.num_0 = QPushButton('0', self)
        self.num_0.setStyleSheet('''background-color: #2c3c7a; color: #e0e3f0; font-size: 25px;''')
        self.num_0.resize(50, 50)
        self.num_0.move(65, 265)

        self.negative = QPushButton('+ / -', self)
        self.negative.setStyleSheet('''background-color: #2c3c7a; color: #e0e3f0; font-size: 17px;''')
        self.negative.resize(50, 50)
        self.negative.move(120, 265)

        self.minus = QPushButton('-', self)
        self.minus.setStyleSheet('''background-color: #2c3c7a; color: #e0e3f0; font-size: 25px;''')
        self.minus.resize(50, 50)
        self.minus.move(175, 265)

        self.fact = QPushButton('x !', self)
        self.fact.setStyleSheet('''background-color: #2c3c7a; color: #e0e3f0; font-size: 25px;''')
        self.fact.resize(50, 50)
        self.fact.move(230, 265)

        self.delete = QPushButton('Del', self)
        self.delete.setStyleSheet('''background-color: #cc3b36; color: #e0e3f0; font-size: 25px;''')
        self.delete.resize(85, 50)
        self.delete.move(285, 265)

        self.point = QPushButton(',', self)
        self.point.setStyleSheet('''background-color: #2c3c7a; color: #e0e3f0; font-size: 25px;''')
        self.point.resize(50, 50)
        self.point.move(230, 320)

        self.ent = QPushButton('=', self)
        self.ent.setStyleSheet('''background-color: #2c3c7a; color: #e0e3f0; font-size: 25px;''')
        self.ent.resize(160, 50)
        self.ent.move(10, 320)

        self.cleaner = QPushButton('C', self)
        self.cleaner.setStyleSheet('''background-color: #2c3c7a; color: #e0e3f0; font-size: 25px;''')
        self.cleaner.resize(50, 50)
        self.cleaner.move(175, 320)

        self.num_1.clicked.connect(self.one)
        self.num_2.clicked.connect(self.two)
        self.num_3.clicked.connect(self.three)
        self.num_4.clicked.connect(self.four)
        self.num_5.clicked.connect(self.five)
        self.num_6.clicked.connect(self.six)
        self.num_7.clicked.connect(self.seven)
        self.num_8.clicked.connect(self.eight)
        self.num_9.clicked.connect(self.nine)
        self.num_0.clicked.connect(self.zero)
        self.plus.clicked.connect(self.plus_1)
        self.minus.clicked.connect(self.minus_1)
        self.div.clicked.connect(self.div_1)
        self.mul.clicked.connect(self.mul_1)
        self.negative.clicked.connect(self.negative_1)
        self.sqrt.clicked.connect(self.sqrt_1)
        self.ent.clicked.connect(self.enter)
        self.cleaner.clicked.connect(self.cleaner_1)
        self.div_2.clicked.connect(self.div_22)
        self.square.clicked.connect(self.square_1)
        self.percent.clicked.connect(self.percent_1)
        self.fact.clicked.connect(self.fact_1)
        self.delete.clicked.connect(self.delete_1)
        self.point.clicked.connect(self.point_1)
        self.mem.clicked.connect(self.mem_1)
        self.mem_plus.clicked.connect(self.mem_plus_1)
        self.mem_minus.clicked.connect(self.mem_minus_1)

    def memory_window(self):
        if self.memory:
            self.label_mem.setText('M')
        else:
            self.label_mem.setText('')

    def enterValue(self):
        self.memory_on = False
        if not self.flag:
            if self.label.text() == '0' or 'For' in self.label.text() or 'You' in self.label.text():
                self.label.setText('')
                self.operation = []
            if self.my_input == '-' and self.operand_1 == []:
                if self.label.text() != '' and self.label.text()[0] != '-' and self.label.text() != '0':
                    self.label.setText(self.my_input + self.label.text())
                elif self.label.text() != '' and self.label.text()[0] == '-':
                    self.label.setText(self.label.text()[1:])
                else:
                    self.label.setText('')
            elif self.my_input == '.':
                if not self.point_on:
                    self.label.setText(self.label.text() + self.my_input)
                else:
                    self.label.setText(self.label.text())
            else:
                self.label.setText(self.label.text() + self.my_input)
        else:
            self.label.setText(self.my_input)
            self.flag = False

    def one(self):
        self.my_input = '1'
        self.enterValue()

    def two(self):
        self.my_input = '2'
        self.enterValue()

    def three(self):
        self.my_input = '3'
        self.enterValue()

    def four(self):
        self.my_input = '4'
        self.enterValue()

    def five(self):
        self.my_input = '5'
        self.enterValue()

    def six(self):
        self.my_input = '6'
        self.enterValue()

    def seven(self):
        self.my_input = '7'
        self.enterValue()

    def eight(self):
        self.my_input = '8'
        self.enterValue()

    def nine(self):
        self.my_input = '9'
        self.enterValue()

    def zero(self):
        self.my_input = '0'
        self.enterValue()

    def point_1(self):
        self.my_input = '.'
        self.enterValue()
        self.point_on = True

    def plus_1(self):
        self.memory_on = False
        if self.operation != [] and not self.label.text()[-1].isdigit():
            self.operation = '+'
            self.operand_1 = float(self.label.text()[:-2])
            self.label.setText(f'{self.operand_1}+ ')
            self.flag = False
            self.point_on = False
        elif self.operation != [] and self.label.text()[-1].isdigit():
            self.many_operation = self.label.text()
            self.label.setText(f'{self.label.text()}+ ')
            self.point_on = False
        else:
            self.operation = '+'
            self.operand_1 = float(self.label.text())
            self.label.setText(f'{self.operand_1}+ ')
            self.flag = False
            self.point_on = False

    def minus_1(self):
        self.memory_on = False
        if self.operation != [] and not self.label.text()[-1].isdigit():
            self.operation = '-'
            self.operand_1 = float(self.label.text()[:-2])
            self.label.setText(f'{self.operand_1}- ')
            self.flag = False
            self.point_on = False
        elif self.operation != [] and self.label.text()[-1].isdigit():
            self.many_operation = self.label.text()
            self.label.setText(f'{self.label.text()}- ')
            self.point_on = False
        else:
            self.operation = '-'
            self.operand_1 = float(self.label.text())
            self.label.setText(f'{self.operand_1}- ')
            self.flag = False
            self.point_on = False

    def div_1(self):
        self.memory_on = False
        if self.operation != [] and not self.label.text()[-1].isdigit():
            self.operation = '/'
            self.operand_1 = float(self.label.text()[:-2])
            self.label.setText(f'{self.operand_1}/ ')
            self.flag = False
            self.point_on = False
        elif self.operation != [] and self.label.text()[-1].isdigit():
            self.many_operation = self.label.text()
            self.label.setText(f'{self.label.text()}/ ')
            self.point_on = False
        else:
            self.operation = '/'
            self.operand_1 = float(self.label.text())
            self.label.setText(f'{self.operand_1}/ ')
            self.flag = False
            self.point_on = False

    def mul_1(self):
        self.memory_on = False
        if self.operation != [] and not self.label.text()[-1].isdigit():
            self.operation = '*'
            self.operand_1 = float(self.label.text()[:-2])
            self.label.setText(f'{self.operand_1}* ')
            self.flag = False
            self.point_on = False
        elif self.operation != [] and self.label.text()[-1].isdigit():
            self.many_operation = self.label.text()
            self.label.setText(f'{self.label.text()}* ')
            self.point_on = False
        else:
            self.operation = '*'
            self.operand_1 = float(self.label.text())
            self.label.setText(f'{self.operand_1}* ')
            self.flag = False
            self.point_on = False

    def negative_1(self):
        self.flag = False
        self.my_input = '-'
        self.enterValue()

    def sqrt_1(self):
        self.memory_on = False
        self.operation = '√'
        self.operand_1 = float(self.label.text())
        self.flag = False
        self.enter()

    def div_22(self):
        self.memory_on = False
        if self.operation != [] and not self.label.text()[-1].isdigit():
            self.operation = '//'
            self.operand_1 = float(self.label.text()[:-2])
            self.label.setText(f'{self.operand_1}//')
            self.flag = False
            self.point_on = False
        elif self.operation != [] and self.label.text()[-1].isdigit():
            self.many_operation = self.label.text()
            self.label.setText(f'{self.label.text()}// ')
            self.point_on = False
        else:
            self.operation = '//'
            self.operand_1 = float(self.label.text())
            self.label.setText(f'{self.operand_1}//')
            self.flag = False
            self.point_on = False

    def square_1(self):
        self.operation = 'xʸ'
        self.operand_1 = float(self.label.text())
        self.label.setText(f'{self.label.text()}^ ')
        self.flag = False
        self.point_on = False
        self.memory_on = False

    def percent_1(self):
        if self.operation == []:
            self.operand_1 = float(self.label.text()) / 100
            self.label.setText(f'{float(self.label.text()) / 100}')
            self.flag = False
            self.point_on = False
            self.memory_on = False
        else:
            self.lst_ex = (self.label.text()).split(' ')
            self.label.setText(self.lst_ex[0] + ' ' + str(float(self.lst_ex[1]) / 100))

    def fact_1(self):
        self.memory_on = False
        self.operation = 'x !'
        if '.' in self.label.text() or '-' in self.label.text():
            self.label.setText('For x! only positive integer')
            self.flag = False
            self.operation = []
            self.point_on = False
        else:
            self.operand_1 = int(self.label.text())
            self.label.setText(f'{self.label.text()} !')
            self.flag = False
            self.enter()

    def delete_1(self):
        if self.label.text()[-2:] == '//':
            self.label.setText(self.label.text()[:-2])
        else:
            self.label.setText(self.label.text()[:-1])
            self.flag = False
            self.memory_on = False

    def mem_1(self):
        if self.memory != []:
            self.operation = []
            self.operation = ''.join((self.memory).split(' '))
            self.rezult = eval(self.operation)
            self.label.setText(str(self.rezult))
            self.memory_on = True
            self.operand_1 = []
            self.operand_2 = []
            self.operation = []
            self.rezult = []
            self.flag = True
            self.point_on = False
        else:
            self.label.setText('0')
            self.flag = True
            self.point_on = False

    def mem_plus_1(self):
        if self.label.text()[-1].isdigit():
            if self.memory == []:
                self.memory = self.label.text()
                self.memory_window()
                self.flag = True
                if self.operation == []:
                    self.label.setText(self.label.text())
                else:
                    self.enter()
            else:
                self.memory = f'{self.memory}+ {self.label.text()}'
                self.memory_window()
                self.flag = True
                if self.operation == []:
                    self.label.setText(self.label.text())
                else:
                    self.enter()
        if not self.label.text()[-1].isdigit() and self.label.text()[0].isdigit():
            if self.memory == []:
                self.memory = self.label.text()[:-2]
                self.memory_window()
                self.label.setText(self.label.text())
                self.flag = True
            else:
                self.memory = f'{self.memory}+ {self.label.text()[:-2]}'
                self.memory_window()
                self.label.setText(self.label.text())
                self.flag = True
        else:
            self.label.setText(self.label.text())
            self.flag = True

    def mem_minus_1(self):
        if self.label.text()[-1].isdigit():
            if self.memory == []:
                self.memory = f'-{self.label.text()}'
                self.memory_window()
                self.flag = True
                if self.operation == []:
                    self.label.setText(self.label.text())
                else:
                    self.enter()
            else:
                self.memory = f'{self.memory}- {self.label.text()}'
                self.memory_window()
                self.flag = True
                if self.operation == []:
                    self.label.setText(self.label.text())
                else:
                    self.enter()
        if not self.label.text()[-1].isdigit() and self.label.text()[0].isdigit():
            if self.memory == []:
                self.memory = f'-{self.label.text()[:-2]}'
                self.memory_window()
                self.label.setText(self.label.text())
                self.flag = True
            else:
                self.memory = f'{self.memory}- {self.label.text()[:-2]}'
                self.memory_window()
                self.label.setText(self.label.text())
                self.flag = True
        else:
            self.label.setText(self.label.text())
            self.memory_window()
            self.flag = True

    def enter(self):
        self.memory_on = False
        if self.many_operation == []:
            if self.operation != [] and (self.label.text()[-1].isdigit() or self.label.text()[-1] == '!'):
                if self.operation == 'x !':
                    from math import factorial
                    self.rezult = factorial(self.operand_1)
                elif self.operation == '√':
                    self.rezult = self.operand_1 ** (1 / 2)
                elif self.operation == '//':
                    self.lst_ex = (self.label.text()).split('//')
                    self.operand_2 = float(self.lst_ex[1])
                    if self.operand_2 == 0:
                        self.rezult = "You can't divide by zero!🤪"
                    else:
                        self.rezult = self.operand_1 // self.operand_2
                else:
                    self.lst_ex = (self.label.text()).split(' ')
                    self.operand_2 = float(self.lst_ex[1])
                    if self.operation == '+':
                        self.rezult = self.operand_1 + self.operand_2
                    elif self.operation == '-':
                        self.rezult = self.operand_1 - self.operand_2
                    elif self.operation == '*':
                        self.rezult = self.operand_1 * self.operand_2
                    elif self.operation == '/':
                        if self.operand_2 == 0:
                            self.rezult = "You can't divide by zero!🤪"
                        else:
                            self.rezult = self.operand_1 / self.operand_2
                    elif self.operation == 'xʸ':
                        self.rezult = self.operand_1 ** self.operand_2

            elif self.operation != [] and not self.label.text()[-1].isdigit():
                self.rezult = float(self.label.text()[:-2])
            else:
                self.rezult = self.label.text()
        else:
            self.many_operation = self.label.text()
            self.operation = []
            self.operation = ''.join((self.many_operation).split(' '))
            self.rezult = eval(self.operation)

        self.label.setText(str(self.rezult))
        self.operand_1 = []
        self.operand_2 = []
        self.operation = []
        self.rezult = []
        self.flag = True
        self.point_on = False

    def cleaner_1(self):
        if self.memory_on:
            self.label.setText('0')
            self.memory = []
            self.memory_on = False
            self.memory_window()
        else:
            self.label.setText('0')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Calculator()
    ex.show()
    sys.exit(app.exec())
