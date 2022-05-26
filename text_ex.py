# pyuic5 ui_file.ui -o ui_file.py
import sqlite3
import sys
from PyQt5.QtWidgets import QMainWindow
from text_ui import Ui_Dialog
from random import sample


class Text_ex(QMainWindow, Ui_Dialog):
    # создание необходимых переменных
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.arg = 0
        self.formuls = []
        self.znach = []
        self.arg2 = 0
        self.flag2 = True
        self.flag3 = True
        self.plus = 0
        self.minus = 0

    # показывает кнопки режимов теплоты электричества и движения
    def show_regim(self):
        self.heat.show()
        self.electricity.show()
        self.movement.show()

    # запись данных из базы данных
    def open_dp(self):
        send = self.sender()
        type = send.text()
        con = sqlite3.connect("book.db")
        cur = con.cursor()
        self.result = cur.execute(f"""SELECT * FROM {type}
                    """).fetchall()
        self.pushButton_4.show()
        self.pushButton_3.show()
        self.heat.hide()
        self.electricity.hide()
        self.movement.hide()

    # добовление в строку символов которых нет на стандартной клавиатуре
    def add_symbol(self):
        send = self.sender()
        text = self.lineEdit.text()
        self.lineEdit.setText(text + send.text())

    # показывает все необхадимые виджеты
    def show_all(self):
        self.label.show()
        self.label_2.show()
        self.label_3.show()
        self.label_4.show()
        self.label_5.show()
        self.pushButton.show()
        self.pushButton_2.show()
        self.lineEdit.show()
        self.pushButton_4.hide()
        self.pushButton_3.hide()

    # создаёт список random_exe в котором хранятся случайные примеры и создаёт списко znach в котором хранятся ответы
    # на примеры для режима формулы  при первом проходе
    def reg_formuls(self):
        self.flag3 = False
        for i in self.result:
            self.formuls.append((i[0], self.arg))
            self.znach.append((self.arg, i[1]))
            self.arg += 1
        self.random_exe = sample(self.znach, len(self.znach))
        self.label.setText(str(self.random_exe[self.arg2][1]))
        self.pushButton_6.show()
        self.pushButton_5.show()
        self.pushButton_7.show()
        self.show_all()

    # создаёт список random_exe в котором хранятся случайные примеры и создаёт списко znach в котором хранятся ответы
    # на примеры для режима значение при первом проходе
    def reg_znach(self):
        for i in self.result:
            self.formuls.append((self.arg, i[0]))
            self.znach.append((i[1], self.arg))
            self.arg += 1
        self.random_exe = sample(self.formuls, len(self.formuls))
        self.label.setText(str(self.random_exe[self.arg2][1]))
        self.show_all()

    # создаёт список random_exe в котором хранятся случайные примеры для всех режимов
    def random_ex(self):
        if self.flag3:
            self.random_exe = sample(self.formuls, len(self.formuls))
        else:
            self.random_exe = sample(self.znach, len(self.znach))

    # перезапускает программу с момента выбора режима
    def reload(self):
        self.random_ex()
        self.plus = 0
        self.minus = 0
        self.arg2 = 0
        self.label_2.setText("0")
        self.label_3.setText("0")
        self.label.setText("")
        self.lineEdit.setText("")
        self.pushButton.show()
        self.lineEdit.show()
        self.label.setText(str(self.random_exe[self.arg2][1]))

    # показывает пример пользователю
    def show_ex(self):
        if self.arg2 < len(self.formuls) - 1:
            self.arg2 += 1
        else:
            self.pushButton.hide()
            self.lineEdit.hide()
        self.label.setText(str(self.random_exe[self.arg2][1]))
        self.lineEdit.setText("")

    # сравнивает ответ пользователя с правильным ответом
    def plus_minus(self):
        if self.flag3:
            otvet = self.znach[self.random_exe[self.arg2][0]][0]
        else:
            otvet = self.formuls[self.random_exe[self.arg2][0]][0]
        if self.lineEdit.text() == otvet:
            self.plus += 1
            self.label_2.setText(str(self.plus))
            self.show_ex()
        else:
            self.minus += 1
            self.label_3.setText(str(self.minus))
            self.show_ex()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)
