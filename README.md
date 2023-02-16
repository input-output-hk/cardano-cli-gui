# cardano-cli-gui
Simple GUI that cover some basic functionality of the Cardano CLI command line tool.<br>
**IMPORTANT:** Project is under construction and may contain bugs. 

To run the GUI you can use the executable files. You can also run it from the terminal.
In that case you need to have `python 3` and `PyQt 5` installed:<br>
`python cardano-cli-gui.py`

**IMPORTANT:** To use the *query* and *send* command in the GUI a cardano node has to be 
running and synced to the test or main network.

The GUI functionality is seperated in 4 tabs and covers following things:

1. **Start** tab, that notifies the user that he has to set a valid folder path to unlock
other tabs. The folder path will be used to load and save key and address files. It also
displays if the *Debug mode* is set ON or OFF.

![alt text](https://github.com/LukaKurnjek/cardano-cli-gui/blob/main/images/start.png) 

2. **Wallet** tab, that handles loading or generating verification and signing keys, 
payment addresses and payment public key hashes.  

![alt text](https://github.com/LukaKurnjek/cardano-cli-gui/blob/main/images/wallet.png)

3. **Transactions** tab, that handles checking funds for a payment address and sending 
funds to a receiving address.

![alt text](https://github.com/LukaKurnjek/cardano-cli-gui/blob/main/images/transactions.png)

4. **Script address** tab, that handles building a script payment address for a script 
file. You can also send funds to the generated script address and attach a datum to the 
transaction. 

![alt text](https://github.com/LukaKurnjek/cardano-cli-gui/blob/main/images/smart_contract.png)
