

import os
import sys
import subprocess
import traceback

from PyQt5.QtCore import Qt
from PyQt5.QtCore import QSize 
from PyQt5.QtGui import QPixmap, QPalette, QColor, QFont
from PyQt5.QtWidgets import (QApplication, QMainWindow, QTabWidget, 
                             QAction, QPushButton, QLabel, QLineEdit, 
                             QWidget, QGridLayout, QMessageBox,
                             QRadioButton, QPlainTextEdit, QComboBox)

global debug_mode
global folder_path
global testnet_magic
global current_era


lightPallet = QPalette()
lightPallet.setColor(QPalette.Window, QColor(224, 224, 224))

darkPalette = QPalette()
darkPalette.setColor(QPalette.Window, QColor(53, 53, 53))
darkPalette.setColor(QPalette.WindowText, Qt.white)
darkPalette.setColor(QPalette.Disabled, QPalette.WindowText, QColor(127, 127, 127))
darkPalette.setColor(QPalette.Base, QColor(42, 42, 42))
darkPalette.setColor(QPalette.AlternateBase, QColor(66, 66, 66))
darkPalette.setColor(QPalette.ToolTipBase, Qt.white)
darkPalette.setColor(QPalette.ToolTipText, Qt.white)
darkPalette.setColor(QPalette.Text, Qt.white)
darkPalette.setColor(QPalette.Disabled, QPalette.Text, QColor(127, 127, 127))
darkPalette.setColor(QPalette.Dark, QColor(35, 35, 35))
darkPalette.setColor(QPalette.Shadow, QColor(20, 20, 20))
darkPalette.setColor(QPalette.Button, QColor(53, 53, 53))
darkPalette.setColor(QPalette.ButtonText, Qt.white)
darkPalette.setColor(QPalette.Disabled, QPalette.ButtonText, QColor(127, 127, 127))
darkPalette.setColor(QPalette.BrightText, Qt.red)
darkPalette.setColor(QPalette.Link, QColor(42, 130, 218))
darkPalette.setColor(QPalette.Highlight, QColor(42, 130, 218))
darkPalette.setColor(QPalette.Disabled, QPalette.Highlight, QColor(80, 80, 80))
darkPalette.setColor(QPalette.HighlightedText, Qt.white)
darkPalette.setColor(QPalette.Disabled, QPalette.HighlightedText, QColor(127, 127, 127))

class MainWindow(QMainWindow):
    def __init__(self):
        global folder_path, debug_mode, testnet_magic, current_era 
        super().__init__()

        # Initiate global variables
        self.init_global_variables()

        # Set window properties
        self.setMinimumSize(QSize(740, 900)) 
        self.setWindowTitle("Cardano client GUI 1.0")

        # Create the applications menu 
        self.app_menu = self.menuBar()
        debug_menu = self.app_menu.addMenu("&Debug")
        style_menu = self.app_menu.addMenu("&Style")

        # Debug menu widgets
        on_toggle = QAction("&ON", self)
        off_toggle = QAction("&OFF", self)

        debug_menu.addAction(on_toggle)
        debug_menu.addSeparator()
        debug_menu.addAction(off_toggle)

        on_toggle.triggered.connect(self.set_debug_on)
        off_toggle.triggered.connect(self.set_debug_off)

        # Style menu widgets
        light_style = QAction("&Light", self)
        dark_style = QAction("&Dark", self)

        style_menu.addAction(light_style)
        style_menu.addSeparator()
        style_menu.addAction(dark_style)

        light_style.triggered.connect(self.set_light_style)
        dark_style.triggered.connect(self.set_dark_style)

        # Create tabs and adds start window 
        self.tabs = QTabWidget()
        self.tabs.setTabPosition(QTabWidget.North)
        self.tabs.setMovable(True)

        self.start_window = QWidget()
        self.init_start_tab()

        self.tabs.addTab(self.start_window,"Start")
        self.setCentralWidget(self.tabs)

    # Sets initial values for global variables
    def init_global_variables(self):
        global folder_path, debug_mode, testnet_magic, current_era 
        folder_path = ""
        debug_mode = False
        testnet_magic = "2"
        current_era = "babbage-era"

    # Sets debug mode to ON
    def set_debug_on(self):
        global folder_path, debug_mode, testnet_magic, current_era 
        debug_mode = True
        
        self.label_8_0.setText("Debug mode: ON")
        # When start window was in a separated class
        # self.tabs.widget(0).label_8_0.setText("Debug mode: OFF")

    # Sets debug mode to OFF
    def set_debug_off(self):
        global folder_path, debug_mode, testnet_magic, current_era 
        debug_mode = False
        
        self.label_8_0.setText("Debug mode: OFF")
        # When start window was in a separated class
        # self.tabs.widget(0).label_8_0.setText("Debug mode: OFF")

    # Widgets for the start tab 
    def init_start_tab(self):
        global folder_path, debug_mode, testnet_magic, current_era 
        # Initial message
        label_1_0 = QLabel("To unlock other tabs set a valid folder path.\n" + \
                           "All files will be loaded or saved to this folder.")

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
        label_9_0 = QLabel("If debug mode is ON, the programm prints the cardano-cli\n" + \
                           "commands to the terminal instead of executing them.")
        label_11_0 = QLabel("IMPORTANT:")
        label_12_0 = QLabel("A cardano node has to be synced and running\n" + \
                            "for the query and send command to work.")

        # Widget actions
        button_4_1.clicked.connect(self.set_folder_path)

        # Set label fonts 
        labels = [label_1_0, label_3_0, 
                  label_5_0, self.label_6_0, 
                  self.label_8_0, label_9_0, 
                  label_11_0, label_12_0]
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
        layout.addWidget(label_1_0, 1, 0)
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

        self.start_window.setLayout(layout)

    # Function for setting the folder_path global variable
    def set_folder_path(self):
        global folder_path, debug_mode, testnet_magic, current_era 
        folder_path_input = self.input_4_0.text()
        if folder_path_input[-1] == "/":
            folder_path_input = folder_path_input[0:-1]
        folder_exists = os.path.isdir(folder_path_input)
        
        if folder_exists:
            folder_path = folder_path_input
            self.label_6_0.setText(folder_path_input)
 
            self.tabs.addTab(Wallet(),"Wallet")
            self.tabs.addTab(Transactions(),"Transactions")
            self.tabs.addTab(Smart_contracts(),"Smart contrancts")
            self.tabs.addTab(Developer(),"Developer")
        else:
            self.input_4_0.setText(folder_path)
            msg = "This path is not a valid folder path.\n" + \
                  "Spaces before or after the path are not allowed."                   
            QMessageBox.warning(self, "Notification:", msg,
                                QMessageBox.Close)

    def set_light_style(self):
        global folder_path, debug_mode, testnet_magic, current_era 
        app.setPalette(lightPallet)

    def set_dark_style(self):
        global folder_path, debug_mode, testnet_magic, current_era 
        app.setPalette(darkPalette)

class Wallet(QWidget):
    def __init__(self):
        global folder_path, debug_mode, testnet_magic 
        super().__init__()

        # Creating local variables
        self.vkey_name = ""
        self.address = ""
        self.pkh = ""

        # Starting text and Cardano picture
        self.label_0_0 = QLabel("Manage wallet address and its keys.")
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
        global folder_path, debug_mode, testnet_magic 
        vkey_name = self.input_2_0.text()
        vkey_path = folder_path + "/" + vkey_name
        vkey_exists = os.path.isfile(vkey_path)
        
        skey_name = vkey_name.split(".")[0] + ".skey"
        skey_path = folder_path + "/" + skey_name
        skey_exists = os.path.isfile(skey_path) 

        if vkey_exists:
            self.vkey_name = vkey_name
        else:
            msg = "Verification key does not exists.\n" + \
                  "Please enter a valid file name."                       
            QMessageBox.warning(self, "Notification:", msg,
                                QMessageBox.Close)
            return None

        if skey_exists:
            self.input_4_0.setText(skey_name)

    def generate_skey_and_vkey(self):
        global folder_path, debug_mode, testnet_magic 
        file_number_counter = 1
        while(True):
            if len(str(file_number_counter)) == 1:
                vkey_name = "0" + str(file_number_counter) + ".vkey"
                skey_name = "0" + str(file_number_counter) + ".skey"
            else:
                vkey_name = str(file_number_counter) + ".vkey"
                skey_name = str(file_number_counter) + ".skey"
            
            vkey_file_path = folder_path + "/" + vkey_name
            vkey_file_exists = os.path.isfile(vkey_file_path)

            skey_file_path = folder_path + "/" + skey_name
            skey_file_exists = os.path.isfile(skey_file_path)

            if (not vkey_file_exists) and (not skey_file_exists):
                command = "cardano-cli address key-gen " + \
                          "--verification-key-file " + vkey_name + " " + \
                          "--signing-key-file " + skey_name 

                if debug_mode:
                    print("Command below is defined in py-files/wallet.py line 180:")
                    print(command + "\n")
                else:
                    try:
                        subprocess.Popen(command.split(), cwd=folder_path)
                        self.vkey_name = vkey_name
                        self.input_2_0.setText(self.vkey_name)
                        self.input_4_0.setText(skey_name)
                    except Exception:
                        output = traceback.format_exc()
                        log_error_msg(output)
                        
                        msg = "Verification and signing key could not be generated.\n" + \
                              "Look at the error.log file for error output." 
                        QMessageBox.warning(self, "Notification:", msg,
                                            QMessageBox.Close)
                break
            
            file_number_counter += 1

    def set_address(self): 
        global folder_path, debug_mode, testnet_magic 
        address_name = self.input_8_0.text()
        address_path = folder_path + "/" + address_name
        address_exists = os.path.isfile(address_path)
        
        if address_exists:
            with open(address_path, "r") as file:
                self.address = file.read()
        else:
            msg = "Address does not exists.\n" + \
                  "Please enter a valid file name."                      
            QMessageBox.warning(self, "Notification:", msg,
                                QMessageBox.Close)

    def generate_address(self):
        global folder_path, debug_mode, testnet_magic 
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
        address_path = folder_path + "/" + address_name
        address_exists = os.path.isfile(address_path)

        if address_exists:
            msg = "Address file with same name as verification key already exists.\n" + \
                  "To generate a new address file, delete or rename the existing file."   
            QMessageBox.warning(self, "Notification:", msg,
                                QMessageBox.Close)
            return None

        if is_testnet:
            net_part = "--testnet-magic " + testnet_magic + " "
        elif is_mainnet:
            net_part = "--mainnet "

        command = "cardano-cli address build " + \
                  "--payment-verification-key-file " + self.vkey_name + " " + \
                  net_part + \
                  "--out-file " + address_name

        if debug_mode:
            print("Command below is defined in py-files/wallet.py line 251:")
            print(command + "\n")
        else:
            try:
                subprocess.Popen(command.split(), cwd=folder_path)
                self.input_8_0.seText(address_name) 
                with open(address_path, "r") as file:
                    self.address = file.read() 
            except Exception:
                output = traceback.format_exc()
                log_error_msg(output)
                
                msg = "Address could not be generated.\n" + \
                      "Look at the error.log file for error output."                    
                QMessageBox.warning(self, "Notification:", msg,
                                    QMessageBox.Close)

    def show_address(self): 
        global folder_path, debug_mode, testnet_magic 
        self.input_10_0.setText(self.address)

    def set_pkh(self): 
        global folder_path, debug_mode, testnet_magic 
        pkh_name = self.input_13_0.text()
        pkh_path = folder_path + "/" + pkh_name
        pkh_exists = os.path.isfile(pkh_path)
        
        if pkh_exists:
            with open(pkh_path, "r") as file:
                self.pkh = file.read()
        else:
            msg = "Public key hash does not exists.\n" + \
                  "Please specify a valid file name."                        
            QMessageBox.warning(self, "Notification:", msg,
                                QMessageBox.Close)

    def generate_pkh(self):
        global folder_path, debug_mode, testnet_magic 
        if self.vkey_name == "":
            msg = "Please set or generate first a verification key."     
            QMessageBox.warning(self, "Notification:", msg,
                                QMessageBox.Close)
            return None

        pkh_name = self.vkey_name.split(".")[0] + ".pkh"
        pkh_path = folder_path + "/" + pkh_name
        pkh_exists = os.path.isfile(pkh_path)

        if pkh_exists:
            msg = "Public key hash file with same name as verification key already exists.\n" + \
                  "To generate a new verification key, delete or rename the existing file."      
            QMessageBox.warning(self, "Notification:", msg,
                                QMessageBox.Close)
            return None

        command = "cardano-cli address key-hash " + \
                  "--payment-verification-key-file " + self.vkey_name + " " + \
                  "--out-file " + pkh_name
        
        if debug_mode:
            print("Command below is defined in py-files/wallet.py line 309:")
            print(command + "\n")
        else:
            try:
                subprocess.Popen(command.split(), cwd=folder_path)
                self.input_13_0.setText(pkh_name)
                with open(pkh_path, "r") as file:
                    self.pkh = file.read()
            except Exception:
                output = traceback.format_exc()
                log_error_msg(output)
                
                msg = "Public key hash could not be generated.\n" + \
                      "Look at the error.log file for error output."                     
                QMessageBox.warning(self, "Notification:", msg,
                                    QMessageBox.Close)

    def show_pkh(self): 
        global folder_path, debug_mode, testnet_magic 
        self.input_15_0.setText(self.pkh)

class Transactions(QWidget):
    def __init__(self):
        global folder_path, debug_mode, testnet_magic 
        super().__init__()

        # Creating local variables
        self.address = ""
        self.skey_name = ""
        self.net = ""
        self.era = current_era
        self.utxo = ""
        self.receiving_address = ""

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
        self.label_11_0 = QLabel("Current era parameter set to:")
        self.label_12_0 = QLabel(current_era)
        self.label_13_0 = QLabel("Input UTxO address:")
        self.input_14_0 = QLineEdit()
        self.button_14_1 = QPushButton("Set")
        self.label_15_0 = QLabel("Input receiving address name:")
        self.input_16_0 = QLineEdit()
        self.button_16_1 = QPushButton("Set")
        self.button_18_0 = QPushButton("Send")

        # Widget actions for sending funds section 
        self.button_14_1.clicked.connect(self.set_utxo)
        self.button_16_1.clicked.connect(self.set_receiving_address)
        self.button_18_0.clicked.connect(self.send_funds)

        # Set label fonts 
        labels = [self.label_0_0, self.label_1_0, 
                  self.label_3_0, self.label_5_0,
                  self.label_7_0, self.label_9_0, 
                  self.label_11_0, self.label_12_0,
                  self.label_13_0, self.label_15_0]
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
        layout.addWidget(self.label_12_0, 12, 0)
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
        global folder_path, debug_mode, testnet_magic 
        address_name = self.input_2_0.text()
        address_path = folder_path + "/" + address_name
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
        global folder_path, debug_mode, testnet_magic 
        skey_name = self.input_4_0.text()
        skey_path = folder_path + "/" + skey_name
        skey_exists = os.path.isfile(skey_path)
        
        if skey_exists:
            self.skey_name = skey_name
        else:
            msg = "Signing key file does not exists.\n" + \
                  "Please enter a valid file name."  
            QMessageBox.warning(self, "Notification:", msg,
                                QMessageBox.Close) 

    def querry_address_funds(self):
        global folder_path, debug_mode, testnet_magic 
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
            net_part = "--testnet-magic " + testnet_magic + " "
        
        command = "cardano-cli query utxo " + \
                  "--address " + self.address + " " + \
                  net_part 
        
        if debug_mode:
            print("Command below is defined in py-files/transactions.py line 204:")
            print(command + "\n")
        else:
            try:
                response = subprocess.Popen(command.split(), cwd=folder_path) 
                output = response.communicate()[0]
                self.input_6_0.setPlainText(output.decode("utf-8"))
            except Exception:
                output = traceback.format_exc()
                log_error_msg(output)
                
                msg = "Address could not be querried.\n" + \
                      "Check if cardano node is running and is synced.\n" + \
                      "Look at the error.log file for error output."                    
                QMessageBox.warning(self, "Notification:", msg,
                                    QMessageBox.Close)

    def set_net(self, selected_net):
        global folder_path, debug_mode, testnet_magic 
        if selected_net != "":
            self.net = selected_net 

    def set_utxo(self):
        global folder_path, debug_mode, testnet_magic 
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
        global folder_path, debug_mode, testnet_magic 
        receiving_address_name = self.input_16_0.text()
        receiving_address_path = folder_path + "/" + receiving_address_name
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
        global folder_path, debug_mode, testnet_magic 
        self.command_failed = False

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
        amount_in_lovelace = parse_amount(amount_text, currency)

        if amount_in_lovelace == -1:
            msg = "The specified amount in " + currency + " is not a valid input.\n" + \
                  "Amount in ADA can have max 6 decimal numbers.\n" + \
                  "Spaces and characters are not allowed." 
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
            global folder_path, debug_mode, testnet_magic 
            if debug_mode:
                print(debug_msg)
                print(command + "\n")
            else:
                try:
                    subprocess.Popen(command.split(), cwd=folder_path)
                except Exception:
                    output = traceback.format_exc()
                    log_error_msg(output)                   
                    QMessageBox.warning(self, "Notification:", msg,
                                        QMessageBox.Close)
                    self.command_failed = True

        if self.net == "mainnet":
            net_part = "--mainnet "
        elif self.net == "testnet": 
            net_part = "--testnet-magic " + testnet_magic + " "

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

        debug_msg_build = "Command below is defined in py-files/transactions.py line 340:"
        debug_msg_sign = "Command below is defined in py-files/transactions.py line 347:"
        debug_msg_submit = "Command below is defined in py-files/transactions.py line 352:" 
                    
        manage_command(command_build, msg_build, debug_msg_build)
        if not self.command_failed:
            manage_command(command_sign, msg_sign, debug_msg_sign)
            if not debug_mode:
                os.remove(folder_path + "/tx.body")
        if not self.command_failed:
            manage_command(command_submit, msg_submit, debug_msg_submit)
            if not debug_mode:
                os.remove(folder_path + "/tx.signed")

class Smart_contracts(QWidget):
    def __init__(self):
        global folder_path, debug_mode, testnet_magic 
        super().__init__()

        # Creating local variables
        self.script_file = ""
        self.script_address = ""
        self.net = ""

        self.change_address = ""
        self.skey_name = ""
        self.era = current_era
        self.utxo = ""
        self.datum_file_name = ""

        # Cardano picture
        self.label_0_0 = QLabel("Generate cardano script address and send funds to it.")
        picture_0_2 = QLabel("")
        picture_0_2.setPixmap(QPixmap("./images/cardano.png"))
        picture_0_2.setFixedSize(80,80)
        picture_0_2.setScaledContents(True)

        # Widgets for building script address section 
        self.label_1_0 = QLabel("Type in script file name:")
        self.input_2_0 = QLineEdit()
        self.button_2_1 = QPushButton("Set")
        self.label_3_0 = QLabel("Script address file name:")
        self.input_4_0 = QLineEdit()
        self.button_4_1 = QPushButton("Set")
        self.button_4_2 = QPushButton("Generate")
        self.label_5_0 = QLabel("Select mainnet or testnet:")
        self.comboBox_6_0 = QComboBox()
        self.label_7_0 = QLabel("Script address:")
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
        self.label_9_0 = QLabel("Type in your change address name:")
        self.input_10_0 = QLineEdit()
        self.button_10_1 = QPushButton("Set")
        self.label_11_0 = QLabel("Type in your signing key file name:")
        self.input_12_0 = QLineEdit()
        self.button_12_1 = QPushButton("Set")
        self.label_13_0 = QLabel("Send amount (seperat decimal number with dot):")
        self.input_14_0 = QLineEdit()
        self.radioButton_14_1 = QRadioButton("Ada")
        self.radioButton_14_2 = QRadioButton("Lovelace")
        self.label_15_0 = QLabel("Current era parameter set to:")
        self.label_16_0 = QLabel(current_era)
        self.label_17_0 = QLabel("Input UTxO address:")
        self.input_18_0 = QLineEdit()
        self.button_18_1 = QPushButton("Set")
        self.label_19_0 = QLabel("Type in datum file name:")
        self.input_20_0 = QLineEdit()
        self.button_20_1 = QPushButton("Set")

        self.button_22_0 = QPushButton("Send")

        # Widget actions for building script address section  
        self.button_10_1.clicked.connect(self.set_change_address)
        self.button_12_1.clicked.connect(self.set_skey_name)
        self.button_18_1.clicked.connect(self.set_utxo)
        self.button_20_1.clicked.connect(self.set_datum)
        self.button_22_0.clicked.connect(self.send_funds)

        # Set label fonts 
        labels = [self.label_0_0, self.label_1_0, 
                  self.label_3_0, self.label_5_0, 
                  self.label_7_0, self.label_9_0, 
                  self.label_11_0, self.label_13_0, 
                  self.label_15_0, self.label_16_0, 
                  self.label_17_0, self.label_19_0] 
        for label in labels:
            font = label.font()
            font.setPointSize(12)
            label.setFont(font)

        # Set lineEdit sizes 
        inputs = [self.input_2_0, self.input_4_0, 
                  self.input_8_0, self.input_10_0, 
                  self.input_12_0, self.input_14_0,
                  self.input_18_0, self.input_20_0]
        for input in inputs: 
            input.setFixedSize(500,30)

        # Set button sizes 
        buttons = [self.button_2_1, self.button_4_1,
                   self.button_4_2, self.button_8_1, 
                   self.button_10_1, self.button_12_1, 
                   self.button_18_1, self.button_20_1] 
        for button in buttons:
            button.setFixedSize(80,30)

        self.button_22_0.setFixedSize(160,30) 

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
        layout.addWidget(self.label_16_0, 16, 0)
        layout.addWidget(self.label_17_0, 17, 0)
        layout.addWidget(self.input_18_0, 18, 0)
        layout.addWidget(self.button_18_1, 18, 1)
        layout.addWidget(self.label_19_0, 19, 0)
        layout.addWidget(self.input_20_0, 20, 0)
        layout.addWidget(self.button_20_1, 20, 1)
        layout.addWidget(self.emptyLabel, 21, 0)
        layout.addWidget(self.button_22_0, 22, 0) 

        self.setLayout(layout) 

    def set_script_file(self):
        global folder_path, debug_mode, testnet_magic 
        script_file_name = self.input_2_0.text()
        script_file_path = folder_path + "/" + script_file_name
        script_file_exists = os.path.isfile(script_file_path)
        
        if script_file_exists:
            self.script_file = script_file_name
        else:
            msg = "Script file does not exists.\n" + \
                  "Please enter a valid file name." 
            QMessageBox.warning(self, "Notification:", msg,
                                QMessageBox.Close) 

    def set_script_address_file(self):
        global folder_path, debug_mode, testnet_magic 
        script_address_file_name = self.input_4_0.text()
        script_address_file_path = folder_path + "/" + script_address_file_name
        script_address_file_exists = os.path.isfile(script_address_file_path)
        
        if script_address_file_exists:
            with open(script_address_file_path, "r") as file:
                self.script_address = file.read() 
        else:
            msg = "Script address file does not exists.\n" + \
                  "Please enter a valid file name." 
            QMessageBox.warning(self, "Notification:", msg,
                                QMessageBox.Close)

    def generate_script_address_file(self):
        global folder_path, debug_mode, testnet_magic 
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
            net_part = "--testnet-magic " + testnet_magic + " "
        
        command = "cardano-cli address build-script " + \
                  "--script-file " + self.script_file + " " + \
                  net_part + \
                  "--out-file " + script_address_file
        
        if debug_mode:
            print("Command below is defined in py-files/smart_contracts.py line 217:")
            print(command + "\n") 
        else:
            try:
                subprocess.Popen(command.split(), cwd=folder_path) 
                self.input_4_0.setText(script_address_file) 
            except Exception:
                output = traceback.format_exc()
                log_error_msg(output)
                
                msg = "Script address could not be generated.\n" + \
                      "Look at the error.log file for error output."                  
                QMessageBox.warning(self, "Notification:", msg,
                                    QMessageBox.Close)

    def set_net(self, selected_net):
        global folder_path, debug_mode, testnet_magic 
        if selected_net != "":
            self.net = selected_net

    def show_script_address(self):
        global folder_path, debug_mode, testnet_magic 
        self.input_8_0.setText(self.script_address)

    def set_change_address(self): 
        global folder_path, debug_mode, testnet_magic 
        change_address_name = self.input_10_0.text()
        change_address_path = folder_path + "/" + change_address_name
        change_address_exists = os.path.isfile(change_address_path)
        
        if change_address_exists:
            with open(change_address_path, "r") as file:
                self.change_address = file.read()
        else:
            msg = "Address file does not exists.\n" + \
                  "Please enter a valid file name." 
            QMessageBox.warning(self, "Notification:", msg,
                                QMessageBox.Close)

    def set_skey_name(self):
        global folder_path, debug_mode, testnet_magic 
        skey_name = self.input_12_0.text()
        skey_path = folder_path + "/" + skey_name
        skey_exists = os.path.isfile(skey_path)
        
        if skey_exists:
            self.skey_name = skey_name
        else:
            msg = "Signing key file does not exists.\n" + \
                  "Please enter a valid file name."  
            QMessageBox.warning(self, "Notification:", msg,
                                QMessageBox.Close) 

    def set_utxo(self):
        global folder_path, debug_mode, testnet_magic 
        utxo_input = self.input_18_0.text()
        if not ("#" in utxo_input):
            msg = "UTxO transaction input has to contain # sign and transaction index." + \
                  "Please enter a valid transaction input." 
            QMessageBox.warning(self, "Notification:", msg,
                                QMessageBox.Close)
            return None

        trans_hash = utxo_input.split("#")[0]
        if not (len(trans_hash) == 64):
            msg = "UTxO transaction hash has to be 64 characters long." + \
                  "Please enter a valid transaction hash." 
            QMessageBox.warning(self, "Notification:", msg,
                                QMessageBox.Close)
            return None

        self.utxo = utxo_input 

    def set_datum(self):
        global folder_path, debug_mode, testnet_magic 
        self.command_failed = False

        datum_file_name = self.input_20_0.text() 
        if not (".json" in datum_file_name):
            msg = "Datum has to be a file in JSON fromat." + \
                  "Please type in a name with a .json extension." 
            QMessageBox.warning(self, "Notification:", msg,
                                QMessageBox.Close)
            return None

        datum_file_path = folder_path + "/" + datum_file_name
        datum_file_exists = os.path.isfile(datum_file_path)
        if not datum_file_exists:
            msg = "Datum file does not exists.\n" + \
                  "Please enter a valid file name." 
            QMessageBox.warning(self, "Notification:", msg,
                                QMessageBox.Close) 
            return None

        self.datum_file_name = datum_file_name 

    def send_funds(self): 
        global folder_path, debug_mode, testnet_magic 
        if self.script_address == "":
            msg = "Please set the receiving script address." 
            QMessageBox.warning(self, "Notification:", msg,
                                QMessageBox.Close)
            return None

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
        amount_in_lovelace = parse_amount(amount_text, currency)

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

        if self.datum_file_name == "":
            msg = "Please set a valid datum file name." 
            QMessageBox.warning(self, "Notification:", msg,
                                QMessageBox.Close)
            return None

        def manage_command(command, msg, debug_msg):
            global folder_path, debug_mode, testnet_magic 
            if debug_mode:
                print(debug_msg)
                print(command + "\n")
            else:
                try:
                    subprocess.Popen(command.split(), cwd=folder_path)
                except Exception:
                    output = traceback.format_exc()
                    log_error_msg(output)                   
                    QMessageBox.warning(self, "Notification:", msg,
                                        QMessageBox.Close)
                    self.command_failed = True

        if self.net == "mainnet":
            net_part = "--mainnet "
        elif self.net == "testnet": 
            net_part = "--testnet-magic " + testnet_magic + " "

        command_build = "cardano-cli transaction build " + \
                        "--" + self.era + " " + \
                        net_part + \
                        "--tx-in " + self.utxo + " " + \
                        "--tx-out " + self.script_address + " " + str(amount_in_lovelace) + " lovelace " + \
                        "--tx-out-datum-hash-file " + self.datum_file_name + " " + \
                        "--change-address " + self.change_address + " " + \
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

        debug_msg_build = "Command below is defined in py-files/smart_contracts.py line 392:" 
        debug_msg_sign = "Command below is defined in py-files/smart_contracts.py line 400:" 
        debug_msg_submit = "Command below is defined in py-files/smart_contracts.py line 405:" 
                    
        manage_command(command_build, msg_build, debug_msg_build)
        if not self.command_failed:
            manage_command(command_sign, msg_sign, debug_msg_sign)
            if not debug_mode:
                os.remove(folder_path + "/tx.body")
        if not self.command_failed:
            manage_command(command_submit, msg_submit, debug_msg_submit) 
            if not debug_mode:                                              
                os.remove(folder_path + "/tx.signed")

class Developer(QWidget):
    def __init__(self):
        global folder_path, debug_mode, testnet_magic 
        super().__init__()

        # Initial message
        label_1_0 = QLabel("Manage advenced  Only for experienced developers.\n" + \
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
        self.label_5_0 = QLabel("Current testnet magic set to: " + testnet_magic)

        # Widgets for era section
        label_8_0 = QLabel("Input era:")
        self.input_9_0 = QLineEdit()
        button_9_1 = QPushButton("Set")
        self.label_10_0 = QLabel("Current era set to: " + current_era)

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
        global folder_path, debug_mode, testnet_magic 
        input_magic = self.input_4_0.text()
        if not input_magic.isdigit():
            msg = "Testnet magic number should contain only digits."        
            QMessageBox.warning(self, "Notification:", msg,
                                QMessageBox.Close)
        else:
            testnet_magic = input_magic
            self.label_5_0.setText("Current testnet magic set to: " + testnet_magic)
        

    def set_era(self):
        global folder_path, debug_mode, testnet_magic 
        input_era = self.input_9_0.text()
        if input_era == "":
            msg = "Era can not be an empty string."        
            QMessageBox.warning(self, "Notification:", msg,
                                QMessageBox.Close)
        else:
            current_era = input_era
            self.label_10_0.setText("Current era set to: " + current_era) 

    def reset_values(self):
        global folder_path, debug_mode, testnet_magic 
        testnet_magic = "2"
        self.input_4_0.setText("")
        self.label_5_0.setText("Current testnet magic set to: " + testnet_magic)
        
        current_era = "babbage-era"
        self.input_9_0.setText("")
        self.label_10_0.setText("Current era set to: " + current_era)     


# Writes an error message to a log file 
def log_error_msg(output):
    with open("./error.log", "w") as file:
        file.write(output)

# Parses the input string for the ADA or Lovelace amount
def parse_amount(input, currency):
    input_check = True
    input_lovelace = -1 

    if currency == "ADA":
        if '.' in input:
            input_parts = input.split(".")
            input_check1 = len(input_parts) == 2
            input_check2 = input[-1] != "." and input[0] != "."
            input_check3 = len(input_parts[1]) < 7
            if input_check1 and input_check2 and input_check3:
                for el in input_parts[0]:
                    if not el.isdigit():
                        input_check = False
                        break
                for el in input_parts[1]:
                    if not el.isdigit():
                        input_check = False
                        break
                if input_check:
                    if len(input_parts[1]) < 6:
                        lovelace_part = input_parts[1] + (6 - len(input_parts[1]))*"0"
                    else: 
                        lovelace_part = input_parts[1]
                    input_lovelace = int(input_parts[0])*1000000 + int(lovelace_part)
        return input_lovelace
    elif currency == "Lovelace":
        for el in input:
            if not el.isdigit():
                input_check = False
                break
        if input_check:
            input_lovelace = int(input)
        return input_lovelace

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()
