#!/usr/bin/python3
import socket
import pickle
import struct
import sys
from obj import Cube
# server receive data and send them back to client and close itself

HOST = "127.0.0.1"
PORT = 20001


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


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    while True:
        s.listen(1)
        print("listening for connections...")
        conn, addr = s.accept()
        with conn:
            print("Connected by: ", addr)
            while True:
                data = recv_msg(conn)
                if not data:
                    break
                # print(pickle.loads(data))
                send_msg(conn, data)
                # data = conn.recv(1024)
                # if not data:
                #     break
                # conn.sendall(data)
        print("Connection closed:", addr)
