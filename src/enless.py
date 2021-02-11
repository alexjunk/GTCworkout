#!/usr/bin/env python3

import serial
import binascii
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
    y = binascii.b2a_hex(x)
    if len(y):
        print("longueur {}".format(len(y)))
        print(y)
    time.sleep(1)

ser.close()
