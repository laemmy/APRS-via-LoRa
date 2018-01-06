#!/usr/bin/env python3
import serial
import aprslib
import signal
import sys
from configparser import ConfigParser


try:
    with open('config.txt') as file:
        pass
except IOError as e:
    print ("config.txt does not exist.")
    exit()



config = ConfigParser()
config.read('config.txt')
callsign = config.get('DEFAULT', 'Callsign')
passcode = config.get('DEFAULT', 'Passcode')
interface = config.get('DEFAULT', 'Interface')


def signal_handler(signal, iframe):
    print ('Igate stopped....')
    sys.exit(0)
signal.signal(signal.SIGINT, signal_handler)

ser = serial.Serial(interface)
ser.flushInput()
ser.flushOutput()

AIS = aprslib.IS(callsign, passcode, port=14580)
AIS.connect()
print ('Igate started ...')
while True:
    data_raw = ser.readline().decode("utf-8")
    print(data_raw)
    AIS.sendall(str(data_raw))
