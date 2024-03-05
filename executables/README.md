# Executable files for cardano-cli-gui
Executable files are provided for Windows and Linux. However on Windows the GUI fonts and 
sizes may get distorted. If you are using the debug option that prints commands to the terminal, 
start the executable from your terminal window.

| :zap: NixOS users can not use the executable file. Instead start a nix shell with the provided shell.nix file and run the gui from the source code as described in the README file on the main page inside the nix shell. |
|------------------------------------------------------------------------------------------------------|

Executables were created with the `pyinstaller` tool with the command:
```console
pyinstaller --onefile cardano-cli-gui_all.py
```

Before creating an executable file you need to install `Python 3` on your
OS and then install the packages `PyQt5` and `Pillow` with `pip`:
```console
pip install PyQt5
pip install Pillow
```

The folder `create_single_file/` contains the python script:
```console
create_cardano-cli-gui_all.py
``` 

This script creates a single python file `cardano-cli-gui_all.py`
that contains code from: 
- `cardano-cli-gui.py` file 
- python files located in `py-files` folder 
