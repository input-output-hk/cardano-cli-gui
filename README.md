# cardano-cli-gui
Simple GUI for the cardano client tool.

**IMPORTANT:** To use the GUI a cardano node has to be running and synced to the network.

The GUI functionality is seperated in 4 tabs and covers following things:

1. **Start** tab, that notifies the user that a cardano node has to be
running in order for the GUI to work. The user can also set the current 
folder from this tab, that will be used to load and save files.

![alt text](https://github.com/LukaKurnjek/cardano-cli-gui/blob/main/images/start.png) 

2. **Wallet** tab, that handles loading or generating verification and 
signing keys, payment addresses and payment public key hashes. 

![alt text](https://github.com/LukaKurnjek/cardano-cli-gui/blob/main/images/wallet.png)

3. **Transactions** tab, that handles checking funds for a payment address,
and sending funds to a receiving address.

![alt text](https://github.com/LukaKurnjek/cardano-cli-gui/blob/main/images/transactions.png)

4. **Script address** tab, that handles building a script payment address 
for a script file. You can also send funds to the generated script address 
and attach a datum to the transaction. 

![alt text](https://github.com/LukaKurnjek/cardano-cli-gui/blob/main/images/smart_contract.png)
