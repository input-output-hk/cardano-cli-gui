

import os
import settings
import subprocess
import traceback
import common_functions

from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import (QPushButton, QLabel, QLineEdit, 
                             QWidget, QGridLayout, QMessageBox,
                             QRadioButton)

# Widgets and functions for the wallet tab
class Wallet(QWidget):
    def __init__(self):
        super().__init__()

        # Creating local variables
        self.vkey_name = ""
        self.address_name = ""
        self.pkh_name = ""

        # Header text 
        self.label_0_0 = QLabel("Manage wallet address and its keys.")

        # Cardano picture
        picture_0_2 = QLabel("")
        picture_0_2.setPixmap(QPixmap("./images/cardano.png"))
        picture_0_2.setFixedSize(80,80)
        picture_0_2.setScaledContents(True)

        # Widgets for verification key section 
        self.label_1_0 = QLabel("Input verification key name:")
        self.input_2_0 = QLineEdit()
        self.button_2_1 = QPushButton("Set")

        # Widgets for signing key section 
        self.label_3_0 = QLabel("Signing key name:")
        self.input_4_0 = QLineEdit()
        self.button_5_0 = QPushButton("Generate both keys")

        # Widget actions for signing and verifaction key section
        self.button_2_1.clicked.connect(self.set_verification_key)
        self.button_5_0.clicked.connect(self.generate_skey_and_vkey)

        # Widgets for payment address section 
        self.label_7_0 = QLabel("Input payment address name:")
        self.input_8_0 = QLineEdit()
        self.button_8_1 = QPushButton("Set")
        self.button_8_2 = QPushButton("Generate")
        self.label_9_0 = QLabel("Payment address:")
        self.radioButton_9_1 = QRadioButton("Mainnet")
        self.radioButton_9_2 = QRadioButton("Testnet")
        self.input_10_0 = QLineEdit()
        self.button_10_1 = QPushButton("Show")

        # Widget actions for payment address section  
        self.button_8_1.clicked.connect(self.set_address) 
        self.button_8_2.clicked.connect(self.generate_address) 
        self.button_10_1.clicked.connect(self.show_address) 

        # Widgets for payment address key hash section 
        self.label_12_0 = QLabel("Payment public key hash name:")
        self.input_13_0 = QLineEdit()
        self.button_13_1 = QPushButton("Set")
        self.button_13_2 = QPushButton("Generate")
        self.label_14_0 = QLabel("Key hash:")
        self.input_15_0 = QLineEdit()
        self.button_15_1 = QPushButton("Show")

        # Widget actions for payment public key hash section 
        self.button_13_1.clicked.connect(self.set_pkh) 
        self.button_13_2.clicked.connect(self.generate_pkh) 
        self.button_15_1.clicked.connect(self.show_pkh) 

        # Set label fonts 
        labels = [self.label_0_0, 
                  self.label_1_0, self.label_3_0, 
                  self.label_7_0, self.label_9_0,
                  self.label_12_0, self.label_14_0]
        for label in labels:
            font = label.font()
            font.setPointSize(12)
            label.setFont(font)

        # Set lineEdit sizes 
        inputs = [self.input_2_0, self.input_4_0, 
                  self.input_8_0, self.input_10_0,
                  self.input_13_0, self.input_15_0]
        for input in inputs:
            input.setFixedSize(500,30)

        # Set button sizes 
        buttons = [self.button_2_1,  
                   self.button_8_1, self.button_8_2, 
                   self.button_10_1, self.button_13_1, 
                   self.button_13_2, self.button_15_1] 
        for button in buttons:
            button.setFixedSize(80,30)  

        self.button_5_0.setFixedSize(160,30)  

        # Space between the sections
        self.emptyLabel = QLabel()

        # Layouts 
        layout = QGridLayout()
        layout.addWidget(self.label_0_0, 0, 0) 
        layout.addWidget(picture_0_2, 0, 2) 
        # Adding widgets for verification key section 
        layout.addWidget(self.label_1_0, 1, 0) 
        layout.addWidget(self.input_2_0, 2, 0) 
        layout.addWidget(self.button_2_1, 2, 1) 
        layout.addWidget(self.emptyLabel, 3, 0)
        # Adding widgets for signing key section 
        layout.addWidget(self.label_3_0, 3, 0)
        layout.addWidget(self.input_4_0, 4, 0)
        layout.addWidget(self.button_5_0, 5, 0)
        layout.addWidget(self.emptyLabel, 6, 0)
        # Adding widgets for payment address section 
        layout.addWidget(self.label_7_0, 7, 0)
        layout.addWidget(self.input_8_0, 8, 0)
        layout.addWidget(self.button_8_1, 8, 1)
        layout.addWidget(self.button_8_2, 8, 2)
        layout.addWidget(self.label_9_0, 9, 0)
        layout.addWidget(self.radioButton_9_1, 9, 1)
        layout.addWidget(self.radioButton_9_2, 9, 2)
        layout.addWidget(self.input_10_0, 10, 0)
        layout.addWidget(self.button_10_1, 10, 1) 
        layout.addWidget(self.emptyLabel, 11, 0)
        # Adding widgets for payment public key hash section 
        layout.addWidget(self.label_12_0, 12, 0)
        layout.addWidget(self.input_13_0, 13, 0)
        layout.addWidget(self.button_13_1, 13, 1)
        layout.addWidget(self.button_13_2, 13, 2)
        layout.addWidget(self.label_14_0, 14, 0)
        layout.addWidget(self.input_15_0, 15, 0)
        layout.addWidget(self.button_15_1, 15, 1)
        layout.addWidget(self.emptyLabel, 16, 0)

        self.setLayout(layout)

    def set_verification_key(self):
        vkey_name = self.input_2_0.text()
        vkey_path = settings.folder_path + "/" + vkey_name
        vkey_exists = os.path.isfile(vkey_path)
        
        skey_name = vkey_name.split(".")[0] + ".skey"
        skey_path = settings.folder_path + "/" + skey_name
        skey_exists = os.path.isfile(skey_path) 

        if not vkey_exists:
            msg = "Verification key does not exists.\n" + \
                  "Please enter a valid file name."                       
            QMessageBox.warning(self, "Notification:", msg,
                                QMessageBox.Close)
            return None

        if not (".vkey" in vkey_name):
            msg = "Verification key has to have a .vkey file extension name.\n" + \
                  "Please type in a file name with a .vkey extension." 
            QMessageBox.warning(self, "Notification:", msg,
                                QMessageBox.Close)
            return None

        self.vkey_name = vkey_name
        msg = "Verification key file successfully set."  
        QMessageBox.information(self, "Notification:", msg)
        if skey_exists:
            self.input_4_0.setText(skey_name)

    def generate_skey_and_vkey(self):
        file_number_counter = 1
        while(True):
            if len(str(file_number_counter)) == 1:
                vkey_name = "0" + str(file_number_counter) + ".vkey"
                skey_name = "0" + str(file_number_counter) + ".skey"
            else:
                vkey_name = str(file_number_counter) + ".vkey"
                skey_name = str(file_number_counter) + ".skey"
            
            vkey_file_path = settings.folder_path + "/" + vkey_name
            vkey_file_exists = os.path.isfile(vkey_file_path)

            skey_file_path = settings.folder_path + "/" + skey_name
            skey_file_exists = os.path.isfile(skey_file_path)

            if (not vkey_file_exists) and (not skey_file_exists):
                command = "cardano-cli address key-gen " + \
                          "--verification-key-file " + vkey_name + " " + \
                          "--signing-key-file " + skey_name 

                if settings.debug_mode:
                    print("Command below is defined in py-files/wallet.py line 184:")
                    print(command + "\n")
                else:
                    try:
                        subprocess.Popen(command.split(), cwd=settings.folder_path)
                        self.vkey_name = vkey_name
                        self.input_2_0.setText(self.vkey_name)
                        self.input_4_0.setText(skey_name)
                    except Exception:
                        output = traceback.format_exc()
                        common_functions.log_error_msg(output)
                        
                        msg = "Verification and signing key could not be generated.\n" + \
                              "Look at the error.log file for error output." 
                        QMessageBox.warning(self, "Notification:", msg,
                                            QMessageBox.Close)
                break
            
            file_number_counter += 1

    def set_address(self): 
        address_name = self.input_8_0.text()
        address_path = settings.folder_path + "/" + address_name
        address_exists = os.path.isfile(address_path)
        
        if not address_exists:
            msg = "Address does not exists.\n" + \
                  "Please enter a valid file name."                      
            QMessageBox.warning(self, "Notification:", msg,
                                QMessageBox.Close)
            return None

        if not (".addr" in address_name):
            msg = "Address file has to have a .addr file extension name.\n" + \
                  "Please type in a file name with a .addr extension." 
            QMessageBox.warning(self, "Notification:", msg,
                                QMessageBox.Close)
            return None

        self.address_name = address_name
        msg = "Public address file successfully set."  
        QMessageBox.information(self, "Notification:", msg)

    def generate_address(self):
        is_mainnet = self.radioButton_9_1.isChecked()
        is_testnet = self.radioButton_9_2.isChecked()

        if (not is_mainnet) and (not is_testnet):
            msg = "Select option mainnet or testnet."    
            QMessageBox.warning(self, "Notification:", msg,
                                QMessageBox.Close)
            return None

        if self.vkey_name == "":
            msg = "Please set or generate first a verification key."     
            QMessageBox.warning(self, "Notification:", msg,
                                QMessageBox.Close)
            return None 

        address_name = self.vkey_name.split(".")[0] + ".addr"
        address_path = settings.folder_path + "/" + address_name
        address_exists = os.path.isfile(address_path)

        if address_exists:
            file_number_counter = 1
            while(True):
                if len(str(file_number_counter)) == 1:
                    tmp_address_name = "0" + str(file_number_counter) + ".addr"
                else:
                    tmp_address_name = str(file_number_counter) + ".addr"
                
                tmp_address_path = settings.folder_path + "/" + tmp_address_name
                tmp_address_exists = os.path.isfile(tmp_address_path)

                if (not tmp_address_exists):
                    address_name = tmp_address_name
                    break

                file_number_counter += 1

            msg = "Address file with same name as verification key already exists.\n" + \
                  "The address file name " + address_name + " will be used." 
            QMessageBox.warning(self, "Notification:", msg,
                                QMessageBox.Close)

        if is_testnet:
            net_part = "--testnet-magic " + settings.testnet_magic + " "
        elif is_mainnet:
            net_part = "--mainnet "

        command = "cardano-cli address build " + \
                  "--payment-verification-key-file " + self.vkey_name + " " + \
                  net_part + \
                  "--out-file " + address_name

        if settings.debug_mode:
            print("Command below is defined in py-files/wallet.py line 271:")
            print(command + "\n")
        else:
            try:
                subprocess.Popen(command.split(), cwd=settings.folder_path)
                self.input_8_0.setText(address_name) 
                self.address_name = address_name
            except Exception:
                output = traceback.format_exc()
                common_functions.log_error_msg(output)
                
                msg = "Address could not be generated.\n" + \
                      "Look at the error.log file for error output."                    
                QMessageBox.warning(self, "Notification:", msg,
                                    QMessageBox.Close)

    def show_address(self): 
        address_path = settings.folder_path + "/" + self.address_name
        address_exists = os.path.isfile(address_path)

        if address_exists:
            with open(address_path, "r") as file:
                address = file.read()
            self.input_10_0.setText(address)
        else:
            msg = "Please set or generate first an address file."                    
            QMessageBox.warning(self, "Notification:", msg,
                                QMessageBox.Close)

    def set_pkh(self): 
        pkh_name = self.input_13_0.text()
        pkh_path = settings.folder_path + "/" + pkh_name
        pkh_exists = os.path.isfile(pkh_path)
        
        if not pkh_exists:
            msg = "Public key hash does not exists.\n" + \
                  "Please specify a valid file name."                        
            QMessageBox.warning(self, "Notification:", msg,
                                QMessageBox.Close)
            return None

        if not (".pkh" in pkh_name):
            msg = "Public key hash has to have a .pkh file extension name.\n" + \
                  "Please type in a file name with a .pkh extension." 
            QMessageBox.warning(self, "Notification:", msg,
                                QMessageBox.Close)
            return None

        self.pkh_name = pkh_name
        msg = "Public key hash file successfully set."  
        QMessageBox.information(self, "Notification:", msg)

    def generate_pkh(self):
        if self.vkey_name == "":
            msg = "Please set or generate first a verification key."     
            QMessageBox.warning(self, "Notification:", msg,
                                QMessageBox.Close)
            return None

        pkh_name = self.vkey_name.split(".")[0] + ".pkh"
        pkh_path = settings.folder_path + "/" + pkh_name
        pkh_exists = os.path.isfile(pkh_path)

        if pkh_exists:
            file_number_counter = 1
            while(True):
                if len(str(file_number_counter)) == 1:
                    tmp_pkh_name = "0" + str(file_number_counter) + ".pkh"
                else:
                    tmp_pkh_name = str(file_number_counter) + ".pkh"
                
                tmp_pkh_path = settings.folder_path + "/" + tmp_pkh_name
                tmp_pkh_exists = os.path.isfile(tmp_pkh_path)

                if (not tmp_pkh_exists):
                    pkh_name = tmp_pkh_name
                    break

                file_number_counter += 1

            msg = "Public key hash file with same name as verification key already exists." + \
                  "The public key hash file name " + pkh_name + " will be used." 
            QMessageBox.warning(self, "Notification:", msg,
                                QMessageBox.Close)

        command = "cardano-cli address key-hash " + \
                  "--payment-verification-key-file " + self.vkey_name + " " + \
                  "--out-file " + pkh_name
        
        if settings.debug_mode:
            print("Command below is defined in py-files/wallet.py line 354:")
            print(command + "\n")
        else:
            try:
                subprocess.Popen(command.split(), cwd=settings.folder_path)
                self.input_13_0.setText(pkh_name)
                self.pkh_name = pkh_name
            except Exception:
                output = traceback.format_exc()
                common_functions.log_error_msg(output)
                
                msg = "Public key hash could not be generated.\n" + \
                      "Look at the error.log file for error output."                 
                QMessageBox.warning(self, "Notification:", msg,
                                    QMessageBox.Close)

    def show_pkh(self): 
        pkh_path = settings.folder_path + "/" + self.pkh_name
        pkh_exists = os.path.isfile(pkh_path)

        if pkh_exists:
            with open(pkh_path, "r") as file:
                pkh = file.read()
            self.input_15_0.setText(pkh)
        else:
            msg = "Public key hash file does not exists.\n" + \
                  "If you have generated it, wait a couple of\n" + \
                  "seconds and try again to view the file."  
            QMessageBox.warning(self, "Notification:", msg,
                                QMessageBox.Close)