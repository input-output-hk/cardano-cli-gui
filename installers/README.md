# Installer files for cardano-cli-gui
Installer files are provided for Windows, Mac OS and Linux.

Executables were created with the `pyinstaller` tool:<br>
`pyinstaller --onefile cardano-cli-gui_all.py --noconsole`

The folder `create_single_file` contains the python script:<br>
`create_cardano-cli-gui_all.py` 

This script creates a single python file `create_cardano-cli-gui_all.py`
that contains code from: 
- `create_cardano-cli.py` file 
- python files located in `py-files` folder 
