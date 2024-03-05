# cardano-cli-gui
Simple GUI that covers some basic functionality of the [Cardano CLI](https://github.com/intersectmbo/cardano-cli/) 
command line tool. The GUI was created by IOGs education team for learning purposes and was tested with 
[Cardano node 8.7.3](https://github.com/IntersectMBO/cardano-node/releases/tag/8.7.3).  

| :warning: WARNING                                                                                         |
|:----------------------------------------------------------------------------------------------------------|
| The GUI was created for educational purposes and is not regularly updated with changes in the Cardano CLI.
Using the GUI with a different version of a Cardano node may break some functionality of the GUI.
If you are using the GUI for submitting transactions on the main net you are doing so at your own risk.     |

To run the GUI you can use the executable files in the `executables/` folder. Download the executable for your OS. 

| :memo:        | The GUI can also run in debug mode where it prints the `cardano-cli` commands to the terminal window instead of executing them.|
|---------------|:-------------------------------------------------------------------------------------------------------------------------------|

If you want to use the GUI in debug mode you should run the executable from a terminal window. 
In non-debug mode the GUI writer possible errors to the error.log file.  

You can also run the GUI from source. In that case you need to have `python 3` and the `PyQt 5` 
library installed. Once installed download this repository, open a terminal in it and run:  
```console
python cardano-cli-gui.py
```

**IMPORTANT: For most of the GUIs functionality a cardano node has to be running and synced to the test or main network.**

To run a cardano node download it from the [Cardano node releases](https://github.com/input-output-hk/cardano-node/releases) page and install it. The installer files are located under the Assets section that needs to be expanded. Add all executable files including the `cardano-node` and `cardano-cli` to you system path, e.g. copy them to `/usr/local/bin/` if you are using a Linux OS. 

Then download the configurations files from the [Environments configuration files](https://book.world.dev.cardano.org/environments.html) page. You can chose configuartion files depending on the network you want to run your Cardano node in. 

From the folder that contains the configuration files you have downloaded run:  
```console
cardano-node run \
 --topology topology.json \
 --database-path db \
 --socket-path node.socket \
 --host-addr 0.0.0.0 \
 --port 3001 \
 --config config.json
```

The `node.socket` file will be created in the folder from where you ran the above command. 
Stop the node and add to your system path the following environment variable
```console
CARDANO_NODE_SOCKET_PATH="<path>/<to>/node.socket"
```
If you are using a Linux OS you can do this by adding to the the follwoing line at end of your *.bashrc* file that is located in your HOME folder: 
```console
export CARDANO_NODE_SOCKET_PATH="$HOME/<path>/<to>/node.socket"
```
After that source the *.bashrc* file:  
```console
source ~/.bash.rc
```
Once you have added this envrionment variable start the cardano node again. You can check how much the node is synced if you go to the **Query** tab of the GUI. 
There select mainnet or testnet and press the *Query info* button. If you then scroll down in the text box you will see the field *syncProgress*. 

You can also check the sync progress for the preview or preprod testnet with the following command:  
```console
cardano-cli query tip --testnet-magic <testnet_number> 
```
For the testnet number use 1 for preprod and 2 for preview. 

GUI design
----------

The GUI functionality is seperated in 7 tabs and covers following things:

1. **Start** tab: notifies the user to set a valid folder path to unlock other tabs. 
The folder path will be used to load and save any filles as key and address files. It also
displays if the *Debug mode* is set ON or OFF.  

![alt text](https://github.com/input-output-hk/cardano-cli-gui/blob/main/images/start.png) 

2. **Wallet** tab: loads or generates verification and signing keys, payment addresses and 
payment public key hashes.  

![alt text](https://github.com/input-output-hk/cardano-cli-gui/blob/main/images/wallet.png)

3. **Transactions** tab: checks funds for a payment address and sends funds to a receiving address.  

![alt text](https://github.com/input-output-hk/cardano-cli-gui/blob/main/images/transactions.png)

4. **Smart contracts - send** tab: builds a script payment address for a script file and sends funds 
to the generated script address. You can attach a datum to the transaction.  

![alt text](https://github.com/input-output-hk/cardano-cli-gui/blob/main/images/smart_contracts_send.png)

5. **Smart contracts - receive** tab: creates a spending transactions that spends a script address UTxO. 
You can attach a datum and a redeemer to the transaction and set a validity interval.  

![alt text](https://github.com/input-output-hk/cardano-cli-gui/blob/main/images/smart_contracts_receive.png)

6. **Query** tab: queries an address for funds, queries network information and shows the transaction 
hash for a signed transaction file.   

![alt text](https://github.com/input-output-hk/cardano-cli-gui/blob/main/images/query.png)

7. **Developer** tab: sets the testnet number, updates the era parameter and generates
the protocol parameters file for the chosen network.  

![alt text](https://github.com/input-output-hk/cardano-cli-gui/blob/main/images/developer.png)
