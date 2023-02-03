
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import (QPushButton, QLabel, QLineEdit, 
                             QWidget, QGridLayout, QRadioButton)

class Smart_contracts(QWidget):
    def __init__(self):
        super().__init__()

        # Cardano picture
        self.label_0_0 = QLabel("Generate cardano script address.")
        picture_0_2 = QLabel("")
        picture_0_2.setPixmap(QPixmap("./images/cardano.png"))
        picture_0_2.setFixedSize(80,80)
        picture_0_2.setScaledContents(True)

        # Widgets for building script address section 
        self.label_1_0 = QLabel("Type in script file name:")
        self.input_2_0 = QLineEdit()
        self.button_2_1 = QPushButton("Set")
        self.label_3_0 = QLabel("Script payment address file name:")
        self.input_4_0 = QLineEdit()
        self.button_4_1 = QPushButton("Set")
        self.button_4_2 = QPushButton("Generate")
        self.label_5_0 = QLabel("Script payment address:")
        self.input_6_0 = QLineEdit() 
        self.button_6_1 = QPushButton("Show")

        # Widgets for sending funds to script address section
        self.label_9_0 = QLabel("Send funds to the above script address.")
        self.label_10_0 = QLabel("Type in your address:")
        self.input_11_0 = QLineEdit()
        self.button_11_1 = QPushButton("Set")
        self.label_12_0 = QLabel("Input UTxO address:")
        self.input_13_0 = QLineEdit()
        self.button_13_1 = QPushButton("Set")
        self.label_14_0 = QLabel("Send follwing amount:")
        self.input_15_0 = QLineEdit()
        self.radioButton_15_1 = QRadioButton("Ada")
        self.radioButton_15_2 = QRadioButton("Lovelace")
        self.label_16_0 = QLabel("Type in datum file name:")
        self.input_17_0 = QLineEdit()
        self.button_17_1 = QPushButton("Set")

        self.button_19_0 = QPushButton("Send")

        # Set label fonts 
        labels = [self.label_0_0, 
                  self.label_1_0, self.label_3_0, 
                  self.label_5_0, self.label_9_0, 
                  self.label_10_0, self.label_12_0, 
                  self.label_14_0, self.label_16_0]
        for label in labels:
            font = label.font()
            font.setPointSize(12)
            label.setFont(font)

        self.label_9_0.setFixedSize(500,80)

        # Set lineEdit sizes 
        inputs = [self.input_2_0, self.input_4_0, 
                  self.input_6_0, self.input_11_0, 
                  self.input_13_0, self.input_15_0,
                  self.input_17_0]
        for input in inputs:
            input.setFixedSize(500,30)

        # Set button sizes 
        buttons = [self.button_2_1, self.button_4_1,
                   self.button_4_2, self.button_6_1, 
                   self.button_11_1, self.button_13_1,
                   self.button_17_1]
        for button in buttons:
            button.setFixedSize(80,30)

        self.button_19_0.setFixedSize(160,30) 

        # Space between the sections
        self.emptyLabel = QLabel()

        # Layouts 
        layout = QGridLayout()
        layout.addWidget(self.label_0_0 , 0, 0)
        layout.addWidget(picture_0_2, 0, 2)
        # Adding widgets building script address section 
        layout.addWidget(self.label_1_0, 1, 0)
        layout.addWidget(self.input_2_0, 2, 0)
        layout.addWidget(self.button_2_1, 2, 1)
        layout.addWidget(self.label_3_0, 3, 0)
        layout.addWidget(self.input_4_0, 4, 0)
        layout.addWidget(self.button_4_1, 4, 1)
        layout.addWidget(self.button_4_2, 4, 2)
        layout.addWidget(self.label_5_0, 5, 0)
        layout.addWidget(self.input_6_0, 6, 0) 
        layout.addWidget(self.button_6_1, 6, 1)  
        layout.addWidget(self.emptyLabel, 7, 0)
        layout.addWidget(self.emptyLabel, 8, 0)
        # Adding widgets for sending funds to script address section 
        layout.addWidget(self.label_9_0, 9, 0)
        layout.addWidget(self.label_10_0, 10, 0)
        layout.addWidget(self.input_11_0, 11, 0)
        layout.addWidget(self.button_11_1, 11, 1)
        layout.addWidget(self.label_12_0, 12, 0)
        layout.addWidget(self.input_13_0, 13, 0)
        layout.addWidget(self.button_13_1, 13, 1)
        layout.addWidget(self.label_14_0, 14, 0)
        layout.addWidget(self.input_15_0, 15, 0)
        layout.addWidget(self.radioButton_15_1, 15, 1)
        layout.addWidget(self.radioButton_15_2, 15, 2)
        layout.addWidget(self.label_16_0, 16, 0)
        layout.addWidget(self.input_17_0, 17, 0)
        layout.addWidget(self.button_17_1, 17, 1)
        layout.addWidget(self.emptyLabel, 18, 0)
        layout.addWidget(self.button_19_0, 19, 0)

        self.setLayout(layout) 