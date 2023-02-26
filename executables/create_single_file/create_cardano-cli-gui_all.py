
# Name of file which will be created
out_file_name = "cardano-cli-gui_all.py"

# Import statements and configuration
imports = """\n
import os
import sys
import time
import subprocess
import traceback

import base64
from io import BytesIO
from PIL import Image, ImageQt

from PyQt5.QtCore import Qt
from PyQt5.QtCore import QSize 
from PyQt5.QtGui import QPixmap, QPalette, QColor, QFont
from PyQt5.QtWidgets import (QApplication, QMainWindow, QTabWidget, 
                             QAction, QPushButton, QLabel, QLineEdit, 
                             QWidget, QGridLayout, QMessageBox,
                             QRadioButton, QPlainTextEdit, QComboBox,
                             QHBoxLayout)
"""
with open(out_file_name,"w") as outFile:
    outFile.writelines(imports) 

with open("../../py-files/settings.py",'r') as inFile, open(out_file_name,"a") as outFile:
    outFile.writelines(line for line in inFile 
                       if not line.startswith("from"))
    outFile.writelines("\n\n")

# Adding bytestring for Cardano picture
with open("../../py-files/picture.py",'r') as inFile, open(out_file_name,"a") as outFile:
    outFile.writelines("\n")
    for line in inFile:
        outFile.writelines(line)
    outFile.writelines("\n")

code_for_picture = """
        # Load byte data
        byte_data = base64.b64decode(cardano_picture)
        image_data = BytesIO(byte_data)
        image = Image.open(image_data)

        # PIL to QPixmap
        qImage = ImageQt.ImageQt(image)
        image = QPixmap.fromImage(qImage)

        # QPixmap to QLabel        
"""

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
        global_statement = "global folder_path, debug_mode, testnet_magic, current_era \n"
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

        # Adding code for cardano picture
        if "picture_1_1 = QLabel" in line:
            line = code_for_picture + line

        if "picture_1_1.setPixmap" in line:
            line = "        picture_1_1.setPixmap(image)\n"

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

            # Adding code for cardano picture
            if "picture" in line and "QLabel" in line:
                line = code_for_picture + line

            if ".setPixmap" in line:
                if "picture_0_1" in line:
                    line = "        picture_0_1.setPixmap(image)\n"
                if "picture_0_2" in line:
                    line = "        picture_0_2.setPixmap(image)\n"
                if "picture_1_1" in line:
                    line = "        picture_1_1.setPixmap(image)\n"

            # Write line to file
            if class_section:
                outFile.writelines(line)

        outFile.writelines("\n\n")

proces_file("../../py-files/wallet.py")
proces_file("../../py-files/transactions.py")
proces_file("../../py-files/smart_contracts_send.py")
proces_file("../../py-files/smart_contracts_receive.py")
proces_file("../../py-files/developer.py") 

# Adding helper functions to end of file
with open("../../py-files/common_functions.py",'r') as inFile, open(out_file_name,"a") as outFile:
    code_section = False
    outFile.writelines("# Writes an error message to a log file")
    for line in inFile:
        if not code_section:
            code_section = line.startswith("# Writes an error message to a log file")

        # Change access of global variable
        if "settings." in line:
            line = "".join(line.split("settings."))

        if code_section:
            outFile.writelines(line)

# Adding content for main window of application
main_window_creation = """

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()
"""

with open(out_file_name,"a") as outFile:
    outFile.writelines(main_window_creation) 