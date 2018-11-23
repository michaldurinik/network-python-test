#!/usr/bin/env python3
import socket
from time import sleep
from obj import cube
import pickle
import struct
import sys

HOST = "127.0.0.1"
PORT = 65432

def send_msg(sock, msg):
    # Prefix each message with a 4-byte length (network byte order)
    msg = struct.pack('>I', len(msg)) + msg
    sock.sendall(msg)

def recv_msg(sock):
    # Read message length and unpack it into an integer
    raw_msglen = recvall(sock, 4)
    if not raw_msglen:
        return None
    msglen = struct.unpack('>I', raw_msglen)[0]
    # Read the message data
    return recvall(sock, msglen)

def recvall(sock, n):
    # Helper function to recv n bytes or return None if EOF is hit
    data = b''
    while len(data) < n:
        packet = sock.recv(n - len(data))
        if not packet:
            return None
        data += packet
    return data

c = cube()
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    packet = pickle.dumps(c)
    print(sys.getsizeof(packet))
    send_msg(s, packet)
    data = recv_msg(s)
    print(sys.getsizeof(data))
    #print(pickle.loads(data))
    #i = "0"
    #i = i.encode()
    #i = pickle.dumps(c)
    #s.sendall(i)
    #fragments = []
    #while True:
    #    chunck = s.recv(1024)
    #    if not chunck:
    #        break
    #    fragments.append(chunck)

    #i = "".join(fragments)
    #print(i)
    #i = s.recv(1024)
    #print("Received:", repr(i))
    #i = int(i)
    #i += 1
    #i = str(i)
    #i = i.encode()
    sleep(2)
