#!/usr/bin/env python3

import serial
import binascii
import time

ser = serial.Serial(
 port='/dev/ttyAMA0',
 baudrate = 19200,
 parity=serial.PARITY_NONE,
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

verbose = True

rcv = [0x21, 0x52, 0x09, 0x21]

def install(tx, interval):
    """
    tx : paquet de données envoyé par le transmetteur
    interval : intervalle en minutes entre 2 envois de données par le transmetteur 
    """
    root = [0x7A, 0x5D, 0x00, 0x00, 0x00, 0x2f, 0x2f, 0x0F, 0x7F]
    data = [0x11, tx[21], 0x01, *tx[5:9][::-1], interval, 0x00, *rcv[::-1]]
    # cf partie 4 - with enless receiver
    l = len(root) + len(data)
    message = [l, *root, *data]
    # cf partie 3 - over the air
    """
    m = [0x44, 0x24, 0x48, *tx[5:11], *root, *data, 0x4D]
    l = len(m)
    message = [0x68, l, *m, 0x16]
    """
    pkt = serial.to_bytes(message)
    if verbose:
        print(message)
        print([hex(x) for x in message])
        print(binascii.b2a_hex(pkt))
    n = ser.write(pkt)
    if n:
        print("wrote {} bytes on the serial port".format(n))


while 1:
    x=ser.readline()
    y = binascii.b2a_hex(x)
    print(y)
    if len(x) :
        # on vérifie le premier et le dernier octet
        if hex(x[0]) == '0x68' and hex(x[-1]) == '0x16' :
            # x[1] doit être égal à la taille du paquet, moins 3 octets (lui-même, start et stop)
            if x[1] == len(x) - 3 :
                serNb = "{:02X}{:02X}{:02X}{:02X}".format(x[8],x[7],x[6],x[5])
                print("Frame received from enless sensor {}".format(serNb))
                # message
                data = x[20:-2]
                rssi = x[-2]/2
                print("rssi is {:.1f}".format(rssi))
                if data[0] == 0x10:
                    t = deviceTypes[hex(data[1])]
                    print("This is an installation request from {} transmitter".format(t))
                    install(x,5)
                if data[0] == 0x12:
                    print("got the ACK")
                if data[0] in [0x01,0x02,0x03,0x04,0x23,0x24,0x25,0x26,0x27] :
                    print("got a measurement")
                    if data[1] in [0x01,0x02]:
                        temp = int.from_bytes(data[3:5], byteorder='little')/10
                        print("temperature is {:.1f}".format(temp))
                    if data[1] == 0x02:
                        rh = int.from_bytes(data[5:7], byteorder='little')/10
                        print("humidity is {:.1f}".format(rh))

    time.sleep(1)

ser.close()
