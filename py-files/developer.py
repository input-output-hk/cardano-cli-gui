

import settings

from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import (QPushButton, QLabel, QLineEdit, 
                             QWidget, QGridLayout, QMessageBox)

# Widgets and functions for the developer tab
class Developer(QWidget):
    def __init__(self):
        super().__init__()

        # Initial message
        label_1_0 = QLabel("Manage advenced settings. Only for experienced developers.\n" + \
                           "If you are not sure keep default parameter values.")

        # Cardano picture
        picture_1_1 = QLabel("")
        picture_1_1.setPixmap(QPixmap("./images/cardano.png"))
        picture_1_1.setFixedSize(80,80)
        picture_1_1.setScaledContents(True)

        # Widgets for testnet magic section 
        label_3_0 = QLabel("Input testnet magic number:")
        self.input_4_0 = QLineEdit()
        button_4_1 = QPushButton("Set")
        self.label_5_0 = QLabel("Current testnet magic set to: " + settings.testnet_magic)

        # Widgets for era section
        label_8_0 = QLabel("Input era:")
        self.input_9_0 = QLineEdit()
        button_9_1 = QPushButton("Set")
        self.label_10_0 = QLabel("Current era set to: " + settings.current_era)

        # Widgets for default value section
        label_13_0 = QLabel("Reset parameters to default values:")
        button_14_0 = QPushButton("Reset")

        # Button functions
        button_4_1.clicked.connect(self.set_magic)
        button_9_1.clicked.connect(self.set_era)
        button_14_0.clicked.connect(self.reset_values)

        # Set label fonts 
        labels = [label_1_0, label_3_0, 
                  self.label_5_0, label_8_0, 
                  self.label_10_0, label_13_0]
        for label in labels:
            font = label.font()
            font.setPointSize(12)
            label.setFont(font)

        # Set lineEdit size 
        self.input_4_0.setFixedSize(500,30)
        self.input_9_0.setFixedSize(500,30)

        # Set button size 
        button_4_1.setFixedSize(80,30)
        button_9_1.setFixedSize(80,30)
        button_14_0.setFixedSize(160,30)

        # Space between the sections
        emptyLabel = QLabel()

        # Layouts 
        layout = QGridLayout()
        layout.addWidget(emptyLabel, 0, 0)
        layout.addWidget(label_1_0, 1, 0)
        layout.addWidget(picture_1_1, 1, 1)
        layout.addWidget(emptyLabel, 2, 0)
        layout.addWidget(label_3_0, 3, 0)
        layout.addWidget(self.input_4_0, 4, 0)
        layout.addWidget(button_4_1, 4, 1)
        layout.addWidget(self.label_5_0, 5, 0)
        layout.addWidget(emptyLabel, 6, 0)
        layout.addWidget(emptyLabel, 7, 0)
        layout.addWidget(label_8_0, 8, 0)
        layout.addWidget(self.input_9_0, 9, 0)
        layout.addWidget(button_9_1, 9, 1)
        layout.addWidget(self.label_10_0, 10, 0)
        layout.addWidget(emptyLabel, 11, 0)
        layout.addWidget(emptyLabel, 12, 0)
        layout.addWidget(label_13_0, 13, 0)
        layout.addWidget(button_14_0, 14, 0)
        layout.addWidget(emptyLabel, 15, 0)
        layout.addWidget(emptyLabel, 16, 0)

        self.setLayout(layout)

    # Functions for setting global variables
    def set_magic(self):
        input_magic = self.input_4_0.text()
        if not input_magic.isdigit():
            msg = "Testnet magic number should contain only digits."        
            QMessageBox.warning(self, "Notification:", msg,
                                QMessageBox.Close)
        else:
            settings.testnet_magic = input_magic
            self.label_5_0.setText("Current testnet magic set to: " + settings.testnet_magic)
        

    def set_era(self):
        input_era = self.input_9_0.text()
        if input_era == "":
            msg = "Era can not be an empty string."        
            QMessageBox.warning(self, "Notification:", msg,
                                QMessageBox.Close)
        else:
            settings.current_era = input_era
            self.label_10_0.setText("Current era set to: " + settings.current_era) 

    def reset_values(self):
        settings.testnet_magic = "2"
        self.input_4_0.setText("")
        self.label_5_0.setText("Current testnet magic set to: " + settings.testnet_magic)
        
        settings.current_era = "babbage-era"
        self.input_9_0.setText("")
        self.label_10_0.setText("Current era set to: " + settings.current_era)     