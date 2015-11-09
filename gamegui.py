import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class GameGui(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):
        self.myfont = QFont("Source Code Pro", 12, QFont.Bold)

        self.pal = QPalette()
        self.pal.setColor(QPalette.Base, QColor(10, 10, 10))
        self.pal.setColor(QPalette.Background, QColor(30, 30, 30))
        self.pal.setColor(QPalette.Text, QColor(240, 240, 240))

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle("Hello World :)")
        self.setFont(self.myfont)
        self.setPalette(self.pal)

        self.vbox = QVBoxLayout()

        self.text = QTextEdit(self)
        self.text.setReadOnly(True)
        self.text.setPalette(self.pal)
        self.vbox.addWidget(self.text)

        self.input = QLineEdit("", self)
        self.vbox.addWidget(self.input)

        self.setLayout(self.vbox)
        self.show()


    def addText(self, text, color):
        self.text.moveCursor(QTextCursor.End)
        self.text.setTextColor(QColor(color[0], color[1], color[2]))
        self.text.insertPlainText(text)
        self.text.moveCursor(QTextCursor.End)


