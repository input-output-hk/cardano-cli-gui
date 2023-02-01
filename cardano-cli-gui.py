

import sys
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import (QApplication, QMainWindow, QPushButton, 
                             QLabel, QLineEdit, QWidget, QGridLayout)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")

        picture02 = QLabel("")
        picture02.setPixmap(QPixmap("./images/cardano.png"))
        picture02.setFixedSize(80,60)
        picture02.setScaledContents(True)

        self.label10 = QLabel("Verification key:")
        font10 = self.label10.font()
        font10.setPointSize(12)
        self.label10.setFont(font10)

        self.input20 = QLineEdit()
        self.input20.setFixedSize(500,30)

        self.button21 = QPushButton("Load")
        self.button21.setFixedSize(80,30)
        self.button22 = QPushButton("Generate")
        self.button22.setFixedSize(80,30)

        layout = QGridLayout()
        layout.addWidget(picture02, 0, 2)
        layout.addWidget(self.label10, 1, 0)
        layout.addWidget(self.input20, 2, 0)
        layout.addWidget(self.button21, 2, 1)
        layout.addWidget(self.button22, 2, 2)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()

