

from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import (QPushButton, QLabel, QLineEdit, QWidget, QGridLayout)

class Wallet(QWidget):
    def __init__(self):
        super().__init__()

        # Cardano picture
        picture_0_2 = QLabel("")
        picture_0_2.setPixmap(QPixmap("./images/cardano.png"))
        picture_0_2.setFixedSize(80,80)
        picture_0_2.setScaledContents(True)

        # Widgets for verification key section 
        self.label_1_0 = QLabel("Verification key name:")
        self.input_2_0 = QLineEdit()
        self.button_2_1 = QPushButton("Load")
        self.button_2_2 = QPushButton("Generate")

        # Widgets for signing key section 
        self.label_4_0 = QLabel("Signing key name:")
        self.input_5_0 = QLineEdit()
        self.button_5_1 = QPushButton("Load")
        self.button_5_2 = QPushButton("Generate")

        # Widgets for payment address section 
        self.label_7_0 = QLabel("Payment address name:")
        self.input_8_0 = QLineEdit()
        self.button_8_1 = QPushButton("Load")
        self.button_8_2 = QPushButton("Generate")
        self.label_9_0 = QLabel("Payment address:")
        self.input_10_0 = QLineEdit()

        # Widgets for payment address key hash section 
        self.label_12_0 = QLabel("Payment public key hash name:")
        self.input_13_0 = QLineEdit()
        self.button_13_1 = QPushButton("Load")
        self.button_13_2 = QPushButton("Generate")
        self.label_14_0 = QLabel("Key hash:")
        self.input_15_0 = QLineEdit()

        # Set label fonts 
        labels = [self.label_1_0, self.label_4_0, 
                  self.label_7_0, self.label_9_0,
                  self.label_12_0, self.label_14_0]
        for label in labels:
            font = label.font()
            font.setPointSize(12)
            label.setFont(font)

        # Set lineEdit sizes 
        inputs = [self.input_2_0, self.input_5_0, 
                  self.input_8_0, self.input_10_0,
                  self.input_13_0, self.input_15_0]
        for input in inputs:
            input.setFixedSize(500,30)

        # Set button sizes 
        buttons = [self.button_2_1, self.button_2_2,
                   self.button_5_1, self.button_5_2,
                   self.button_8_1, self.button_8_2,
                   self.button_13_1, self.button_13_2]
        for button in buttons:
            button.setFixedSize(80,30)   

        # Space between the sections
        self.emptyLabel = QLabel()

        # Layouts 
        layout = QGridLayout()
        layout.addWidget(picture_0_2, 0, 2)
        # Adding widgets for verification key section 
        layout.addWidget(self.label_1_0, 1, 0)
        layout.addWidget(self.input_2_0, 2, 0)
        layout.addWidget(self.button_2_1, 2, 1)
        layout.addWidget(self.button_2_2, 2, 2)
        layout.addWidget(self.emptyLabel, 3, 0)
        # Adding widgets for signing key section 
        layout.addWidget(self.label_4_0, 4, 0)
        layout.addWidget(self.input_5_0, 5, 0)
        layout.addWidget(self.button_5_1, 5, 1)
        layout.addWidget(self.button_5_2, 5, 2)
        layout.addWidget(self.emptyLabel, 6, 0)
        # Adding widgets for payment address section 
        layout.addWidget(self.label_7_0, 7, 0)
        layout.addWidget(self.input_8_0, 8, 0)
        layout.addWidget(self.button_8_1, 8, 1)
        layout.addWidget(self.button_8_2, 8, 2)
        layout.addWidget(self.label_9_0, 9, 0)
        layout.addWidget(self.input_10_0, 10, 0)
        layout.addWidget(self.emptyLabel, 11, 0)
        # Adding widgets for payment public key hash section 
        layout.addWidget(self.label_12_0, 12, 0)
        layout.addWidget(self.input_13_0, 13, 0)
        layout.addWidget(self.button_13_1, 13, 1)
        layout.addWidget(self.button_13_2, 13, 2)
        layout.addWidget(self.label_14_0, 14, 0)
        layout.addWidget(self.input_15_0, 15, 0)
        layout.addWidget(self.emptyLabel, 16, 0)

        self.setLayout(layout)