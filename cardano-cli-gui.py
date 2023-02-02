

import sys
sys.path.insert(1, './py-files')
from wallet import Wallet
from start import Start

from PyQt5.QtWidgets import (QApplication, QMainWindow, QTabWidget)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Cardano client GUI 1.0")
        
        tabs = QTabWidget()
        tabs.setTabPosition(QTabWidget.North)
        tabs.setMovable(True)

        tabs.addTab(Start(),"Start")
        tabs.addTab(Wallet(),"Wallet")
        self.setCentralWidget(tabs)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()

