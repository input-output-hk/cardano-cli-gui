
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import (QPushButton, QLabel, QLineEdit, 
                             QWidget, QGridLayout, QRadioButton,
                             QComboBox)

class Smart_contracts(QWidget):
    def __init__(self):
        super().__init__()

        # Creating local variables
        self.address = ""
        self.skey_name = ""
        self.net = ""
        self.era = ""
        self.utxo = ""
        self.script_address = ""
        self.command_failed = False

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
        self.label_3_0 = QLabel("Script payment address file name:")
        self.input_4_0 = QLineEdit()
        self.button_4_1 = QPushButton("Set")
        self.button_4_2 = QPushButton("Generate")
        self.label_5_0 = QLabel("Select mainnet or testnet:")
        self.comboBox_6_0 = QComboBox()
        self.label_7_0 = QLabel("Script payment address:")
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
        self.label_9_0 = QLabel("Type in your address:")
        self.input_10_0 = QLineEdit()
        self.button_10_1 = QPushButton("Set")
        self.label_11_0 = QLabel("Type in your signing key file name:")
        self.input_12_0 = QLineEdit()
        self.button_12_1 = QPushButton("Set")
        self.label_13_0 = QLabel("Send amount (seperat decimal number with dot):")
        self.input_14_0 = QLineEdit()
        self.radioButton_14_1 = QRadioButton("Ada")
        self.radioButton_14_2 = QRadioButton("Lovelace")
        self.label_15_0 = QLabel("Select era:")
        self.comboBox_16_0 = QComboBox()
        self.label_17_0 = QLabel("Input UTxO address:")
        self.input_18_0 = QLineEdit()
        self.button_18_1 = QPushButton("Set")
        self.label_19_0 = QLabel("Type in datum file name:")
        self.input_20_0 = QLineEdit()
        self.button_20_1 = QPushButton("Set")

        self.button_22_0 = QPushButton("Send")

        # Widget actions for building script address section  
        self.button_10_1.clicked.connect(self.set_sending_address)
        self.button_12_1.clicked.connect(self.set_signing_key)

        self.comboBox_16_0.addItems(["", "byron-era", "shelley-era", "allegra-era", "mary-era", "alonzo-era", "babbage-era"])
        self.comboBox_16_0.currentTextChanged.connect(self.update_era)

        self.button_18_1.clicked.connect(self.set_utxo)
        self.button_20_1.clicked.connect(self.set_datum)
        self.button_22_0.clicked.connect(self.send_funds)

        # Set label fonts 
        labels = [self.label_0_0, self.label_1_0, 
                  self.label_3_0, self.label_5_0, 
                  self.label_7_0, self.label_9_0, 
                  self.label_11_0, self.label_13_0, 
                  self.label_15_0, self.label_17_0, 
                  self.label_19_0] 
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
        layout.addWidget(self.comboBox_16_0, 16, 0)
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
        pass

    def set_script_address_file(self):
        pass

    def generate_script_address_file(self):
        pass 

    def set_net(self):
        pass

    def show_script_address(self):
        pass

    def set_sending_address(self):
        pass

    def set_signing_key(self):
        pass

    def update_era(self):
        pass 

    def set_utxo(self):
        pass

    def set_datum(self):
        pass

    def send_funds(self):
        pass

    