import socket
import os
import struct
HEADER = 64
PORT = 5050
ListofWorkers = ["worker1", "worker2"]
SERVER = ListofWorkers[0]
DISCONNECT_MESSAGE = "DISCONNECT!"
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))

for worker in ListofWorkers:
   SERVER = worker
   ADDR = (SERVER, PORT)
   client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   client.connect(ADDR)
   send("Hello World!")




