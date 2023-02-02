

from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import (QPushButton, QLabel, QLineEdit, QWidget, QGridLayout)

class Start(QWidget):
    def __init__(self):
        super().__init__()

        # Cardano picture
        picture_1_1 = QLabel("")
        picture_1_1.setPixmap(QPixmap("./images/cardano.png"))
        picture_1_1.setFixedSize(80,80)
        picture_1_1.setScaledContents(True)

        # Widgets for Status tab 
        label_3_0 = QLabel("Input folder path:")
        input_4_0 = QLineEdit()
        button_4_1 = QPushButton("Set")
        label_6_0 = QLabel("Current folder path set to:")
        label_7_0 = QLabel("NO FOLDER PATH SET")
        label_11_0 = QLabel("IMPORTANT:")
        label_12_0 = QLabel("A cardano node has to be synced and running.")

        # Set label fonts 
        labels = [label_3_0, label_6_0, 
                  label_7_0, label_11_0, 
                  label_12_0]
        for label in labels:
            font = label.font()
            font.setPointSize(12)
            label.setFont(font)

        # Set lineEdit size 
        input_4_0.setFixedSize(500,30)

        # Set button size 
        button_4_1.setFixedSize(80,30)

        # Space between the sections
        emptyLabel = QLabel()

        # Layouts 
        layout = QGridLayout()
        layout.addWidget(emptyLabel, 0, 0)
        layout.addWidget(emptyLabel, 1, 0)
        layout.addWidget(picture_1_1, 1, 1)
        layout.addWidget(emptyLabel, 2, 0)
        layout.addWidget(label_3_0, 3, 0)
        layout.addWidget(input_4_0, 4, 0)
        layout.addWidget(button_4_1, 4, 1)
        layout.addWidget(emptyLabel, 5, 0)
        layout.addWidget(label_6_0, 6, 0)
        layout.addWidget(label_7_0, 7, 0)
        layout.addWidget(emptyLabel, 8, 0)
        layout.addWidget(emptyLabel, 9, 0)
        layout.addWidget(emptyLabel, 10, 0)
        layout.addWidget(label_11_0, 11, 0)
        layout.addWidget(label_12_0, 12, 0)
        layout.addWidget(emptyLabel, 13, 0)
        layout.addWidget(emptyLabel, 14, 0)
        layout.addWidget(emptyLabel, 15, 0)

        self.setLayout(layout)
