#!/usr/bin/env python3

import serial
import binascii
import time

port = "/dev/ttyUSB0"
#port = "/dev/ttyAMA0"

ser = serial.Serial(
 port = port,
 baudrate = 19200,
 parity=serial.PARITY_NONE,
 stopbits=serial.STOPBITS_ONE,
 bytesize=serial.EIGHTBITS,
 timeout=1,
 write_timeout=1
)
print(ser.is_open)

verbose = True

# l'adresse du receiver
rcv = [0x21, 0x52, 0x09, 0x21]

# la racine des messages enless, depuis le M field jusqu'au VIF byte
root = bytearray([0x7A, 0x01, 0x00, 0x00, 0x00, 0x2f, 0x2f, 0x0F, 0x7F])

# mode 0 : implémente get()
# mode différent de 0 : implémente readline()
mode = 0

def get():
    """
    return the enless frame
    """
    while 1:
      if mode == 0 :
        # we read a byte
        a = ser.read()
        # if the byte is 0x68, we have a packet
        if a and a[0] == 0x68:
            # we read one more byte to get the length
            b = ser.read()
            # we read the packet plus the x16 and return
            c = ser.read(b[0]+1)
            if c[-1] == 0x16:
                return c[:-1]
      else :
        x = ser.readline()
        if x :
          if x[0] == 0x68 and x[-1] == 0x16 :
            # x[1] doit être égal à la taille du paquet, moins 3 octets (lui-même, start et stop)
            if x[1] == len(x) - 3 :
                return x[2:-1]

def send(message):
    """
    write a payload message on the serial port
    """
    if verbose:
        #print([hex(x) for x in message])
        print(binascii.b2a_hex(message))
    try :
        ser.flushOutput()
        n = ser.write(message)
        #ser.write(b'\n')
    except IOError as e:
        print("ERROR {}".format(e))
    finally:
        print("wrote {} bytes on the serial port".format(n))
        #ser.flush()

def install(frame, interval):
    """
    installation packet to be send by the receiver

    frame : enless frame sans les 2 premiers octets et sans le dernier (0x16)

    interval : intervalle en minutes entre 2 envois de données par le transmetteur
    """
    data = bytearray([0x11, frame[19], 0x01, *frame[3:7][::-1], interval, 0x00, *rcv[::-1]])
    # cf partie 4 - with enless receiver
    l = len(root) + len(data)
    message = bytearray([l, *root, *data])
    # cf partie 3 - over the air
    """
    m = bytearray([0x44, 0x24, 0x48, *frame[3:9], *root, *data, 0x4D])
    l = len(m)
    message = bytearray([0x68, l, *m, 0x16])
    """
    print("going to send the installation packet")
    send(message)

def RSSIresponse(frame, nb=0x01):
    """
    installation packet to be send by the receiver

    frame : enless frame sans les 2 premiers octets et sans le dernier (0x16)
    """
    data = bytearray([0x15, frame[19], nb, *frame[3:7][::-1], frame[-1]])
    l = len(root) + len(data)
    message = bytearray([l, *root, *data])
    print("going to send the RSSI response {:02x}".format(nb))
    send(message)

def decodeMeasure(data):
    """
    decode un message périodique de données

    data : enless "data" message commencant juste après le VIF byte et s'arrêtant au RSSI byte
    """
    print("decoding a measurement")
    if data[1] in [0x01,0x02]:
        temp = int.from_bytes(data[3:5], byteorder='little', signed=True)/10
        print("temperature is {:.1f}".format(temp))
    if data[1] == 0x02:
        rh = int.from_bytes(data[5:7], byteorder='little')/10
        print("humidity is {:.1f}".format(rh))


while 1:
    frame = get()
    if frame:
        print("****************************************")
        print(binascii.b2a_hex(frame))
        data = frame[18:-1]
        # on vérifie qu'on a bien l signature d'un enless frame
        if frame[0] == 0x44 and frame[1] == 0xae and frame[2]==0x0c:
            print("enless frame")
            print("data is {}".format(binascii.b2a_hex(data)))
            rssi = frame[-1]/2
            print("rssi is {:.1f}".format(rssi))
            txid = frame[3:7][::-1]
            txidstr = "{:02x}{:02x}{:02x}{:02x}".format(txid[0],txid[1],txid[2],txid[3])
            if data[0] == 0x10 :
                print("Installation request coming from {}".format(txidstr))
                install(frame,5)
            if data[0] == 0x12:
                print("got the ACK")
                RSSIresponse(frame)
            if data[0] == 0x14:
                print("got the install RSSI flag")
                RSSIresponse(frame, nb=data[2])
            if data[0] == 0x16:
                print("INSTALLATION COMPLETED WITH SUCCESS")
            if data[0] in [0x01,0x02,0x03,0x04,0x23,0x24,0x25,0x26,0x27] :
                decodeMeasure(data)
    time.sleep(1)

ser.close()
