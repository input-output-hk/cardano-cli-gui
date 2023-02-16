# Installer files cardano-cli-gui
Installer files are provided for Windows, Mac OS and Linux.

Executables were created with the `pyinstaller` tool:
`pyinstaller --onefile cardano-cli-gui_all.py --noconsole`

The python script `create_cardano-cli-gui_all.py` creates a single 
python file `create_cardano-cli-gui_all.py`that contains all the code 
from the `create_cardano-cli.py` file and the other python files 
located in `py-files` folder. 
