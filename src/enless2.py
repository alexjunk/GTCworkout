#!/usr/bin/env python3

import serial
import binascii
import time

ser = serial.Serial(
 port='/dev/ttyAMA0',
 baudrate = 19200,
 parity=serial.PARITY_NONE,
 stopbits=serial.STOPBITS_ONE,
 bytesize=serial.EIGHTBITS,
 timeout=1,
 write_timeout=1
)
print(ser.is_open)

verbose = True

rcv = [0x21, 0x52, 0x09, 0x21]

def install(frame, interval):
    """
    frame : enless frame sans les 2 premiers octets et sans le dernier (0x16)
    interval : intervalle en minutes entre 2 envois de données par le transmetteur
    """
    root = bytearray([0x7A, 0x01, 0x00, 0x00, 0x00, 0x2f, 0x2f, 0x0F, 0x7F])
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
    if verbose:
        #print([hex(x) for x in message])
        print(binascii.b2a_hex(message))
    try :
        ser.flushOutput()
        n = ser.write(message)
        ser.write(b'\n')
    except IOError as e:
        print("ERROR {}".format(e))
    finally:
        print("wrote {} bytes on the serial port".format(n))
        #ser.flush()

def installb():
    """
    just a test
    """
    try :
        n = ser.write("167a010000002f2f0f7f11020112220760050021095221".encode('utf-8'))
    except IOError as e:
        print("ERROR {}".format(e))
    finally:
        print("wrote {} bytes on the serial port".format(n))

# mode 0 : avec get()
# sinon on utilise readline()
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

def decodeMeasure(data):
    print("decoding a measurement")
    if data[1] in [0x01,0x02]:
        temp = int.from_bytes(data[3:5], byteorder='little')/10
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
        print(binascii.b2a_hex(data))
        rssi = frame[-1]/2
        print("rssi is {:.1f}".format(rssi))
        txid = frame[3:7][::-1]
        txidstr = "{:02x}{:02x}{:02x}{:02x}".format(txid[0],txid[1],txid[2],txid[3])
        if data[0] == 0x10 :
            print("Installation request coming from {}".format(txidstr))
            install(frame,5)
            #installb()
        if data[0] == 0x12:
            print("got the ACK")
        if data[0] in [0x01,0x02,0x03,0x04,0x23,0x24,0x25,0x26,0x27] :
            decodeMeasure(data)
    time.sleep(1)

ser.close()
