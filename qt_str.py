
import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtWidgets import QPlainTextEdit, QLineEdit
from PyQt5.QtGui import QIcon
from PyQt5 import QtCore

from logic_func import AND

class Prog(QWidget):
    def __init__(self):

        super().__init__()
        self.initUI()

    def initUI(self):

        self.setGeometry(150, 150, 450, 80)
        self.setFixedSize(450, 80)
        self.setWindowTitle('Logic Function')
        self.setWindowIcon(QIcon('res/icon.png'))

        self.button = QPushButton("==>", self)
        self.button.move(280, 15)
        self.button.resize(50, 50)
        self.button.pressed.connect(self.button_func)

        self.input_edit = QLineEdit(self)
        self.input_edit.resize(250, 50)
        self.input_edit.move(15, 15)
        self.input_edit.setAlignment(QtCore.Qt.AlignCenter)
        # self.input_edit.textChanged.connect(self.on_text_changed)

        self.print_edit = QLineEdit(self)
        self.print_edit.resize(90, 50)
        self.print_edit.move(345, 15)
        self.print_edit.setAlignment(QtCore.Qt.AlignCenter)

    def button_func(self):
        self.print_edit.setText(str(eval(self.input_edit.text())))

    def on_text_changed(self, text):
        width = self.input_edit.fontMetrics().width(text)
        self.input_edit.setMinimumWidth(width)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    prog = Prog()
    prog.show()
    sys.exit(app.exec())
