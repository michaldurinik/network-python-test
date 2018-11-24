#!/usr/bin/python3
import socket
#server receive data and send them back to client and close itself

HOST = "127.0.0.1"
PORT = 65432

#while True:
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(1)
    conn, addr = s.accept()
    with conn:
        print("Connected by: ", addr)
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)
