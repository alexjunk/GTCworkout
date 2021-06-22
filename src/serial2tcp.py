import serial
import binascii
import socket

"""
ser = serial.serial_for_url("socket://192.168.2.1:5000")
while 1:
    flag = ser.read(1)
    #print(binascii.b2a_hex(start))

    if flag[0] == 0x68:
        print("MBUS flag detected")
        length = int(ser.read(1)[0])
        print("trying to read {} bytes".format(length))
        data = ser.read(length)
        print(binascii.b2a_hex(data))
        ser.flushOutput()

ser.close()
"""

import socket
host = "192.168.2.1"
port = 5000
size = 1024


while 1:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host,port))
        flag = s.recv(1)
        if flag and flag[0] == 0x68:
            print("MBUS flag detected")
            length = int(s.recv(1)[0])
            data = s.recv(length)
            stop = s.recv(1)
            if stop[0] == 0x16:
                print(binascii.b2a_hex(data))

s.close()
