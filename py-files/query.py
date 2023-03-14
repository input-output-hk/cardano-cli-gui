

import os
import time
import settings
import subprocess
import traceback
import common_functions

from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtWidgets import (QPushButton, QLabel, QLineEdit, 
                             QWidget, QGridLayout, QMessageBox,
                             QComboBox, QPlainTextEdit)

# Widgets and functions for the query tab
class Query(QWidget):
    def __init__(self):
        super().__init__()

        self.net = ""
        self.address = ""

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
        self.label_9_0 = QLabel("Show transaction hash for tx.signed file:")
        self.input_10_0 = QPlainTextEdit()
        self.button_10_1 = QPushButton("Show")

        # Action functions
        self.comboBox_2_0.addItems(["", "mainnet", "testnet"])
        self.comboBox_2_0.currentTextChanged.connect(self.set_net)

        self.button_4_1.clicked.connect(self.set_address)
        self.button_6_1.clicked.connect(self.query_address_funds)
        self.button_8_1.clicked.connect(self.query_net)
        self.button_10_1.clicked.connect(self.show_transaction)

        # Set label fonts 
        labels = [self.label_0_0, self.label_1_0,
                  self.label_3_0, self.label_5_0,
                  self.label_7_0, self.label_9_0]
        for label in labels:
            font = label.font()
            font.setPointSize(12)
            label.setFont(font)

        # Set lineEdit size 
        self.input_4_0.setFixedSize(500, 30)

        # Set plainTextEdit properties
        consolas_font = QFont()
        consolas_font.setFamily("Consolas")

        self.input_6_0.setFixedSize(500,230) 
        self.input_6_0.setFont(consolas_font)
        self.input_6_0.setLineWrapMode(QPlainTextEdit.LineWrapMode.NoWrap) 
        self.init_text = "                              TxHash                              TxIx          Amount\n" + \
                         "--------------------------------------------------------------------------------------------"
        self.input_6_0.setPlainText(self.init_text)

        self.input_8_0.setFixedSize(500,110) 
        self.input_8_0.setFont(consolas_font)
        self.input_8_0.setLineWrapMode(QPlainTextEdit.LineWrapMode.NoWrap) 
        self.input_8_0.setPlainText("")

        self.input_10_0.setFixedSize(500,60) 
        #self.input_10_0.setFont(consolas_font)
        self.input_10_0.setLineWrapMode(QPlainTextEdit.LineWrapMode.NoWrap) 
        self.input_10_0.setPlainText("")

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

    def set_net(self, selected_net):
        self.net = selected_net 

    def set_address(self):
        address_name = self.input_4_0.text()
        address_path = settings.folder_path + "/" + address_name
        address_exists = os.path.isfile(address_path)
        
        if not (".addr" in address_name):
            msg = "Address file has to have a .addr file extension name.\n" + \
                  "Please type in a file name with a .addr extension." 
            QMessageBox.warning(self, "Notification:", msg,
                                QMessageBox.Close)
            return None

        if not address_exists:
            msg = "Address file does not exists.\n" + \
                  "Please enter a valid file name." 
            QMessageBox.warning(self, "Notification:", msg,
                                QMessageBox.Close)
            return None

        with open(address_path, "r") as file:
            self.address = file.read()
        msg = "Address file successfully set."  
        QMessageBox.information(self, "Notification:", msg)

    def query_address_funds(self):
        if self.address == "":
            msg = "Address file not set.\n" + \
                  "Please set a valid file name."                   
            QMessageBox.warning(self, "Notification:", msg,
                                QMessageBox.Close)
            return None

        if self.net == "":
            msg = "Select option mainnet or testnet."    
            QMessageBox.warning(self, "Notification:", msg,
                                QMessageBox.Close)
            return None

        if self.net == "mainnet": 
            net_part =  "--mainnet "
        elif self.net == "testnet":
            net_part = "--testnet-magic " + settings.testnet_magic + " "
        
        command = "cardano-cli query utxo " + \
                  "--address " + self.address + " " + \
                  net_part 
        
        if settings.debug_mode:
            print("Command below is defined in py-files/query.py line 171:")
            print(common_functions.format_command(command) + "\n")
        else:
            try:
                response = subprocess.Popen(command.split(), stdout=subprocess.PIPE) 
                output = response.communicate()[0].decode("utf-8")
                self.input_6_0.setPlainText(output)
            except Exception:
                output = traceback.format_exc()
                common_functions.log_error_msg(output)
                
                msg = "Address could not be querried.\n" + \
                      "Check if cardano node is running and is synced.\n" + \
                      "Look at the error.log file for error output."                    
                QMessageBox.warning(self, "Notification:", msg,
                                    QMessageBox.Close)

    def query_net(self):
        if self.net == "":
            msg = "Select option mainnet or testnet."    
            QMessageBox.warning(self, "Notification:", msg,
                                QMessageBox.Close)
            return None

        if self.net == "mainnet": 
            net_part =  "--mainnet "
        elif self.net == "testnet":
            net_part = "--testnet-magic " + settings.testnet_magic + " "
        
        command = "cardano-cli query tip " + \
                  net_part 
        
        if settings.debug_mode:
            print("Command below is defined in py-files/query.py line 205:")
            print(common_functions.format_command(command) + "\n")
        else:
            try:
                response = subprocess.Popen(command.split(), stdout=subprocess.PIPE) 
                output = response.communicate()[0].decode("utf-8")
                self.input_8_0.setPlainText(output)
            except Exception:
                output = traceback.format_exc()
                common_functions.log_error_msg(output)
                
                msg = "Tip of net could not be querried.\n" + \
                      "Check if cardano node is running and is synced.\n" + \
                      "Look at the error.log file for error output." 
                QMessageBox.warning(self, "Notification:", msg,
                                    QMessageBox.Close)

    def show_transaction(self):
        tx_signed_path = settings.folder_path + "/" + "tx.signed"
        tx_signed_exists = os.path.isfile(tx_signed_path)

        if not tx_signed_exists:
            msg = "tx.signed file does not exists.\n" + \
                  "Please submit first a transaction." 
            QMessageBox.warning(self, "Notification:", msg,
                                QMessageBox.Close)
            return None

        command = "cardano-cli transaction txid --tx-file tx.signed"

        try:
            response = subprocess.Popen(command.split(), stdout=subprocess.PIPE, cwd=settings.folder_path) 
            # time.spleep(1) 
            output = response.communicate()[0].decode("utf-8")
            self.input_10_0.setPlainText("https://preview.cardanoscan.io/transaction/\n" + output)
        except Exception:
            output = traceback.format_exc()
            common_functions.log_error_msg(output)
            
            msg = "Signed transaction could not be querried.\n" + \
                  "Check if cardano node is running and is synced.\n" + \
                  "Look at the error.log file for error output." 
            QMessageBox.warning(self, "Notification:", msg,
                                QMessageBox.Close)