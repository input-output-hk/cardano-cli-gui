

import sys
sys.path.insert(1, './py-files')

import settings
from start import Start
from wallet import Wallet
from transactions import Transactions
from smart_contracts import Smart_contracts

from PyQt5.QtWidgets import (QApplication, QMainWindow, QTabWidget, QAction)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Initiate global variables
        self.init_global_variables()

        # Set window title
        self.setWindowTitle("Cardano client GUI 1.0")

        # Create the applications menu 
        self.app_menu = self.menuBar()
        debug_menu = self.app_menu.addMenu("&Debug")
        help_menu = self.app_menu.addMenu("&Help")

        on_toggle = QAction("&ON", self)
        off_toggle = QAction("&OFF", self)

        debug_menu.addAction(on_toggle)
        debug_menu.addSeparator()
        debug_menu.addAction(off_toggle)

        on_toggle.triggered.connect(self.set_debug_on)
        off_toggle.triggered.connect(self.set_debug_off)

        tutorial_btn = QAction("&Tutorial", self)
        help_menu.addAction(tutorial_btn)

        # Create tabs and add windows 
        self.tabs = QTabWidget()
        self.tabs.setTabPosition(QTabWidget.North)
        self.tabs.setMovable(True)

        self.tabs.addTab(Start(),"Start")
        self.tabs.addTab(Wallet(),"Wallet")
        self.tabs.addTab(Transactions(),"Transactions")
        self.tabs.addTab(Smart_contracts(),"Smart contrancts")
        self.setCentralWidget(self.tabs)

    def init_global_variables(self):
        settings.folder_path = ""
        settings.debug_mode = "OFF"

    def set_debug_on(self):
        settings.debug_mode = "ON"
        self.tabs.widget(0).label_8_0.setText("Debug mode: ON")

    def set_debug_off(self):
        settings.debug_mode = "OFF"
        self.tabs.widget(0).label_8_0.setText("Debug mode: OFF")

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()

