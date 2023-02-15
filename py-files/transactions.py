

import os
import settings
import subprocess
import traceback
import common_functions

from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtWidgets import (QPushButton, QLabel, QLineEdit, 
                             QWidget, QGridLayout, QRadioButton,
                             QMessageBox, QPlainTextEdit, QComboBox)

# Widgets and functions for the transactions tab
class Transactions(QWidget):
    def __init__(self):
        super().__init__()

        # Creating local variables
        self.address = ""
        self.skey_name = ""
        self.net = ""
        self.era = ""
        self.utxo = ""
        self.receiving_address = ""
        self.command_failed = False

        # Intro text and cardano picture
        self.label_0_0 = QLabel("Send funds from your address to another one.")
        picture_0_1 = QLabel("")
        picture_0_1.setPixmap(QPixmap("./images/cardano.png"))
        picture_0_1.setFixedSize(80,80)
        picture_0_1.setScaledContents(True)

        # Widgets for payment address section 
        self.label_1_0 = QLabel("Type in your address name (will be also used as change address):")
        self.input_2_0 = QLineEdit()
        self.button_2_1 = QPushButton("Set")
        self.label_3_0 = QLabel("Type in your signing key name:")
        self.input_4_0 = QLineEdit()
        self.button_4_1 = QPushButton("Set")
        self.label_5_0 = QLabel("Funds for above payment address:")
        self.input_6_0 = QPlainTextEdit()
        self.button_6_1 = QPushButton("Querry\nfunds")
        self.label_7_0 = QLabel("Select mainnet or testnet:")
        self.comboBox_8_0 = QComboBox()

        # Widget actions for payment address section
        self.button_2_1.clicked.connect(self.set_address_name)
        self.button_4_1.clicked.connect(self.set_skey_name)
        self.button_6_1.clicked.connect(self.querry_address_funds)

        self.comboBox_8_0.addItems(["", "mainnet", "testnet"])
        self.comboBox_8_0.currentTextChanged.connect(self.set_net)

        # Widgets for sending funds section 
        self.label_9_0 = QLabel("Send amount (seperat decimal number with dot):")
        self.radioButton_9_1 = QRadioButton("Ada")
        self.input_10_0 = QLineEdit()
        self.radioButton_10_1 = QRadioButton("Lovelace")
        self.label_11_0 = QLabel("Select era:")
        self.comboBox_12_0 = QComboBox()
        self.label_13_0 = QLabel("Input UTxO address:")
        self.input_14_0 = QLineEdit()
        self.button_14_1 = QPushButton("Set")
        self.label_15_0 = QLabel("Input receiving address:")
        self.input_16_0 = QLineEdit()
        self.button_16_1 = QPushButton("Set")
        self.button_18_0 = QPushButton("Send")

        # Widget actions for sending funds section 
        self.button_14_1.clicked.connect(self.set_utxo)
        self.button_16_1.clicked.connect(self.set_receiving_address)
        self.button_18_0.clicked.connect(self.send_funds)

        self.comboBox_12_0.addItems(["", "byron-era", "shelley-era", "allegra-era", "mary-era", "alonzo-era", "babbage-era"])
        self.comboBox_12_0.currentTextChanged.connect(self.update_era)

        # Set label fonts 
        labels = [self.label_0_0, self.label_1_0, 
                  self.label_3_0, self.label_5_0,
                  self.label_7_0, self.label_9_0, 
                  self.label_11_0, self.label_13_0, 
                  self.label_15_0]
        for label in labels:
            font = label.font()
            font.setPointSize(12)
            label.setFont(font)

        # Set lineEdit sizes 
        inputs = [self.input_2_0, self.input_4_0, 
                  self.input_6_0, self.input_10_0,
                  self.input_14_0, self.input_16_0]
        for input in inputs:
            input.setFixedSize(500,30)

        # Set plainTextEdit properties
        self.input_6_0.setFixedSize(500,80) 
        consolas_font = QFont()
        consolas_font.setFamily("Consolas")
        self.input_6_0.setFont(consolas_font)

        self.input_6_0.setLineWrapMode(QPlainTextEdit.LineWrapMode.NoWrap) 
        # In pure Qt code the above line would translate to:
        # #include <QPlainTextEdit>
        # QPlainTextEdit plainText;
        # plainText.setLineWrapMode(QPlainTextEdit::LineWrapMode::NoWrap);

        self.init_text = "                              TxHash                              TxIx          Amount\n" + \
                         "--------------------------------------------------------------------------------------------"
        self.input_6_0.setPlainText(self.init_text)

        # Set button sizes         
        self.button_2_1.setFixedSize(80,30)
        self.button_4_1.setFixedSize(80,30)
        self.button_6_1.setFixedSize(80,60)
        self.button_14_1.setFixedSize(80,30)
        self.button_16_1.setFixedSize(80,30)
        self.button_18_0.setFixedSize(160,30)

        # Space between the sections
        self.emptyLabel = QLabel()

        # Layouts 
        layout = QGridLayout()
        # Intro widgets
        layout.addWidget(self.label_0_0, 0, 0)
        layout.addWidget(picture_0_1, 0, 1)
        # Adding widgets for payment address section 
        layout.addWidget(self.label_1_0, 1, 0)
        layout.addWidget(self.input_2_0, 2, 0)
        layout.addWidget(self.button_2_1, 2, 1)
        layout.addWidget(self.label_3_0, 3, 0)
        layout.addWidget(self.input_4_0, 4, 0)
        layout.addWidget(self.button_4_1, 4, 1)
        layout.addWidget(self.label_5_0, 5, 0)
        layout.addWidget(self.input_6_0, 6, 0)
        layout.addWidget(self.button_6_1, 6, 1)
        layout.addWidget(self.label_7_0, 7, 0)
        layout.addWidget(self.comboBox_8_0, 8, 0)
        layout.addWidget(self.emptyLabel, 7, 0)
        layout.addWidget(self.emptyLabel, 8, 0)
        # Adding widgets for payment address section 
        layout.addWidget(self.label_9_0, 9, 0)
        layout.addWidget(self.radioButton_9_1, 9, 1)
        layout.addWidget(self.input_10_0, 10, 0)
        layout.addWidget(self.radioButton_10_1, 10, 1)
        layout.addWidget(self.label_11_0, 11, 0)
        layout.addWidget(self.comboBox_12_0, 12, 0)
        layout.addWidget(self.label_13_0, 13, 0)
        layout.addWidget(self.input_14_0, 14, 0)
        layout.addWidget(self.button_14_1, 14, 1)
        layout.addWidget(self.label_15_0, 15, 0)
        layout.addWidget(self.input_16_0, 16, 0)
        layout.addWidget(self.button_16_1, 16, 1)
        layout.addWidget(self.emptyLabel, 17, 0)
        layout.addWidget(self.button_18_0, 18, 0)
        layout.addWidget(self.emptyLabel, 19, 0)

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
                  "Please enter a valid file name." 
            QMessageBox.warning(self, "Notification:", msg,
                                QMessageBox.Close)

    def set_skey_name(self):
        skey_name = self.input_4_0.text()
        skey_path = settings.folder_path + "/" + skey_name
        skey_exists = os.path.isfile(skey_path)
        
        if skey_exists:
            self.skey_name = skey_name
        else:
            msg = "Signing key file does not exists.\n" + \
                  "Please enter a valid file name."  
            QMessageBox.warning(self, "Notification:", msg,
                                QMessageBox.Close) 

    def querry_address_funds(self):
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
            print("Command below is defined in py-files/transactions.py line 208:")
            print(command)
        else:
            try:
                response = subprocess.Popen(command.split(), cwd=settings.folder_path) 
                output = response.communicate()[0]
                self.input_6_0.setPlainText(output.decode("utf-8"))
            except Exception:
                output = traceback.format_exc()
                common_functions.log_error_msg(output)
                
                msg = "Address could not be querried.\n" + \
                      "Check if cardano node is running and is synced.\n" + \
                      "Look at the error.log file for error output."                    
                QMessageBox.warning(self, "Notification:", msg,
                                    QMessageBox.Close)

    def set_net(self, selected_net):
        if selected_net != "":
            self.net = selected_net 

    def update_era(self, selected_era):
        if selected_era != "":
            self.era = selected_era

    def set_utxo(self):
        utxo_input = self.input_14_0.text()
        if not ("#" in utxo_input):
            msg = "UTxO transaction input has to contain # sign and transaction index." + \
                  "Please enter a valid transaction input." 
            QMessageBox.warning(self, "Notification:", msg,
                                QMessageBox.Close)
            return None

        trans_hash = utxo_input.split("#")[0]
        if len(trans_hash) != 64:
            msg = "UTxO transaction hash has to be 64 characters long." + \
                  "Please enter a valid transaction hash." 
            QMessageBox.warning(self, "Notification:", msg,
                                QMessageBox.Close)
            return None

        self.utxo = utxo_input 

    def set_receiving_address(self):
        receiving_address_name = self.input_16_0.text()
        receiving_address_path = settings.folder_path + "/" + receiving_address_name
        receiving_address_exists = os.path.isfile(receiving_address_path)
        
        if receiving_address_exists:
            with open(receiving_address_path, "r") as file:
                self.receiving_address = file.read()
        else:
            msg = "Receiving address does not exists.\n" + \
                  "Please enter a valid file name."                       
            QMessageBox.warning(self, "Notification:", msg,
                                QMessageBox.Close)

    def send_funds(self): 
        if self.address == "":
            msg = "Please set a valid change address." 
            QMessageBox.warning(self, "Notification:", msg,
                                QMessageBox.Close)
            return None

        if self.skey_name == "":
            msg = "Please set a valid signing key." 
            QMessageBox.warning(self, "Notification:", msg,
                                QMessageBox.Close)
            return None

        if self.net == "":
            msg = "Select option mainnet or testnet."    
            QMessageBox.warning(self, "Notification:", msg,
                                QMessageBox.Close)
            return None

        is_ada = self.radioButton_9_1.isChecked()
        is_lovelace = self.radioButton_10_1.isChecked()

        if (not is_ada) and (not is_lovelace):
            msg = "Select option ada or lovelace."    
            QMessageBox.warning(self, "Notification:", msg,
                                QMessageBox.Close)
            return None

        if is_ada:
            currency = "ADA"
        elif is_lovelace: 
            currency = "Lovelace"
        
        amount_text = self.input_10_0.text() 
        amount_in_lovelace = common_functions.parse_amount(amount_text, currency)

        if amount_in_lovelace == -1:
            msg = "The specified amount in " + currency + " is not a valid input.\n" + \
                  "Amount in ADA can have max 6 decimal numbers.\n" + \
                  "Spaces and characters are not allowed." 
            QMessageBox.warning(self, "Notification:", msg,
                                QMessageBox.Close)
            return None

        if self.era == "":
            msg = "Please select an era." 
            QMessageBox.warning(self, "Notification:", msg,
                                QMessageBox.Close)
            return None

        if self.utxo == "":
            msg = "Please set a valid UTxO transaction input." 
            QMessageBox.warning(self, "Notification:", msg,
                                QMessageBox.Close)
            return None

        if self.receiving_address == "":
            msg = "Please set the receiving address." 
            QMessageBox.warning(self, "Notification:", msg,
                                QMessageBox.Close)
            return None

        def manage_command(command, msg, debug_msg):
            if settings.debug_mode:
                print(debug_msg)
                print(command)
            else:
                try:
                    subprocess.Popen(command.split(), cwd=settings.folder_path)
                except Exception:
                    output = traceback.format_exc()
                    common_functions.log_error_msg(output)                   
                    QMessageBox.warning(self, "Notification:", msg,
                                        QMessageBox.Close)
                    self.command_failed = True

        if self.net == "mainnet":
            net_part = "--mainnet "
        elif self.net == "testnet": 
            net_part = "--testnet-magic " + settings.testnet_magic + " "

        command_build = "cardano-cli transaction build " + \
                        "--" + self.era + " " + \
                        net_part + \
                        "--tx-in " + self.utxo + " " + \
                        "--tx-out " + self.receiving_address + " " + str(amount_in_lovelace) + " lovelace " + \
                        "--change-address " + self.address + " " + \
                        "--out-file tx.body"
        command_sign = "cardano-cli transaction sign " + \
                        "--tx-body-file tx.body " + \
                        "--signing-key-file " + self.skey_name + " " + \
                        net_part + \
                        "--out-file tx.signed" 
        command_submit = "cardano-cli transaction submit " + \
                         net_part + \
                         "--tx-file tx.signed"

        msg_common = "Check if cardano node is running and is synced.\n" + \
                     "Look at the error.log file for error output." 
        msg_build = "Transaction build command failed.\n" + msg_common
        msg_sign = "Transaction sign command failed.\n" + msg_common
        msg_submit = "Transaction submit command failed.\n" + msg_common

        debug_msg_build = "Command below is defined in py-files/transactions.py line 352:"
        debug_msg_sign = "Command below is defined in py-files/transactions.py line 359:"
        debug_msg_submit = "Command below is defined in py-files/transactions.py line 364:" 
                    
        manage_command(command_build, msg_build, debug_msg_build)
        if not self.command_failed:
            manage_command(command_sign, msg_sign, debug_msg_sign)
            os.remove(settings.folder_path + "/tx.body")
        if not self.command_failed:
            manage_command(command_submit, msg_submit, debug_msg_submit)
            os.remove(settings.folder_path + "/tx.signed")
