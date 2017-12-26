# APRS-via-LoRa-Gateway
This script is forwarding received APRS-Packets to APRS-IS (http://www.aprs-is.net/). It was written in five minutes because I need the simple way to check the range of the LoRa-Modems which I have bought. 

# Quickstart

This script is written in Python and is using **aprslib**. Please install it with the following command.
  
  pip install aprslib
  
After that please download the script and make it executable.

  wget https://raw.githubusercontent.com/laemmy/APRS-via-LoRa-Gateway/master/igate.py
  chmod +x
  
After that please open **igate.py** with the editor of your choice and enter your *callsign*, *passcode* and the devicename of your serial interface.

To start just enter

  ./igate.py
  
To quit just press **CONTROL+C**


  

