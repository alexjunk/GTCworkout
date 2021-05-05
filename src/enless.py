#!/usr/bin/env python3

import serial
#import binascii
import time

ser = serial.Serial(
 port='/dev/ttyAMA0',
 baudrate = 19200,
 parity='N',
 stopbits=1,
 bytesize=8,
 timeout=1
)

while 1:
    x=ser.readline()
    #y = binascii.b2a_hex(x)
    if len(x) :
        # on vérifie le premier et le dernier octet
        if hex(x[0]) == '0x68' and hex(x[-1]) == '0x16' :
            # x[1] doit être égal à la taille du paquet, moins 3 octets (lui-même, start et stop)
            if x[1] == len(x) - 3 :
                print("Enless frame received")
                serNb = "{:02X}{:02X}{:02X}{:02X}".format(x[8],x[7],x[6],x[5])
                print("Sensor {}".format(serNb))
    time.sleep(1)

ser.close()
