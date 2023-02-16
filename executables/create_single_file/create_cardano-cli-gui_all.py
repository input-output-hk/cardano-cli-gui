
# Name of file which will be created
out_file_name = "cardano-cli-gui_all.py"

# Import statements and configuration
imports = """\n
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
"""
with open(out_file_name,"w") as outFile:
    outFile.writelines(imports) 

with open("../../py-files/settings.py",'r') as inFile, open(out_file_name,"a") as outFile:
    outFile.writelines(line for line in inFile 
                       if not line.startswith("from"))
    outFile.writelines("\n\n")

# Adding code from cardano-cli-gui.py
with open("../../cardano-cli-gui.py",'r') as inFile, open(out_file_name,"a") as outFile:
    class_section = False
    for line in inFile:
        # Which lines to include and which to exclude
        if not class_section:
            class_section = line.startswith("class")
        if "app = QApplication" in line:
            class_section = False

        # Add declaration of global variables after every function definition
        global_statement = "global folder_path, debug_mode, testnet_magic \n"
        if line.startswith(" "*4 + "def "):
            line = line + " "*8 + global_statement
        if line.startswith(" "*8 + "def "):
            line = line + " "*12 + global_statement

        # Change access of global variable
        if "settings." in line:
            line = "".join(line.split("settings."))

        # Change access of common functions
        if "common_functions." in line:
            line = "".join(line.split("common_functions."))

        # Write line to file
        if class_section:
            outFile.writelines(line)

    outFile.writelines("")

# Adding code from tab files in py-files fodler
def proces_file(file_path):
    with open(file_path,'r') as inFile, open(out_file_name,"a") as outFile:
        class_section = False
        for line in inFile:
            # Which lines to include and which to exclude
            if not class_section:
                class_section = line.startswith("class")

            # Add declaration of global variables after every function definition
            global_statement = "global folder_path, debug_mode, testnet_magic \n"
            if line.startswith(" "*4 + "def "):
                line = line + " "*8 + global_statement
            if line.startswith(" "*8 + "def "):
                line = line + " "*12 + global_statement

            # Change access of global variable
            if "settings." in line:
                line = "".join(line.split("settings."))

            # Change access of common functions
            if "common_functions." in line:
                line = "".join(line.split("common_functions."))

            # Write line to file
            if class_section:
                outFile.writelines(line)

        outFile.writelines("\n\n")

proces_file("../../py-files/wallet.py")
proces_file("../../py-files/transactions.py")
proces_file("../../py-files/smart_contracts.py")

# Adding helper functions to end of file
with open("../../py-files/common_functions.py",'r') as inFile, open(out_file_name,"a") as outFile:
    for line in inFile:
        outFile.writelines(line)
    outFile.writelines("\n")

# Adding content for main window of application
main_window_creation = """
app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()
"""

with open(out_file_name,"a") as outFile:
    outFile.writelines(main_window_creation) 