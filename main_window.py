# импорт библиотек
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from text_ex import Text_ex
from main_ui import Ui_Form


# Создание главного стартового окна
class Main(QMainWindow, Ui_Form):
    # инициальзация
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.text.clicked.connect(self.open_text)

    # открытие окна с заданиями
    def open_text(self):
        self.win = Text_ex()
        self.win.setObjectName("MainWindow")
        self.win.setStyleSheet("#MainWindow{border-image:url(image.jpg)}")
        self.win.show()


# чтобы видеть ошибки
def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


# запуск
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Main()
    ex.setObjectName("MainWindow")
    ex.setStyleSheet("#MainWindow{border-image:url(image.jpg)}")
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec_())
