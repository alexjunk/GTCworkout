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

deviceTypes = {
               "0x1": "temperature",
               "0x2": "temperature and humidity",
               "0x3": "P100",
               "0x4": "pulse",
               "0x5": "energy meter",
               "0x7": "modbus receiver",
               "0x23": "contact",
               "0x24": "CO2",
               "0x25": "4-20mA analog",
               "0x26": "0-5V analog",
               "0x27": "0-10V analog"
              }

rcv = [0x21, 0x52, 0x09, 0x21]

def installPacket(tx, interval):
    """
    tx : paquet de données envoyé par le transmetteur
    interval : intervalle en minutes entre 2 envois de données par le transmetteur 
    """
    txdata = tx[20:-2]
    root = [0x7A, 0x1E, 0x00, 0x00, 0x00, 0x2f, 0x2f, 0x0F, 0x7F]
    data = [0x11, txdata[1], 0x01, tx[5], tx[6], tx[7], tx[8], interval, 0x00, rcv[3], rcv[2], rcv[1], rcv[0]]
    l = len(root) + len(data)
    packet = serial.to_bytes([l, *root, *data])
    print(binascii.b2a_hex(packet))


while 1:
    x=ser.readline()
    y = binascii.b2a_hex(x)
    if len(x) :
        # on vérifie le premier et le dernier octet
        if hex(x[0]) == '0x68' and hex(x[-1]) == '0x16' :
            # x[1] doit être égal à la taille du paquet, moins 3 octets (lui-même, start et stop)
            if x[1] == len(x) - 3 :
                print("Enless frame received")
                serNb = "{:02X}{:02X}{:02X}{:02X}".format(x[8],x[7],x[6],x[5])
                print("Sensor {}".format(serNb))
                # message
                data = x[20:-2]
                print(hex(data[0]))
                mnb = hex(data[1])
                print(deviceTypes[mnb])
                installPacket(x,5)
                print(x)
                print(y)
    time.sleep(1)

ser.close()
