# Installer files for cardano-cli-gui
Installer files are provided for Windows, Mac OS and Linux.

Executables were created with the `pyinstaller` tool:
`pyinstaller --onefile cardano-cli-gui_all.py --noconsole`

The folder `create_single_file` contains the python script `create_cardano-cli-gui_all.py` 
that creates a single python file `create_cardano-cli-gui_all.py`.

This file contains the code from the `create_cardano-cli.py` file and 
the code from other python files located in `py-files` folder. 
