
import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtWidgets import QPlainTextEdit
from PyQt5.QtGui import QIcon

class Prog(QWidget):
    def __init__(self):

        super().__init__()
        self.initUI()

    def initUI(self):

        self.setGeometry(150, 150, 300, 450)
        self.setFixedSize(300, 450)
        self.setWindowTitle('Logic Function')
        self.setWindowIcon(QIcon('res/icon.png'))

        



if __name__ == '__main__':
    app = QApplication(sys.argv)
    prog = Prog()
    prog.show()
    sys.exit(app.exec())
