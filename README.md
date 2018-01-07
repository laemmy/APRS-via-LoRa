# APRS-via-LoRa

This project was started because I need a simple way to check the range of the LoRa Data Radio Modems DRF1278DM from Dorji. My repository contains two python scripts and an example configuration file. The tracker.py is grabbing data from gpsd, build a packet for APRS and send it to a serial attached data modem. It also print the raw data to stdout.

The igate.py receive data over the air from a serial attached data modem. This script is forwarding received APRS-Packets to APRS-IS (http://www.aprs-is.net/) and print receive to stdout.

You need at least two serial data modems like the Dorji DRF1278DM and two computers. For running tracker.py you need also a GPS module.

# Quickstart

Connect a DRF1278DM or similiar device to your two computers or Raspberry Pi.

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
  

