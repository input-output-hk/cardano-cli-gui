

import os
import time
import settings
import subprocess
import traceback
import common_functions

from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import (QPushButton, QLabel, QLineEdit, 
                             QWidget, QGridLayout, QRadioButton,
                             QComboBox, QMessageBox, QHBoxLayout)

# Widgets and functions for the smart contracts tab
class Smart_contracts_send(QWidget):
    def __init__(self):
        super().__init__()

        # Creating local variables
        self.script_file = ""
        self.script_address_file_name = ""
        self.net = ""

        self.change_address = ""
        self.skey_name = ""
        self.era = settings.current_era
        self.utxo = ""
        self.datum_file_name = ""
        self.datum_file_type = ""
        self.command_failed = False

        # Header text 
        self.label_0_0 = QLabel("Generate cardano script address and send funds to it.")  

        # Cardano picture
        picture_0_2 = QLabel("")
        picture_0_2.setPixmap(QPixmap("./images/cardano.png"))
        picture_0_2.setFixedSize(80,80)
        picture_0_2.setScaledContents(True)

        # Widgets for building script address section 
        self.label_1_0 = QLabel("Input script file name:")  
        self.input_2_0 = QLineEdit()
        self.button_2_1 = QPushButton("Set")
        self.label_3_0 = QLabel("Input or generate script address file name:")  
        self.input_4_0 = QLineEdit()
        self.button_4_1 = QPushButton("Set")
        self.button_4_2 = QPushButton("Generate")
        self.label_5_0 = QLabel("Select mainnet or testnet:")
        self.comboBox_6_0 = QComboBox()
        self.label_7_0 = QLabel("Show script address:")  
        self.input_8_0 = QLineEdit() 
        self.button_8_1 = QPushButton("Show")

        # Widget actions for building script address section  
        self.button_2_1.clicked.connect(self.set_script_file)
        self.button_4_1.clicked.connect(self.set_script_address_file)
        self.button_4_2.clicked.connect(self.generate_script_address_file)
        self.comboBox_6_0.addItems(["", "mainnet", "testnet"])
        self.comboBox_6_0.currentTextChanged.connect(self.set_net)
        self.button_8_1.clicked.connect(self.show_script_address)

        # Widgets for sending funds to script address section
        self.label_9_0 = QLabel("Input your address file name:")   
        self.input_10_0 = QLineEdit()
        self.button_10_1 = QPushButton("Set")
        self.label_11_0 = QLabel("Input signing key file name:")   
        self.input_12_0 = QLineEdit()
        self.button_12_1 = QPushButton("Set")
        self.label_13_0 = QLabel("Send amount (for ADA seperat decimal number with dot):")  
        self.input_14_0 = QLineEdit()
        self.radioButton_14_1 = QRadioButton("ADA")  
        self.radioButton_14_2 = QRadioButton("lovelace")   
        self.label_15_0 = QLabel("Input UTxO you want to spent:")  
        self.input_16_0 = QLineEdit()
        self.button_16_1 = QPushButton("Set")
        self.label_17_0 = QLabel("Chosse datum file type and input datum file name:")   

        datum_layout = QHBoxLayout()
        self.comboBox_18_0_1 = QComboBox()
        self.input_18_0_2 = QLineEdit()
        datum_layout.addWidget(self.comboBox_18_0_1)
        datum_layout.addWidget(self.input_18_0_2)
        self.button_18_1 = QPushButton("Set")

        self.button_20_0 = QPushButton("Send")
        self.button_20_1 = QPushButton("Set all")

        # Widget actions for building script address section  
        self.button_10_1.clicked.connect(self.set_change_address)
        self.button_12_1.clicked.connect(self.set_skey_name)
        self.button_16_1.clicked.connect(self.set_utxo)
        self.comboBox_18_0_1.addItems(["tx-out-datum-hash-file", 
                                       "tx-out-datum-embed-file", 
                                       "tx-out-inline-datum-file"])
        self.comboBox_18_0_1.currentTextChanged.connect(self.set_datum_file_type)
        self.button_18_1.clicked.connect(self.set_datum)
        self.button_20_0.clicked.connect(self.send_funds)
        self.button_20_1.clicked.connect(self.set_all)

        # Set label fonts 
        labels = [self.label_0_0, self.label_1_0, 
                  self.label_3_0, self.label_5_0, 
                  self.label_7_0, self.label_9_0, 
                  self.label_11_0, self.label_13_0, 
                  self.label_15_0, self.label_1_0, 
                  self.label_17_0] 
        for label in labels:
            font = label.font()
            font.setPointSize(12)
            label.setFont(font)

        # Set lineEdit sizes 
        inputs = [self.input_2_0, self.input_4_0, 
                  self.input_8_0, self.input_10_0, 
                  self.input_12_0, self.input_14_0,
                  self.input_16_0]
        for input in inputs: 
            input.setFixedSize(500,30)

        self.input_18_0_2.setFixedSize(290, 30)

        # Set comboBox size
        self.comboBox_6_0.setFixedSize(500,30)
        self.comboBox_18_0_1.setFixedSize(200,30)

        # Set button sizes 
        buttons = [self.button_2_1, self.button_4_1,
                   self.button_4_2, self.button_8_1, 
                   self.button_10_1, self.button_12_1, 
                   self.button_16_1, self.button_18_1,
                   self.button_20_1] 
        for button in buttons:
            button.setFixedSize(80,30)

        self.button_20_0.setFixedSize(160,30) 

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
        layout.addWidget(self.comboBox_6_0, 6, 0)
        layout.addWidget(self.label_7_0, 7, 0)
        layout.addWidget(self.input_8_0, 8, 0) 
        layout.addWidget(self.button_8_1, 8, 1) 
        # Adding widgets for sending funds to script address section 
        layout.addWidget(self.label_9_0, 9, 0) 
        layout.addWidget(self.input_10_0, 10, 0) 
        layout.addWidget(self.button_10_1, 10, 1)
        layout.addWidget(self.label_11_0, 11, 0)
        layout.addWidget(self.input_12_0, 12, 0)
        layout.addWidget(self.button_12_1, 12, 1)
        layout.addWidget(self.label_13_0, 13, 0)
        layout.addWidget(self.input_14_0, 14, 0)
        layout.addWidget(self.radioButton_14_1, 14, 1)
        layout.addWidget(self.radioButton_14_2, 14, 2)
        layout.addWidget(self.label_15_0, 15, 0)
        layout.addWidget(self.input_16_0, 16, 0)
        layout.addWidget(self.button_16_1, 16, 1)
        layout.addWidget(self.label_17_0, 17, 0)
        layout.addLayout(datum_layout, 18, 0)
        layout.addWidget(self.button_18_1, 18, 1)
        layout.addWidget(self.emptyLabel, 19, 0)
        layout.addWidget(self.button_20_0, 20, 0)
        layout.addWidget(self.button_20_1, 20, 1)
        layout.addWidget(self.emptyLabel, 21, 0) 

        self.setLayout(layout) 

    def set_script_file(self):
        script_file_name = self.input_2_0.text()
        script_file_path = settings.folder_path + "/" + script_file_name
        script_file_exists = os.path.isfile(script_file_path)

        if not (".plutus" in script_file_name):
            msg = "Script file has to have a .plutus file extension name.\n" + \
                  "Please enter a file name with a .plutus extension." 
            QMessageBox.warning(self, "Notification:", msg,
                                QMessageBox.Close)
            return None

        if not script_file_exists:
            msg = "Script file does not exists.\n" + \
                  "Please enter a valid file name." 
            QMessageBox.warning(self, "Notification:", msg,
                                QMessageBox.Close) 
            return None

        self.script_file = script_file_name
        msg = "Script file successfully set." 
        QMessageBox.information(self, "Notification:", msg)


    def set_script_address_file(self):
        script_address_file_name = self.input_4_0.text()
        script_address_file_path = settings.folder_path + "/" + script_address_file_name
        script_address_file_exists = os.path.isfile(script_address_file_path)

        if not (".addr" in script_address_file_name):
            msg = "Address file has to have a .addr file extension name.\n" + \
                  "Please enter a file name with a .addr extension." 
            QMessageBox.warning(self, "Notification:", msg,
                                QMessageBox.Close)
            return None

        if not script_address_file_exists:
            msg = "Script address file does not exists.\n" + \
                  "Please enter a valid file name." 
            QMessageBox.warning(self, "Notification:", msg,
                                QMessageBox.Close)
            return None

        self.script_address_file_name = script_address_file_name
        msg = "Script address file successfully set." 
        QMessageBox.information(self, "Notification:", msg)

    def generate_script_address_file(self):
        if self.script_file == "":
            msg = "Script file not set.\n" + \
                  "Please set a valid file name."                   
            QMessageBox.warning(self, "Notification:", msg,
                                QMessageBox.Close)
            return None
        
        if self.net == "":
            msg = "Select option mainnet or testnet."    
            QMessageBox.warning(self, "Notification:", msg,
                                QMessageBox.Close)
            return None

        script_address_file = self.script_file.split(".")[0] + ".addr"
        if os.path.isfile(script_address_file):
            msg = "Address file with same name as script file already exists.\n" + \
                  "Please delete it and try again to generate address file."    
            QMessageBox.warning(self, "Notification:", msg,
                                QMessageBox.Close)
            return None

        if self.net == "mainnet": 
            net_part =  "--mainnet "
        elif self.net == "testnet":
            net_part = "--testnet-magic " + settings.testnet_magic + " "
        
        command = "cardano-cli address build " + \
                  "--payment-script-file " + self.script_file + " " + \
                  net_part + \
                  "--out-file " + script_address_file
        
        if settings.debug_mode:
            print("Command for generating script address file:")  
            print(common_functions.format_command(command) + "\n")  
        else:
            try:
                subprocess.Popen(command.split(), cwd=settings.folder_path) 
                self.input_4_0.setText(script_address_file) 
                self.script_address_file_name = script_address_file
            except Exception:
                output = traceback.format_exc()
                common_functions.log_error_msg(output)
                
                msg = "Script address could not be generated.\n" + \
                      "Look at the error.log file for error output."                  
                QMessageBox.warning(self, "Notification:", msg,
                                    QMessageBox.Close)

    def set_net(self, selected_net):
        self.net = selected_net

    def show_script_address(self):
        script_address_file_path = settings.folder_path + "/" + self.script_address_file_name
        script_address_file_exists = os.path.isfile(script_address_file_path)
        
        if script_address_file_exists:
            with open(script_address_file_path, "r") as file:
                script_address = file.read()
            self.input_8_0.setText(script_address)
        else:
            msg = "Script address file does not exists.\n" + \
                  "If you have generated it, wait a couple of\n" + \
                  "seconds and try again to view the file."    
            QMessageBox.warning(self, "Notification:", msg,
                                QMessageBox.Close)

    def set_change_address(self): 
        change_address_name = self.input_10_0.text()
        change_address_path = settings.folder_path + "/" + change_address_name
        change_address_exists = os.path.isfile(change_address_path)

        if not (".addr" in change_address_name):
            msg = "Change address file has to have a .addr file extension name.\n" + \
                  "Please enter a file name with a .addr extension." 
            QMessageBox.warning(self, "Notification:", msg,
                                QMessageBox.Close)
            return None

        if not change_address_exists:
            msg = "Address file does not exists.\n" + \
                  "Please enter a valid file name." 
            QMessageBox.warning(self, "Notification:", msg,
                                QMessageBox.Close)
            return None

        with open(change_address_path, "r") as file:
            self.change_address = file.read()
        msg = "Change address file successfully set." 
        QMessageBox.information(self, "Notification:", msg)

    def set_skey_name(self):
        skey_name = self.input_12_0.text()
        skey_path = settings.folder_path + "/" + skey_name
        skey_exists = os.path.isfile(skey_path)
        
        if not (".skey" in skey_name):
            msg = "Signing key has to have a .skey file extension name.\n" + \
                  "Please enter a file name with a .skey extension." 
            QMessageBox.warning(self, "Notification:", msg,
                                QMessageBox.Close)
            return None

        if not skey_exists:
            msg = "Signing key file does not exists.\n" + \
                  "Please enter a valid file name."  
            QMessageBox.warning(self, "Notification:", msg,
                                QMessageBox.Close) 
            return None

        self.skey_name = skey_name
        msg = "Signing key file successfully set." 
        QMessageBox.information(self, "Notification:", msg)

    def set_utxo(self):
        utxo_input = self.input_16_0.text()
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
        msg = "UTxO address successfully set." 
        QMessageBox.information(self, "Notification:", msg)

    def set_datum_file_type(self, selected_datum_file_type):
        self.datum_file_type = selected_datum_file_type

    def set_datum(self):
        datum_file_name = self.input_18_0_2.text()
        datum_file_path = settings.folder_path + "/" + datum_file_name
        datum_file_exists = os.path.isfile(datum_file_path)

        if not datum_file_exists:
            msg = "Datum file does not exists.\n" + \
                    "Please enter a valid file name." 
            QMessageBox.warning(self, "Notification:", msg,
                                QMessageBox.Close) 
            return None

        if not (".json" in datum_file_name):
            msg = "Datum has to be a file in JSON fromat.\n" + \
                  "Please enter a name with a .json extension." 
            QMessageBox.warning(self, "Notification:", msg,
                                QMessageBox.Close)
            return None

        self.datum_file_name = datum_file_name 
        msg = "Datum file successfully set." 
        QMessageBox.information(self, "Notification:", msg)

    def set_all(self):
        self.set_script_file()
        self.set_script_address_file()
        self.set_change_address()
        self.set_skey_name()
        self.set_utxo()
        self.set_datum()

    def send_funds(self): 
        if self.script_address_file_name == "":
            msg = "Please set the receiving script address.\n" + \
                  "If you have generated it, wait for couple of\n" + \
                  "seconds and then try again to send the funds." 
            QMessageBox.warning(self, "Notification:", msg,
                                QMessageBox.Close)
            return None
        else:
            script_address_file_path = settings.folder_path + "/" + self.script_address_file_name
            with open(script_address_file_path, "r") as file:
                self.script_address = file.read()

        if self.net == "":
            msg = "Select option mainnet or testnet."    
            QMessageBox.warning(self, "Notification:", msg,
                                QMessageBox.Close)
            return None

        if self.change_address == "":
            msg = "Please set a valid change address." 
            QMessageBox.warning(self, "Notification:", msg,
                                QMessageBox.Close)
            return None

        if self.skey_name == "":
            msg = "Please set a valid signing key." 
            QMessageBox.warning(self, "Notification:", msg,
                                QMessageBox.Close)
            return None
        
        is_ada = self.radioButton_14_1.isChecked()
        is_lovelace = self.radioButton_14_2.isChecked()

        if (not is_ada) and (not is_lovelace):
            msg = "Select option ada or lovelace."    
            QMessageBox.warning(self, "Notification:", msg,
                                QMessageBox.Close)
            return None

        if is_ada:
            currency = "ADA"
        elif is_lovelace: 
            currency = "Lovelace"
        amount_text = self.input_14_0.text() 
        amount_in_lovelace = common_functions.parse_amount(amount_text, currency)

        if amount_in_lovelace == -1:
            msg = "The specified amount in " + currency + " is not a valid input.\n" + \
                  "Amount in ADA can have max 6 decimal numbers.\nSpaces and characters are not allowed." 
            QMessageBox.warning(self, "Notification:", msg,
                                QMessageBox.Close)
            return None

        if self.utxo == "":
            msg = "Please set a valid UTxO transaction input." 
            QMessageBox.warning(self, "Notification:", msg,
                                QMessageBox.Close)
            return None

        if self.datum_file_type == "":
            msg = "Please set a valid datum file type." 
            QMessageBox.warning(self, "Notification:", msg,
                                QMessageBox.Close) 
            return None

        if self.datum_file_name == "":
            msg = "Please set a valid datum file name." 
            QMessageBox.warning(self, "Notification:", msg,
                                QMessageBox.Close)
            return None

        def manage_command(command, msg, debug_msg):
            if settings.debug_mode:
                print(debug_msg)
                commad_single_string = " ".join(command)
                print(common_functions.format_command(commad_single_string) + "\n")
            else:
                try:
                    subprocess.Popen(command, cwd=settings.folder_path)
                except Exception:
                    output = traceback.format_exc()
                    common_functions.log_error_msg(output)                   
                    QMessageBox.warning(self, "Notification:", msg,
                                        QMessageBox.Close)
                    self.command_failed = True

        if self.net == "mainnet":
            net_part = "--mainnet "
            split_number = 8
        elif self.net == "testnet": 
            net_part = "--testnet-magic " + settings.testnet_magic + " "
            split_number = 9

        datum_part = "--" + self.datum_file_type + " " + self.datum_file_name + " "

        command_build = "cardano-cli transaction build " + \
                        "--" + self.era + " " + \
                        net_part + \
                        "--tx-in " + self.utxo + " " + \
                        "--tx-out " + self.script_address + " " + str(amount_in_lovelace) + " lovelace " + \
                        datum_part + \
                        "--change-address " + self.change_address + " " + \
                        "--out-file tx.body"
        command_build_parts = command_build.split()
        # The receiving address, lovelace amount and lovelace string have to be passed as one string parameter
        command_build_processed = command_build_parts[0:split_number] + \
                                  [" ".join(command_build_parts[split_number:(split_number + 3)])] + \
                                  command_build_parts[(split_number + 3):]

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

        debug_msg_build = "Command for building a transaction:"  
        debug_msg_sign = "Command for signing a transaction:"  
        debug_msg_submit = "Command for submitting a transaction:"  
                    
        manage_command(command_build_processed, msg_build, debug_msg_build)
        time.sleep(1)
        if not self.command_failed:
            manage_command(command_sign.split(), msg_sign, debug_msg_sign)
            time.sleep(1)
        if not self.command_failed:
            manage_command(command_submit.split(), msg_submit, debug_msg_submit) 
        if not self.command_failed and not settings.debug_mode:
            msg = "Commads successfully executed.\n" + \
                  "Look at console output for transaction info."   
            QMessageBox.information(self, "Notification:", msg) 
        self.command_failed = False