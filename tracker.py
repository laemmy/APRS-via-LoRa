#!/usr/bin/env python3
from configparser import ConfigParser
import serial
import aprslib
import time
import signal
import sys
from gps3 import gps3

import serial

try:
    with open('config.txt') as file:
        pass
except IOError as e:
    print ("config.txt does not exist.")
    exit()

config = ConfigParser()
config.read('config.txt')
callsign  = config.get('TRACKER', 'Callsign')
interface = config.get('TRACKER', 'Interface')
interval  = int(config.get('TRACKER', 'interval'))
ser = serial.Serial(interface)

def signal_handler(signal, iframe):
    print ('\nTracker stopped...')
    sys.exit(0)
signal.signal(signal.SIGINT, signal_handler)

def encodeLonLat(lon, lat, symid, symbol):
    lat_deg = int(abs(lat) // 1)
    lat_min = round(60. * (lat % 1), 2)
    nw = "N" if lat >= 0 else "S"
    lat_result = str(lat_deg).zfill(2) + '%05.2f' % lat_min + str(nw)

    lon_deg = int(abs(lon) // 1)
    lon_min = round(60 * (lon % 1), 2)
    ew = "W" if lon <= 0 else "E"

    lon_result = str(lon_deg).zfill(3) + '%05.2f' % lon_min + ew

    return lat_result + symid + lon_result + symbol


gps_socket = gps3.GPSDSocket()
data_stream = gps3.DataStream()
gps_socket.connect()
gps_socket.watch()
for new_data in gps_socket:
    if new_data:
        data_stream.unpack(new_data)

        latitude = data_stream.TPV['lat']
        longitude = data_stream.TPV['lon']

        if latitude != longitude:
            position = encodeLonLat(
                float(longitude), float(latitude), "/", ">")
            beacon =  callsign + '>APRS,WIDE1-1:=' + \
                position + 'LoRa Reichweitentest\n'
            print (beacon)
            ser.write(beacon.encode())
            time.sleep(interval)
