# APRS via LoRa

This project was started because I need a simple way to check the range of the LoRa Data Radio Modems DRF1278DM from Dorji. My repository contains two python scripts and an example configuration file. The tracker.py is grabbing data from gpsd, build a packet for APRS and send it to a serial attached data modem. It also print the raw data to stdout.

The igate.py receive data over the air from a serial attached data modem. This script is forwarding received APRS-Packets to APRS-IS (http://www.aprs-is.net/) and print receive to stdout.

# Hardware Requirements

* 2 Computers with Linux and Python 3 (Raspberry Pi zero work great)
* 2 LoRa Data Radio Modems (tested with DRF1278DM from Dorji)
* at least one UART to USB Adapter
* if you use desktop and laptop and no Raspberry Pi you need three UART to USB adapters 

You need at least two serial data modems like the Dorji DRF1278DM and two computers. For running tracker.py you need also a GPS module.

# Quickstart

Connect a DRF1278DM or similiar device to your two computers or Raspberry Pi.

Clone repository and copy configuration template.

	git clone https://github.com/laemmy/APRS-via-LoRa-Gateway.git
	cp config-template.txt config.txt

Install **aprslib** on both computers.
  
    pip3 install aprslib

Edit **config.txt** on your Igate-Computer and enter your Callsign, APRS-IS passcode and serial interface in section [IGATE].
Then edit **config.txt** on your Tracker-Computer and enter your Callsign, APRS-IS passcode and serial interface section [TRACKER].

Execute **igate.py** on your Igate-Computer to start it.

    ./igate.py
    
To quit just press **CONTROL+C**

## Setup APRS Tracker

Setup the tracking Raspberry Pi is more complex. **tracker.py** is grabbing the data from gpsd. For running gpsd you need a GPS module which is connected to your computer. Please follow this guide for setting up GPS module on Raspberry Pi

https://learn.adafruit.com/adafruit-ultimate-gps-hat-for-raspberry-pi/use-gpsd

If you have everything setup correctly please use **cgps -s** to check gps location. Everything fine? The just start **tracking.py** and move around to do range testing of your LoRa-Modem.








  

