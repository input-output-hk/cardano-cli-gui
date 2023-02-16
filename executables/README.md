# Executable files for cardano-cli-gui
Executable files are provided for Windows, Mac OS and Linux.

If you are using the debug option that prints commands to the terminal,
start the executable from your terminal window.

Executables were created with the `pyinstaller` tool with the command:<br>
`pyinstaller --onefile cardano-cli-gui_all.py --noconsole`

The folder `create_single_file` contains the python script:<br>
`create_cardano-cli-gui_all.py` 

This script creates a single python file `cardano-cli-gui_all.py`
that contains code from: 
- `cardano-cli-gui.py` file 
- python files located in `py-files` folder 