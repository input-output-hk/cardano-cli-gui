

import settings
from os.path import exists
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

        # Widgets for folder section 
        label_3_0 = QLabel("Input folder path:")
        self.input_4_0 = QLineEdit()
        button_4_1 = QPushButton("Set")
        label_5_0 = QLabel("Current folder path set to:")
        self.label_6_0 = QLabel("NO FOLDER PATH SET")

        # Widgets for notification section
        self.label_8_0 = QLabel("Debug mode: OFF")
        label_9_0 = QLabel("If debug mode is ON, the programm prints the cardano-cli\ncommands to the terminal instead of executing them.")
        label_11_0 = QLabel("IMPORTANT:")
        label_12_0 = QLabel("A cardano node has to be synced and running.")

        # Widget actions
        button_4_1.clicked.connect(self.set_folder_path)

        # Set label fonts 
        labels = [label_3_0, label_5_0, 
                  self.label_6_0, self.label_8_0,
                  label_9_0, label_11_0, 
                  label_12_0]
        for label in labels:
            font = label.font()
            font.setPointSize(12)
            label.setFont(font)

        # Set lineEdit size 
        self.input_4_0.setFixedSize(500,30)

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
        layout.addWidget(self.input_4_0, 4, 0)
        layout.addWidget(button_4_1, 4, 1)
        layout.addWidget(label_5_0, 5, 0)
        layout.addWidget(self.label_6_0, 6, 0)
        layout.addWidget(emptyLabel, 7, 0)
        layout.addWidget(self.label_8_0, 8, 0)
        layout.addWidget(label_9_0, 9, 0)
        layout.addWidget(emptyLabel, 10, 0)
        layout.addWidget(label_11_0, 11, 0)
        layout.addWidget(label_12_0, 12, 0)
        layout.addWidget(emptyLabel, 14, 0)
        layout.addWidget(emptyLabel, 15, 0)

        self.setLayout(layout)

    def set_folder_path(self):
        folder_path_input = self.input_4_0.text()
        if folder_path_input[-1] == "/":
            folder_path_input = folder_path_input[0:-1]
        folder_exists = exists(folder_path_input)
        
        if folder_exists:
            settings.folder_path = folder_path_input
            self.label_7_0.setText(folder_path_input)
