

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
class Smart_contracts_receive(QWidget):
    def __init__(self):
        super().__init__()

        # Creating local variables
        self.net = ""
        self.change_address = ""
        self.script_utxo = ""
        self.script_file_name = ""
        self.datum_file_type = ""
        self.datum_file_name = ""
        self.redeemer = ""
        self.collateral_utxo = ""
        self.signer_pkh = ""
        self.validity_type = ""
        self.validity_slot = ""
        self.protocol_parameter_file_name = ""
        self.skey_name = ""
        self.era = settings.current_era
        self.command_failed = False 

        # Header text 
        self.label_0_0 = QLabel("Receive funds from a cardano script address.")

        # Cardano picture
        picture_0_1 = QLabel("")
        picture_0_1.setPixmap(QPixmap("./images/cardano.png"))
        picture_0_1.setFixedSize(80,80)
        picture_0_1.setScaledContents(True)

        # Widgets for receiving funds from script address section 
        net_layout = QHBoxLayout()
        self.label_1_0_1 = QLabel("Select mainnet or testnet:")
        self.comboBox_1_0_2 = QComboBox()
        net_layout.addWidget(self.label_1_0_1)
        net_layout.addWidget(self.comboBox_1_0_2)
        self.label_2_0 = QLabel("Type in your change address name:")
        self.input_3_0 = QLineEdit()
        self.button_3_1 = QPushButton("Set")
        self.label_4_0 = QLabel("Transaction input UTxO from script address:")
        self.input_5_0 = QLineEdit()
        self.button_5_1 = QPushButton("Set")
        self.label_6_0 = QLabel("Type in script file name:")
        self.input_7_0 = QLineEdit()
        self.button_7_1 = QPushButton("Set")
        self.label_8_0 = QLabel("Chosse datum file type and type in file name:")
        datum_layout = QHBoxLayout()
        self.comboBox_9_0_1 = QComboBox()
        self.input_9_0_2 = QLineEdit()
        datum_layout.addWidget(self.comboBox_9_0_1)
        datum_layout.addWidget(self.input_9_0_2)
        self.button_9_1 = QPushButton("Set")
        self.label_10_0 = QLabel("Type in redeemer file name:")
        self.input_11_0 = QLineEdit()
        self.button_11_1 = QPushButton("Set")
        self.label_12_0 = QLabel("Colleteral UTxO from your receiving address:")
        self.input_13_0 = QLineEdit()
        self.button_13_1 = QPushButton("Set")
        self.label_14_0 = QLabel("Public key hash from receiving address:")
        self.input_15_0 = QLineEdit()
        self.button_15_1 = QPushButton("Set")
        self.label_16_0 = QLabel("Chosse validity interval type and type in time slot:")
        validity_layout = QHBoxLayout()
        self.comboBox_17_0_1 = QComboBox()
        self.input_17_0_2 = QLineEdit()
        validity_layout.addWidget(self.comboBox_17_0_1)
        validity_layout.addWidget(self.input_17_0_2)
        self.button_17_1 = QPushButton("Set")
        protocol_layout = QHBoxLayout()
        self.label_18_0_1 = QLabel("Type in protocol param file name:")
        self.input_18_0_2 = QLineEdit()
        protocol_layout.addWidget(self.label_18_0_1)
        protocol_layout.addWidget(self.input_18_0_2)
        self.button_18_1 = QPushButton("Set")
        signing_key_layout = QHBoxLayout()
        self.label_19_0_1 = QLabel("Type in signing key file name:")
        self.input_19_0_2 = QLineEdit()
        signing_key_layout.addWidget(self.label_19_0_1)
        signing_key_layout.addWidget(self.input_19_0_2)
        self.button_19_1 = QPushButton("Set")

        self.button_22_0 = QPushButton("Submit")

        # Widget actions for receiving funds from script address section 
        self.comboBox_1_0_2.addItems(["", "mainnet", "testnet"]) 
        self.comboBox_1_0_2.currentTextChanged.connect(self.set_net) 
        self.comboBox_9_0_1.addItems(["", "tx-out-datum-hash-file", 
                                       "tx-out-datum-embed-file", "tx-out-inline-datum-file"])
        self.comboBox_9_0_1.currentTextChanged.connect(self.set_datum_file_type)
        self.comboBox_17_0_1.addItems(["", "invalid-before", "invalid-hereafter"])
        self.comboBox_17_0_1.currentTextChanged.connect(self.set_validity_interval_type)

        self.button_3_1.clicked.connect(self.set_change_address)
        self.button_5_1.clicked.connect(self.set_script_utxo)
        self.button_7_1.clicked.connect(self.set_script_file)
        self.button_9_1.clicked.connect(self.set_datum)
        self.button_11_1.clicked.connect(self.set_redeemer)
        self.button_13_1.clicked.connect(self.set_colleteral_utxo)
        self.button_15_1.clicked.connect(self.set_pkh)
        self.button_17_1.clicked.connect(self.set_slot)
        self.button_18_1.clicked.connect(self.set_protocol_parameter)
        self.button_19_1.clicked.connect(self.set_skey_name)
        self.button_22_0.clicked.connect(self.submit_transaction)

        # Set label fonts and size 
        labels = [self.label_0_0, self.label_1_0_1, 
                  self.label_2_0, self.label_4_0, 
                  self.label_6_0, self.label_8_0, 
                  self.label_10_0, self.label_12_0, 
                  self.label_14_0, self.label_16_0, 
                  self.label_18_0_1, self.label_19_0_1] 
        for label in labels:
            font = label.font()
            font.setPointSize(12)
            label.setFont(font)

        self.label_1_0_1.setFixedSize(290, 35)
        self.label_18_0_1.setFixedSize(290, 35)
        self.label_19_0_1.setFixedSize(290, 35)

        # Set lineEdit sizes 
        inputs = [self.input_3_0, self.input_5_0, 
                  self.input_7_0, self.input_11_0, 
                  self.input_13_0, self.input_15_0]
        for input in inputs: 
            input.setFixedSize(500,30)

        self.input_9_0_2.setFixedSize(290, 30)
        self.input_17_0_2.setFixedSize(290, 30)
        self.input_18_0_2.setFixedSize(200, 30)
        self.input_19_0_2.setFixedSize(200, 30)

        # Set comboBox size
        self.comboBox_1_0_2.setFixedSize(200,30)
        self.comboBox_9_0_1.setFixedSize(200,30)
        self.comboBox_17_0_1.setFixedSize(200,30) 

        # Set button sizes 
        buttons = [self.button_3_1, self.button_5_1,
                   self.button_7_1, self.button_9_1, 
                   self.button_11_1, self.button_13_1, 
                   self.button_15_1, self.button_17_1,
                   self.button_18_1, self.button_19_1] 
        for button in buttons:
            button.setFixedSize(80,30)

        self.button_22_0.setFixedSize(160,30) 

        # Space between the sections
        self.emptyLabel = QLabel()

        # Layouts 
        layout = QGridLayout()
        layout.addWidget(self.label_0_0 , 0, 0)
        layout.addWidget(picture_0_1, 0, 1)
        # Adding widgets receiving funds from script address section 
        layout.addLayout(net_layout, 1, 0)
        layout.addWidget(self.label_2_0, 2, 0)
        layout.addWidget(self.input_3_0, 3, 0)
        layout.addWidget(self.button_3_1, 3, 1)
        layout.addWidget(self.label_4_0, 4, 0)
        layout.addWidget(self.input_5_0, 5, 0)
        layout.addWidget(self.button_5_1, 5, 1)
        layout.addWidget(self.label_6_0, 6, 0)
        layout.addWidget(self.input_7_0, 7, 0)
        layout.addWidget(self.button_7_1, 7, 1)
        layout.addWidget(self.label_8_0, 8, 0) 
        layout.addLayout(datum_layout, 9, 0) 
        layout.addWidget(self.button_9_1, 9, 1) 
        layout.addWidget(self.label_10_0, 10, 0) 
        layout.addWidget(self.input_11_0, 11, 0)
        layout.addWidget(self.button_11_1, 11, 1)
        layout.addWidget(self.label_12_0, 12, 0)
        layout.addWidget(self.input_13_0, 13, 0)
        layout.addWidget(self.button_13_1, 13, 1)
        layout.addWidget(self.label_14_0, 14, 0)
        layout.addWidget(self.input_15_0, 15, 0)
        layout.addWidget(self.button_15_1, 15, 1)
        layout.addWidget(self.label_16_0, 16, 0)
        layout.addLayout(validity_layout, 17, 0)
        layout.addWidget(self.button_17_1, 17, 1)
        layout.addLayout(protocol_layout, 18, 0)
        layout.addWidget(self.button_18_1, 18, 1)
        layout.addLayout(signing_key_layout, 19, 0)
        layout.addWidget(self.button_19_1, 19, 1)
        layout.addWidget(self.emptyLabel, 21, 0) 
        layout.addWidget(self.button_22_0, 22, 0) 

        self.setLayout(layout) 

    def set_validity_interval_type(self):
        pass

    def set_script_utxo(self):
        pass

    def set_redeemer(self):
        pass

    def set_colleteral_utxo(self):
        pass

    def set_pkh(self):
        pass

    def set_slot(self):
        pass

    def set_protocol_parameter(self):
        pass


    def set_script_file(self):
        script_file_name = self.input_2_0.text()
        script_file_path = settings.folder_path + "/" + script_file_name
        script_file_exists = os.path.isfile(script_file_path)
        
        if not script_file_exists:
            msg = "Script file does not exists.\n" + \
                  "Please enter a valid file name." 
            QMessageBox.warning(self, "Notification:", msg,
                                QMessageBox.Close) 
            return None

        if not (".plutus" in script_file_name):
            msg = "Script file has to have a .plutus file extension name.\n" + \
                  "Please type in a file name with a .plutus extension." 
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
                  "Please type in a file name with a .addr extension." 
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
            print("Command below is defined in py-files/smart_contracts.py line 241:")
            print(command + "\n") 
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
        if selected_net != "":
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
                  "Please type in a file name with a .addr extension." 
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
        
        if not skey_exists:
            msg = "Signing key file does not exists.\n" + \
                  "Please enter a valid file name."  
            QMessageBox.warning(self, "Notification:", msg,
                                QMessageBox.Close) 
            return None

        if not (".skey" in skey_name):
            msg = "Signing key has to have a .skey file extension name.\n" + \
                  "Please type in a file name with a .skey extension." 
            QMessageBox.warning(self, "Notification:", msg,
                                QMessageBox.Close)
            return None

        self.skey_name = skey_name
        msg = "Signing key file successfully set." 
        QMessageBox.information(self, "Notification:", msg)

    def set_utxo(self):
        utxo_input = self.input_18_0.text()
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
        if selected_datum_file_type != "":
            self.datum_file_type = selected_datum_file_type

    def set_datum(self):
        datum_file_name = self.input_20_0_2.text()
        datum_file_path = settings.folder_path + "/" + datum_file_name
        datum_file_exists = os.path.isfile(datum_file_path)

        if datum_file_name == "":
            self.datum_file_name = datum_file_name
            msg = "Datum file successfully unset."
            QMessageBox.information(self, "Notification:", msg)
            return None
        else:
            if not datum_file_exists:
                msg = "Datum file does not exists.\n" + \
                      "Please enter a valid file name." 
                QMessageBox.warning(self, "Notification:", msg,
                                    QMessageBox.Close) 
                return None

        if not (".json" in datum_file_name):
            msg = "Datum has to be a file in JSON fromat.\n" + \
                  "Please type in a name with a .json extension." 
            QMessageBox.warning(self, "Notification:", msg,
                                QMessageBox.Close)
            return None

        self.datum_file_name = datum_file_name 
        msg = "Datum file successfully set." 
        QMessageBox.information(self, "Notification:", msg)

    def submit_transaction(self): 
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
                print(" ".join(command) + "\n")
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

        if self.datum_file_name == "":
            datum_part = ""
        else:
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

        debug_msg_build = "Command below is defined in py-files/smart_contracts.py line 489:" 
        debug_msg_sign = "Command below is defined in py-files/smart_contracts.py line 503:" 
        debug_msg_submit = "Command below is defined in py-files/smart_contracts.py line 509:" 
                    
        manage_command(command_build_processed, msg_build, debug_msg_build)
        time.sleep(1)
        if not self.command_failed:
            manage_command(command_sign.split(), msg_sign, debug_msg_sign)
            time.sleep(1)
        if not self.command_failed:
            manage_command(command_submit.split(), msg_submit, debug_msg_submit) 
        if not self.command_failed and not settings.debug_mode:
            msg = "Send transaction successfully submitted."  
            QMessageBox.information(self, "Notification:", msg) 
        self.command_failed = False
