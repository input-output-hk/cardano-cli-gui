

import settings

from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtWidgets import (QPushButton, QLabel, QLineEdit, 
                             QWidget, QGridLayout, QMessageBox,
                             QComboBox, QPlainTextEdit)

# Widgets and functions for the query tab
class Query(QWidget):
    def __init__(self):
        super().__init__()

        # Header text 
        self.label_0_0 = QLabel("Query the blockchain for parameters and funds.\n" + \
                                "Generate protocol parameter file for an anddress.")

        # Cardano picture
        picture_0_1 = QLabel("")
        picture_0_1.setPixmap(QPixmap("./images/cardano.png"))
        picture_0_1.setFixedSize(80,80)
        picture_0_1.setScaledContents(True)

        # Selecting net type
        self.label_1_0 = QLabel("Select mainnet or testnet for actions in this tab:")
        self.comboBox_2_0 = QComboBox()

        # Widgets for querying address section 
        self.label_3_0 = QLabel("Type in a address file name:")
        self.input_4_0 = QLineEdit()
        self.button_4_1 = QPushButton("Set")
        self.label_5_0 = QLabel("Funds for above payment address:")
        self.input_6_0 = QPlainTextEdit()
        self.button_6_1 = QPushButton("Querry\nfunds")

        # Widgets for querying net info section
        self.label_7_0 = QLabel("Mainnet or testnet information:")
        self.input_8_0 = QPlainTextEdit()
        self.button_8_1 = QPushButton("Querry\ninfo")

        # Widgets for protocol parameters file section
        self.label_9_0 = QLabel("Generate protocol parameters file:")
        self.input_10_0 = QLineEdit("")
        self.button_10_1 = QPushButton("Generate")

        # Button functions
        self.button_4_1.clicked.connect(self.set_address)
        self.button_6_1.clicked.connect(self.query_address)
        self.button_8_1.clicked.connect(self.query_net)
        self.button_10_1.clicked.connect(self.generate_protocol_params_file)

        # Set label fonts 
        labels = [self.label_0_0, self.label_1_0,
                  self.label_3_0, self.label_5_0,
                  self.label_7_0, self.label_9_0]
        for label in labels:
            font = label.font()
            font.setPointSize(12)
            label.setFont(font)

        # Set lineEdit size 
        inputs = [self.input_4_0, self.input_6_0,
                  self.input_8_0, self.input_10_0] 
        for input in inputs:
            input.setFixedSize(500, 30)

        # Set plainTextEdit properties
        consolas_font = QFont()
        consolas_font.setFamily("Consolas")

        self.input_6_0.setFixedSize(500,230) 
        self.input_6_0.setFont(consolas_font)
        self.input_6_0.setLineWrapMode(QPlainTextEdit.LineWrapMode.NoWrap) 
        self.init_text = "                              TxHash                              TxIx          Amount\n" + \
                         "--------------------------------------------------------------------------------------------"
        self.input_6_0.setPlainText(self.init_text)

        self.input_8_0.setFixedSize(500,140) 
        self.input_8_0.setFont(consolas_font)
        self.input_8_0.setLineWrapMode(QPlainTextEdit.LineWrapMode.NoWrap) 
        self.input_8_0.setPlainText("")

        # Set button size 
        self.button_6_1.setFixedSize(80,30)
        self.button_6_1.setFixedSize(80,60)
        self.button_8_1.setFixedSize(80,60)
        self.button_10_1.setFixedSize(80,30)

        # Space between the sections
        emptyLabel = QLabel()

        # Layouts 
        layout = QGridLayout()
        layout.addWidget(self.label_0_0, 0, 0)
        layout.addWidget(picture_0_1, 0, 1)
        layout.addWidget(self.label_1_0, 2, 0)
        layout.addWidget(self.comboBox_2_0, 3, 0)
        layout.addWidget(self.label_3_0, 5, 0)
        layout.addWidget(self.input_4_0, 6, 0)
        layout.addWidget(self.button_4_1, 6, 1)
        layout.addWidget(self.label_5_0, 7, 0)
        layout.addWidget(self.input_6_0, 8, 0)
        layout.addWidget(self.button_6_1, 8, 1)
        layout.addWidget(self.label_7_0, 9, 0)
        layout.addWidget(self.input_8_0, 10, 0)
        layout.addWidget(self.button_8_1, 10, 1)
        layout.addWidget(self.label_9_0, 11, 0)
        layout.addWidget(self.input_10_0, 12, 0)
        layout.addWidget(self.button_10_1, 12, 1)
        layout.addWidget(emptyLabel, 13, 0) 

        self.setLayout(layout)

    # Functions for 
    def set_address(self):
        pass 

    # Functions for 
    def query_address(self):
        pass 

    # Functions for 
    def query_net(self):
        pass 

    # Functions for 
    def generate_protocol_params_file(self):
        pass     