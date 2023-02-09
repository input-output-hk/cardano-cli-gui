

import os
import settings
import subprocess
import traceback

from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtWidgets import (QPushButton, QLabel, QLineEdit, 
                             QWidget, QGridLayout, QRadioButton,
                             QMessageBox, QPlainTextEdit)

class Transactions(QWidget):
    def __init__(self):
        super().__init__()

        # Creating local variables
        self.address = ""

        # Cardano picture
        picture_0_1 = QLabel("")
        picture_0_1.setPixmap(QPixmap("./images/cardano.png"))
        picture_0_1.setFixedSize(80,80)
        picture_0_1.setScaledContents(True)

        # Widgets for payment address section 
        self.label_1_0 = QLabel("Type in payment address name:")
        self.input_2_0 = QLineEdit()
        self.button_2_1 = QPushButton("Set")
        
        self.label_4_0 = QLabel("Funds for above payment address:")
        self.input_5_0 = QPlainTextEdit()
        self.button_5_1 = QPushButton("Querry\nfunds")
        self.radioButton_6_1 = QRadioButton("Mainnet")
        self.radioButton_7_1 = QRadioButton("Testnet")

        # Widget actions for payment address section
        self.button_2_1.clicked.connect(self.set_address_name)
        self.button_5_1.clicked.connect(self.querry_address_funds)

        # Widgets for sending funds section 
        self.label_8_0 = QLabel("Send follwing amount:")
        self.input_9_0 = QLineEdit()
        self.radioButton_9_1 = QRadioButton("Ada")
        self.label_10_0 = QLabel("NOTE: Seperat decimal number with dot.")
        self.radioButton_10_1 = QRadioButton("Lovelace")

        self.label_12_0 = QLabel("Input UTxO address:")
        self.input_13_0 = QLineEdit()
        self.button_13_1 = QPushButton("Set")
        self.label_14_0 = QLabel("Input receiving address:")
        self.input_15_0 = QLineEdit()
        self.button_15_1 = QPushButton("Set")

        self.button_17_0 = QPushButton("Send")

        # Set label fonts 
        labels = [self.label_1_0, self.label_4_0, 
                  self.label_8_0, self.label_10_0,
                  self.label_12_0, self.label_14_0]
        for label in labels:
            font = label.font()
            font.setPointSize(12)
            label.setFont(font)

        # Set lineEdit sizes 
        inputs = [self.input_2_0, self.input_9_0, 
                  self.input_13_0, self.input_15_0]
        for input in inputs:
            input.setFixedSize(500,30)

        # Set plainTextEdit properties
        self.input_5_0.setFixedSize(500,80) 
        consolas_font = QFont()
        consolas_font.setFamily("Consolas")
        self.input_5_0.setFont(consolas_font)

        self.input_5_0.setLineWrapMode(QPlainTextEdit.LineWrapMode.NoWrap) 
        # In pure Qt code the above line would translate to:
        # #include <QPlainTextEdit>
        # QPlainTextEdit plainText;
        # plainText.setLineWrapMode(QPlainTextEdit::LineWrapMode::NoWrap);

        self.init_text = "                              TxHash                              TxIx          Amount\n" + \
                         "--------------------------------------------------------------------------------------------"
        self.input_5_0.setPlainText(self.init_text)

        # Set button sizes         
        self.button_2_1.setFixedSize(80,30)
        self.button_5_1.setFixedSize(80,60)
        self.button_13_1.setFixedSize(80,30)
        self.button_15_1.setFixedSize(80,30)
        self.button_17_0.setFixedSize(160,30)

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
        layout.addWidget(self.radioButton_6_1, 6, 1)
        layout.addWidget(self.emptyLabel, 7, 0)
        layout.addWidget(self.radioButton_7_1, 7, 1)
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
        layout.addWidget(self.label_14_0, 14, 0)
        layout.addWidget(self.input_15_0, 15, 0)
        layout.addWidget(self.button_15_1, 15, 1)

        layout.addWidget(self.emptyLabel, 16, 0)
        layout.addWidget(self.button_17_0, 17, 0)
        layout.addWidget(self.emptyLabel, 18, 0)

        self.setLayout(layout)

    def set_address_name(self):
        address_name = self.input_2_0.text()
        address_path = settings.folder_path + "/" + address_name
        address_exists = os.path.isfile(address_path)
        
        if address_exists:
            with open(address_path, "r") as file:
                self.address = file.read()
        else:
            msg = "Address file does not exists.\n" + \
                  "Please specify a valid file name." 
            QMessageBox.warning(self, "Notification:", msg,
                                QMessageBox.Close)

    def querry_address_funds(self):
        if self.address == "":
            msg = "Address file not set.\n" + \
                  "Please set a valid file name."                   
            QMessageBox.warning(self, "Notification:", msg,
                                QMessageBox.Close)
        else:
            is_mainnet = self.radioButton_6_1.isChecked()
            is_testnet = self.radioButton_7_1.isChecked()

            if (not is_mainnet) and (not is_testnet):
                msg = "Select option mainnet or testnet."    
                QMessageBox.warning(self, "Notification:", msg,
                                    QMessageBox.Close)
            else:
                def handle_command(command):
                    if settings.debug_mode:
                        print(command)
                    else:
                        try:
                            response = subprocess.Popen(command.split(), cwd=settings.folder_path) 
                            output = response.communicate()[0]
                            self.input_5_0.setPlainText(output.decode("utf-8"))
                        except Exception:
                            output = traceback.format_exc()
                            log_error_msg(output)
                            
                            msg = "Address could not be querried.\n" + \
                                  "Check if cardano node is running."                    
                            QMessageBox.warning(self, "Notification:", msg,
                                                QMessageBox.Close)

                if is_testnet:
                    command = "cardano-cli query utxo " + \
                              "--address " + self.address + " " + \
                              "--testnet-magic 1097911063 " 
                    handle_command(command)
                elif is_mainnet:
                    command = "cardano-cli query utxo " + \
                              "--address " + self.address + " " + \
                              "--mainnet"
                    handle_command(command)

def log_error_msg(output):
    with open("./errors.log", "a") as file:
        file.write(output)
        file.write("\n-------------------------------------------------------------------\n\n")

