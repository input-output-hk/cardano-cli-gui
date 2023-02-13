

import os
import sys
sys.path.insert(1, './py-files')

import settings
from wallet import Wallet
from transactions import Transactions
from smart_contracts import Smart_contracts

from PyQt5.QtCore import QSize 
from PyQt5.QtGui import QPixmap 
from PyQt5.QtWidgets import (QApplication, QMainWindow, QTabWidget, 
                             QAction, QPushButton, QLabel, QLineEdit, 
                             QWidget, QGridLayout, QMessageBox)

class MainWindow(QMainWindow):
    def __init__(self):
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
        settings.folder_path = ""
        settings.debug_mode = False

    # Sets debug mode to ON
    def set_debug_on(self):
        settings.debug_mode = True
        
        self.label_8_0.setText("Debug mode: ON")
        # When start window was in a separated class
        # self.tabs.widget(0).label_8_0.setText("Debug mode: OFF")

    # Sets debug mode to OFF
    def set_debug_off(self):
        settings.debug_mode = False
        
        self.label_8_0.setText("Debug mode: OFF")
        # When start window was in a separated class
        # self.tabs.widget(0).label_8_0.setText("Debug mode: OFF")

    # Creates the start tab window
    def init_start_tab(self):
        # Initial message
        label_1_0 = QLabel("To unlock other tabs set a valid folder path.\nAll files will be loaded or saved to this folder.")

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
        label_9_0 = QLabel("If debug mode is ON, the programm prints the cardano-cli\ncommands to the terminal instead of executing them.")
        label_11_0 = QLabel("IMPORTANT:")
        label_12_0 = QLabel("A cardano node has to be synced and running.")

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

    def set_folder_path(self):
        folder_path_input = self.input_4_0.text()
        if folder_path_input[-1] == "/":
            folder_path_input = folder_path_input[0:-1]
        folder_exists = os.path.isdir(folder_path_input)
        
        if folder_exists:
            settings.folder_path = folder_path_input
            self.label_6_0.setText(folder_path_input)
 
            self.tabs.addTab(Wallet(),"Wallet")
            self.tabs.addTab(Transactions(),"Transactions")
            self.tabs.addTab(Smart_contracts(),"Smart contrancts")
        else:
            self.input_4_0.setText(settings.folder_path)
            msg = "This path is not a valid folder path."                    
            QMessageBox.warning(self, "Notification:", msg,
                                QMessageBox.Close)

    def set_light_style(self):
        app.setPalette(settings.lightPallet)

    def set_dark_style(self):
        app.setPalette(settings.darkPalette)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()
