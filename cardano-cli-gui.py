

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
        settings.init()

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

        tutorial_btn = QAction("&Tutorial", self)
        help_menu.addAction(tutorial_btn)

        # Create tabs and add windows 
        tabs = QTabWidget()
        tabs.setTabPosition(QTabWidget.North)
        tabs.setMovable(True)

        tabs.addTab(Start(),"Start")
        tabs.addTab(Wallet(),"Wallet")
        tabs.addTab(Transactions(),"Transactions")
        tabs.addTab(Smart_contracts(),"Smart contrancts")
        self.setCentralWidget(tabs)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()

