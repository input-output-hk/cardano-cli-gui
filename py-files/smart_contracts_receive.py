

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
        self.label_4_0 = QLabel("Type in transaction input UTxO from script address:")
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
        self.label_12_0 = QLabel("Type in colleteral UTxO from your receiving address:")
        self.input_13_0 = QLineEdit()
        self.button_13_1 = QPushButton("Set")
        self.label_14_0 = QLabel("Type in public key hash file name from receiving address:")
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
        self.button_22_1 = QPushButton("Set all")

        # Widget actions for receiving funds from script address section 
        self.comboBox_1_0_2.addItems(["", "mainnet", "testnet"]) 
        self.comboBox_1_0_2.currentTextChanged.connect(self.set_net) 
        self.comboBox_9_0_1.addItems(["", 
                                      "tx-in-datum-cbor-file", 
                                      "tx-in-datum-file", 
                                      "tx-in-datum-value", 
                                      "tx-in-inline-datum-present"])
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
        self.button_22_1.clicked.connect(self.set_all)

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
                   self.button_18_1, self.button_19_1,
                   self.button_22_1] 
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
        layout.addWidget(self.button_22_1, 22, 1) 

        self.setLayout(layout) 

    def set_net(self, selected_net):
        self.net = selected_net

    def set_datum_file_type(self, selected_datum_file_type):
        self.datum_file_type = selected_datum_file_type

    def set_validity_interval_type(self, validity_int_type):
        self.validity_type = validity_int_type

    def set_change_address(self): 
        change_address_name = self.input_3_0.text()
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

    def set_script_utxo(self):
        utxo_input = self.input_5_0.text()
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

        self.script_utxo = utxo_input 
        msg = "UTxO script input successfully set." 
        QMessageBox.information(self, "Notification:", msg)

    def set_script_file(self):
        script_file_name = self.input_7_0.text()
        script_file_path = settings.folder_path + "/" + script_file_name
        script_file_exists = os.path.isfile(script_file_path)
        
        if not (".plutus" in script_file_name):
            msg = "Script file has to have a .plutus file extension name.\n" + \
                  "Please type in a file name with a .plutus extension." 
            QMessageBox.warning(self, "Notification:", msg,
                                QMessageBox.Close)
            return None

        if not script_file_exists:
            msg = "Script file does not exists.\n" + \
                  "Please enter a valid file name." 
            QMessageBox.warning(self, "Notification:", msg,
                                QMessageBox.Close) 
            return None

        self.script_file_name = script_file_name
        msg = "Script file successfully set." 
        QMessageBox.information(self, "Notification:", msg)

    def set_datum(self):
        datum_file_name = self.input_9_0_2.text()
        datum_file_path = settings.folder_path + "/" + datum_file_name
        datum_file_exists = os.path.isfile(datum_file_path)

        if self.datum_file_type == "":
            msg = "Select first datum file type."
            QMessageBox.warning(self, "Notification:", msg,
                                        QMessageBox.Close)
            return None
        
        if datum_file_name == "" and self.datum_file_type != "tx-in-inline-datum-present":
            msg = "Specify a valid datum file."
            QMessageBox.warning(self, "Notification:", msg,
                                        QMessageBox.Close)
            return None
        
        if datum_file_name == "" and self.datum_file_type == "tx-in-inline-datum-present":
            self.datum_file_name = ""
            msg = "Inline datum present option successfully set." 
            QMessageBox.information(self, "Notification:", msg)
            return None

        if not datum_file_exists:
            msg = "Datum file does not exists.\n" + \
                  "Please enter a valid file name." 
            QMessageBox.warning(self, "Notification:", msg,
                                QMessageBox.Close) 
            return None

        self.datum_file_name = datum_file_name + " "
        msg = "Datum file successfully set." 
        QMessageBox.information(self, "Notification:", msg)

    def set_redeemer(self):
        redeemer_file_name = self.input_11_0.text()
        redeemer_file_path = settings.folder_path + "/" + redeemer_file_name
        redeemer_file_exists = os.path.isfile(redeemer_file_path)

        if redeemer_file_name == "":
            self.redeemer = redeemer_file_name
            msg = "Redeemer file successfully unset."
            QMessageBox.information(self, "Notification:", msg)
            return None
        else:
            if not (".json" in redeemer_file_name):
                msg = "Redeemer has to be a file in JSON fromat.\n" + \
                      "Please type in a name with a .json extension." 
                QMessageBox.warning(self, "Notification:", msg,
                                    QMessageBox.Close)
                return None

            if not redeemer_file_exists:
                msg = "Redeemer file does not exists.\n" + \
                      "Please enter a valid file name." 
                QMessageBox.warning(self, "Notification:", msg,
                                    QMessageBox.Close) 
                return None

        self.redeemer = redeemer_file_name 
        msg = "Redeemer file successfully set." 
        QMessageBox.information(self, "Notification:", msg)

    def set_colleteral_utxo(self):
        utxo_input = self.input_13_0.text()
        if not ("#" in utxo_input):
            msg = "UTxO transaction input has to contain # sign and transaction index." + \
                  "Please enter a valid transaction input." 
            QMessageBox.warning(self, "Notification:", msg,
                                QMessageBox.Close)
            return None

        trans_hash = utxo_input.split("#")[0]
        if len(trans_hash) != 64: 
            msg = "UTxO transaction hash has to be 64 characters long.\n" + \
                  "Please enter a valid transaction hash." 
            QMessageBox.warning(self, "Notification:", msg,
                                QMessageBox.Close)
            return None

        self.collateral_utxo = utxo_input 
        msg = "UTxO script input successfully set." 
        QMessageBox.information(self, "Notification:", msg)

    def set_pkh(self):
        pkh_name = self.input_15_0.text()
        pkh_path = settings.folder_path + "/" + pkh_name
        pkh_exists = os.path.isfile(pkh_path)
        
        if not (".pkh" in pkh_name):
            msg = "Public key hash has to have a .pkh file extension name.\n" + \
                  "Please type in a file name with a .pkh extension." 
            QMessageBox.warning(self, "Notification:", msg,
                                QMessageBox.Close)
            return None

        if not pkh_exists:
            msg = "Public key hash does not exists.\n" + \
                  "Please specify a valid file name."                        
            QMessageBox.warning(self, "Notification:", msg,
                                QMessageBox.Close)
            return None

        with open(pkh_path, "r") as file:
            self.signer_pkh = file.read()
        msg = "Public key hash file successfully set."  
        QMessageBox.information(self, "Notification:", msg)

    def set_slot(self):
        slot = self.input_17_0_2.text()

        if not slot.isdigit():
            msg = "Slot has to be an integer number grater than zero."                        
            QMessageBox.warning(self, "Notification:", msg,
                                QMessageBox.Close)
            return None

        self.validity_slot = slot
        msg = "Slot successfully set."  
        QMessageBox.information(self, "Notification:", msg)

    def set_protocol_parameter(self):
        pp_file_name = self.input_18_0_2.text()
        pp_file_path = settings.folder_path + "/" + pp_file_name
        pp_file_exists = os.path.isfile(pp_file_path)

        if pp_file_name == "":
            self.protocol_parameter_file_name = pp_file_name
            msg = "Protocol parameter file successfully unset."
            QMessageBox.information(self, "Notification:", msg)
            return None
        else:
            if not (".json" in pp_file_name):
                msg = "Protocol parameter has to be a file in JSON fromat.\n" + \
                      "Please type in a name with a .json extension." 
                QMessageBox.warning(self, "Notification:", msg,
                                    QMessageBox.Close)
                return None

            if not pp_file_exists:
                msg = "Protocol parameter file does not exists.\n" + \
                      "Please enter a valid file name." 
                QMessageBox.warning(self, "Notification:", msg,
                                    QMessageBox.Close) 
                return None

        self.protocol_parameter_file_name = pp_file_name 
        msg = "Protocol parameter file successfully set." 
        QMessageBox.information(self, "Notification:", msg)

    def set_skey_name(self):
        skey_name = self.input_19_0_2.text()
        skey_path = settings.folder_path + "/" + skey_name
        skey_exists = os.path.isfile(skey_path)

        if not (".skey" in skey_name):
            msg = "Signing key has to have a .skey file extension name.\n" + \
                  "Please type in a file name with a .skey extension." 
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

    def set_all(self):
        self.set_change_address()
        self.set_script_utxo()
        self.set_script_file()
        self.set_datum()
        self.set_redeemer()
        self.set_colleteral_utxo()
        self.set_pkh()
        self.set_slot()
        self.set_protocol_parameter()
        self.set_skey_name()

    def submit_transaction(self): 
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

        if self.script_utxo == "":
            msg = "Please set a valid script UTxO transaction input." 
            QMessageBox.warning(self, "Notification:", msg,
                                QMessageBox.Close)
            return None

        if self.script_file_name == "":
            msg = "Please set the .plutus script file name." 
            QMessageBox.warning(self, "Notification:", msg,
                                QMessageBox.Close)
            return None

        if self.datum_file_type == "":
            msg = "Please set datum file type." 
            QMessageBox.warning(self, "Notification:", msg,
                                QMessageBox.Close)
            return None

        if self.datum_file_name == "" and self.datum_file_type != "tx-in-inline-datum-present":
            msg = "Please set datum file name." 
            QMessageBox.warning(self, "Notification:", msg,
                                QMessageBox.Close)
            return None

        if self.redeemer == "":
            msg = "Please set redeemer file name." 
            QMessageBox.warning(self, "Notification:", msg,
                                QMessageBox.Close)
            return None

        if self.collateral_utxo == "":
            msg = "Please set a valid collateral UTxO transaction input." 
            QMessageBox.warning(self, "Notification:", msg,
                                QMessageBox.Close)
            return None

        if self.signer_pkh == "":
            msg = "Please set a valid signing key file name." 
            QMessageBox.warning(self, "Notification:", msg,
                                QMessageBox.Close)
            return None

        if self.validity_type == "":
            msg = "Please set a validity type." 
            QMessageBox.warning(self, "Notification:", msg,
                                QMessageBox.Close)
            return None

        if self.validity_slot == "":
            msg = "Please set a valid slot." 
            QMessageBox.warning(self, "Notification:", msg,
                                QMessageBox.Close)
            return None

        if self.protocol_parameter_file_name == "":
            msg = "Please set a valid protocol parameter file name." 
            QMessageBox.warning(self, "Notification:", msg,
                                QMessageBox.Close)
            return None

        if self.skey_name == "":
            msg = "Please set a valid signing key." 
            QMessageBox.warning(self, "Notification:", msg,
                                QMessageBox.Close)
            return None

        def manage_command(command, msg, debug_msg):
            if settings.debug_mode:
                print(debug_msg)
                print(common_functions.format_command(command) + "\n")
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
                        "--tx-in " + self.script_utxo + " " + \
                        "--tx-in-script-file " + self.script_file_name + " " + \
                        "--" + self.datum_file_type + " " + self.datum_file_name + \
                        "--tx-in-redeemer-file " + self.redeemer + " " + \
                        "--tx-in-collateral " + self.collateral_utxo + " " + \
                        "--required-signer-hash " + self.signer_pkh + " " + \
                        "--change-address " + self.change_address + " " + \
                        "--" + self.validity_type + " " + self.validity_slot + " " + \
                        "--protocol-params-file " + self.protocol_parameter_file_name + " " + \
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

        debug_msg_build = "Command below is defined in py-files/smart_contracts_receive.py line 557:" 
        debug_msg_sign = "Command below is defined in py-files/smart_contracts_receive.py line 571:" 
        debug_msg_submit = "Command below is defined in py-files/smart_contracts_receive.py line 577:" 
                    
        manage_command(command_build, msg_build, debug_msg_build)
        time.sleep(1)
        if not self.command_failed:
            manage_command(command_sign, msg_sign, debug_msg_sign)
            time.sleep(1)
        if not self.command_failed:
            manage_command(command_submit, msg_submit, debug_msg_submit) 
        if not self.command_failed and not settings.debug_mode:
            msg = "Commads successfully executed.\n" + \
                  "Look at console output for transaction info."  
            QMessageBox.information(self, "Notification:", msg) 
        self.command_failed = False
