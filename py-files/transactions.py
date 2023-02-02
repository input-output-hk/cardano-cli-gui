

from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import (QPushButton, QLabel, QLineEdit, 
                             QWidget, QGridLayout, QRadioButton)

class Transactions(QWidget):
    def __init__(self):
        super().__init__()

        # Cardano picture
        picture_0_1 = QLabel("")
        picture_0_1.setPixmap(QPixmap("./images/cardano.png"))
        picture_0_1.setFixedSize(80,80)
        picture_0_1.setScaledContents(True)

        # Widgets for payment address section 
        self.label_1_0 = QLabel("Payment address name:")
        self.input_2_0 = QLineEdit()
        self.button_2_1 = QPushButton("Load")
        
        self.label_4_0 = QLabel("Payment address funds:")
        self.input_5_0 = QLineEdit()
        self.button_5_1 = QPushButton("Querry\nfunds")

        # Widgets for sending funds section 
        self.label_8_0 = QLabel("Send funds:")
        self.input_9_0 = QLineEdit()
        self.radioButton_9_1 = QRadioButton("Ada")
        self.label_10_0 = QLabel("NOTE: Seperat decimal number with dot.")
        self.radioButton_10_1 = QRadioButton("Lovelace")

        self.label_12_0 = QLabel("Receiving address:")
        self.input_13_0 = QLineEdit()
        self.button_13_1 = QPushButton("Load")

        self.button_15_0 = QPushButton("Send")

        # Set label fonts 
        labels = [self.label_1_0, self.label_4_0, 
                  self.label_8_0, self.label_10_0,
                  self.label_12_0]
        for label in labels:
            font = label.font()
            font.setPointSize(12)
            label.setFont(font)

        # Set lineEdit sizes 
        inputs = [self.input_2_0, self.input_9_0, 
                  self.input_13_0]
        for input in inputs:
            input.setFixedSize(500,30)

        self.input_5_0.setFixedSize(500,80)

        # Set button sizes         
        self.button_2_1.setFixedSize(80,30)
        self.button_5_1.setFixedSize(80,60)
        self.button_13_1.setFixedSize(80,30)
        self.button_15_0.setFixedSize(160,30)

        # Space between the sections
        self.emptyLabel = QLabel()

        # Layouts 
        layout = QGridLayout()
        layout.addWidget(picture_0_1, 0, 1)
        # Adding widgets for payment address section 
        layout.addWidget(self.label_1_0, 1, 0)
        layout.addWidget(self.input_2_0, 2, 0)
        layout.addWidget(self.button_2_1, 2, 1)
        layout.addWidget(self.emptyLabel, 3, 0)

        layout.addWidget(self.label_4_0, 4, 0)
        layout.addWidget(self.input_5_0, 5, 0)
        layout.addWidget(self.button_5_1, 5, 1)
        layout.addWidget(self.emptyLabel, 6, 0)
        layout.addWidget(self.emptyLabel, 7, 0)
        # Adding widgets for payment address section 
        layout.addWidget(self.label_8_0, 8, 0)
        layout.addWidget(self.input_9_0, 9, 0)
        layout.addWidget(self.radioButton_9_1, 9, 1)
        layout.addWidget(self.label_10_0, 10, 0)
        layout.addWidget(self.radioButton_10_1, 10, 1)
        layout.addWidget(self.emptyLabel, 11, 0)

        layout.addWidget(self.label_12_0, 12, 0)
        layout.addWidget(self.input_13_0, 13, 0)
        layout.addWidget(self.button_13_1, 13, 1)
        layout.addWidget(self.emptyLabel, 14, 0)
        layout.addWidget(self.button_15_0, 15, 0)
        layout.addWidget(self.emptyLabel, 16, 0)

        self.setLayout(layout)