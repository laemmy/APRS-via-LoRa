#!/usr/bin/python
import serial,aprslib,signal,sys

callsign = "N0CALL"       # enter your callsign (SSID is optional)
passcode = "123456"          # enter your passcode (grab it here https://apps.magicbug.co.uk/passcode/index.php)
interface= "/dev/ttyS0"     # choose your serial port (grab it with dmesg)

def signal_handler(signal, frame):
    print 'Igate stopped.'
    sys.exit(0)
signal.signal(signal.SIGINT, signal_handler)

ser = serial.Serial(interface)
ser.flushInput()
ser.flushOutput()

AIS = aprslib.IS(callsign, passcode, port=14580)
AIS.connect()
print 'Igate started'
while True:
  data_raw = ser.readline()
  print("IGATE " + data_raw)
  AIS.sendall(data_raw)
