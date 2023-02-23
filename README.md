# cardano-cli-gui
Simple GUI that cover some basic functionality of the Cardano CLI command line tool.<br>

To run the GUI you can use the executable files in the `executables/` folder. Download 
the executable for your OS. If you want to use the GUI also in debug mode you should run 
the executable from a terminal window. Then in debug mode the GUI prints the cardano-cli 
commands to the terminal window instead of acctually executing them. 

You can also run the GUI from source. In that case you need to have `python 3` and `PyQt 5` 
installed for the GUI to work. Simply download this repository, open a terminal in the 
downloaded folder and run:<br>
`python cardano-cli-gui.py`

**IMPORTANT:** To use the *query* and *send* command in the GUI a cardano node has to be 
running and synced to the test or main network. 

To run a cardano node download it from [here](https://github.com/input-output-hk/cardano-node/releases) 
and install it. Then download the configurations files for the Preview testnet from 
[here](https://book.world.dev.cardano.org/environments.html#preview-testnet) or for the Production 
mainnet from [here](https://book.world.dev.cardano.org/environments.html#production-mainnet). 
From the folder that contains your configuration files run: 
```s
cardano-node run \
 --topology topology.json \
 --database-path db \
 --socket-path node.socket \
 --host-addr 0.0.0.0 \
 --port 3001 \
 --config config.json
```

The `node.socket` file will be created in the folder from where you ran the above command. 
Before you use the GUI create the environment variable `CARDANO_NODE_SOCKET_PATH`. If you 
are using bash add the following line to the end of your `.bashrc` file and source it:<br>
`export CARDANO_NODE_SOCKET_PATH="$HOME/path/to/node.socket"`

The GUI functionality is seperated in 5 tabs and covers following things:

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

4. **Smart contracts** tab, that handles building a script payment address for a script 
file. You can also send funds to the generated script address and attach a datum to the 
transaction. 

![alt text](https://github.com/LukaKurnjek/cardano-cli-gui/blob/main/images/smart_contract.png)

5. **Developer** tab, that lets more experienced users to set a different testnet 
magic number or update the era parameter. 

![alt text](https://github.com/LukaKurnjek/cardano-cli-gui/blob/main/images/developer.png)