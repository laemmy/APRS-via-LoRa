# APRS-via-LoRa-Gateway
This script is forwarding received APRS-Packets to APRS-IS (http://www.aprs-is.net/). It was written because I need a simple way to check the range of the LoRa Data Radio Modems DRF1278DM.

# Quickstart

Connect a DRF1278DM or similiar device to a computer or Raspberry Pi. 

Clone repository and copy configuration template.

	git clone https://github.com/laemmy/APRS-via-LoRa-Gateway.git
	cp config-template.txt config.txt

Edit **config.txt** and enter your Callsign, APRS-IS passcode and serial interface. 

This script is written for Python 3 and using **aprslib**. Please install this library with the following command.
  
    pip3 install aprslib
 
To start just enter

    ./igate.py

The **igate.py** print all recieved packets to **stdout** and forward them to the APRS-IS. At the moment there is no daemon mode. Please use **screen** to run it in background.

To quit just press **CONTROL+C**
  

