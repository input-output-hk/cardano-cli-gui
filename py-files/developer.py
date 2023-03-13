

import os
import settings
import subprocess
import traceback
import common_functions

from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import (QPushButton, QLabel, QLineEdit, 
                             QWidget, QGridLayout, QMessageBox,
                             QComboBox)

# Widgets and functions for the developer tab
class Developer(QWidget):
    def __init__(self):
        super().__init__()

        self.net = ""

        # Header text 
        self.label_1_0 = QLabel("Manage advenced settings. Only for experienced developers.\n" + \
                                "If you are not sure keep default parameter values.")

        # Cardano picture
        picture_1_1 = QLabel("")
        picture_1_1.setPixmap(QPixmap("./images/cardano.png"))
        picture_1_1.setFixedSize(80,80)
        picture_1_1.setScaledContents(True)

        # Widgets for testnet magic section 
        self.label_3_0 = QLabel("Input testnet magic number:")
        self.input_4_0 = QLineEdit()
        self.button_4_1 = QPushButton("Set")
        self.label_5_0 = QLabel("Current testnet magic set to: " + settings.testnet_magic)

        # Widgets for era section
        self.label_6_0 = QLabel("Input era:")
        self.input_7_0 = QLineEdit()
        self.button_7_1 = QPushButton("Set")
        self.label_8_0 = QLabel("Current era set to: " + settings.current_era)

        # Widgets for default value section
        self.label_9_0 = QLabel("Reset parameters to default values:")
        self.button_10_0 = QPushButton("Reset")

        # Widgets for generating protocol parameters file
        self.label_12_0 = QLabel("Select mainnet or testnet:")
        self.comboBox_13_0 = QComboBox()
        self.label_14_0 = QLabel("Generate protocol parameters file:")
        self.input_15_0 = QLineEdit("")
        self.button_15_1 = QPushButton("Generate")

        # Button and combobox functions
        self.button_4_1.clicked.connect(self.set_magic)
        self.button_7_1.clicked.connect(self.set_era)
        self.button_10_0.clicked.connect(self.reset_values)
        self.button_15_1.clicked.connect(self.generate_protocol_params_file)

        self.comboBox_13_0.addItems(["", "mainnet", "testnet"])
        self.comboBox_13_0.currentTextChanged.connect(self.set_net)

        # Set label fonts 
        labels = [self.label_1_0, self.label_3_0, 
                  self.label_5_0, self.label_6_0, 
                  self.label_8_0, self.label_9_0,
                  self.label_12_0, self.label_14_0]
        for label in labels:
            font = label.font()
            font.setPointSize(12)
            label.setFont(font)

        # Set lineEdit size 
        self.input_4_0.setFixedSize(500,30)
        self.input_7_0.setFixedSize(500,30)
        self.input_15_0.setFixedSize(500,30)

        # Set button size 
        self.button_4_1.setFixedSize(80,30)
        self.button_7_1.setFixedSize(80,30)
        self.button_10_0.setFixedSize(160,30)
        self.button_15_1.setFixedSize(80,30)

        # Space between the sections
        emptyLabel = QLabel()

        # Layouts 
        layout = QGridLayout()
        layout.addWidget(emptyLabel, 0, 0)
        layout.addWidget(self.label_1_0, 1, 0)
        layout.addWidget(picture_1_1, 1, 1)
        layout.addWidget(emptyLabel, 2, 0)
        layout.addWidget(self.label_3_0, 3, 0)
        layout.addWidget(self.input_4_0, 4, 0)
        layout.addWidget(self.button_4_1, 4, 1)
        layout.addWidget(self.label_5_0, 5, 0)
        layout.addWidget(self.label_6_0, 6, 0)
        layout.addWidget(self.input_7_0, 7, 0)
        layout.addWidget(self.button_7_1, 7, 1)
        layout.addWidget(self.label_8_0, 8, 0)
        layout.addWidget(self.label_9_0, 9, 0)
        layout.addWidget(self.button_10_0, 10, 0)
        layout.addWidget(emptyLabel, 11, 0)
        layout.addWidget(self.label_12_0, 12, 0)
        layout.addWidget(self.comboBox_13_0, 13, 0)
        layout.addWidget(self.label_14_0, 14, 0)
        layout.addWidget(self.input_15_0, 15, 0)
        layout.addWidget(self.button_15_1, 15, 1)
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
            msg = "Testnet magic number successfully set."  
            QMessageBox.information(self, "Notification:", msg) 
        

    def set_era(self):
        input_era = self.input_7_0.text()
        if input_era == "":
            msg = "Era can not be an empty string."        
            QMessageBox.warning(self, "Notification:", msg,
                                QMessageBox.Close)
        else:
            settings.current_era = input_era
            self.label_8_0.setText("Current era set to: " + settings.current_era) 
            msg = "Era successfully set."  
            QMessageBox.information(self, "Notification:", msg) 

    def reset_values(self):
        settings.testnet_magic = "2"
        self.input_4_0.setText("")
        self.label_5_0.setText("Current testnet magic set to: " + settings.testnet_magic)
        
        settings.current_era = "babbage-era"
        self.input_7_0.setText("")
        self.label_8_0.setText("Current era set to: " + settings.current_era)   

        msg = "Default values successfully restored."  
        QMessageBox.information(self, "Notification:", msg) 

    def set_net(self, selected_net):
        self.net = selected_net 

    def generate_protocol_params_file(self):
        if self.net == "":
            msg = "Select option mainnet or testnet."    
            QMessageBox.warning(self, "Notification:", msg,
                                QMessageBox.Close)
            return None

        if self.net == "mainnet": 
            net_part =  "--mainnet "
        elif self.net == "testnet":
            net_part = "--testnet-magic " + settings.testnet_magic + " "
        
        file_number_count = 0
        while(True):
            if file_number_count == 0:
                prepend_num = ""
            else:
                prepend_num = str(file_number_count)
            
            pp_file_name = "protocol" + prepend_num + ".json"
            pp_file_path = settings.folder_path + "/" + pp_file_name
            pp_file_exists = os.path.isfile(pp_file_path)
            
            if not pp_file_exists:
                self.pp_file_name = pp_file_name
                break

            file_number_count += 1

        command = "cardano-cli query protocol-parameters " + \
                  net_part + \
                  "--out-file " + self.pp_file_name 

        if settings.debug_mode:
            print("Command below is defined in py-files/developer.py line 182:")
            print(common_functions.format_command(command) + "\n")
        else:
            try:
                subprocess.Popen(command.split(), cwd=settings.folder_path) 
                self.input_15_0.setText(self.pp_file_name)
                msg = "Protocol parameters file successfully generated." 
                QMessageBox.information(self, "Notification:", msg)
            except Exception:
                output = traceback.format_exc()
                common_functions.log_error_msg(output)
                
                msg = "Protocol parameters file could not be generated.\n" + \
                      "Check if cardano node is running and is synced.\n" + \
                      "Look at the error.log file for error output." 
                QMessageBox.warning(self, "Notification:", msg,
                                    QMessageBox.Close)  