#!/usr/bin/env python3
import socket
from time import sleep
from obj import cube
import pickle

HOST = "127.0.0.1"
PORT = 65432

c = cube()
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    #i = "0"
    #i = i.encode()
    i = pickle.dumps(c)
    while True:
        s.sendall(i)
        while True:
            chunck = s.recv(1024)
            if not chunck:
                break
            fragments.append(chunck)

        i = "".join(fragments)
        print(i)
        #i = s.recv(1024)
        #print("Received:", repr(i))
        #i = int(i)
        #i += 1
        #i = str(i)
        #i = i.encode()
        sleep(10)
