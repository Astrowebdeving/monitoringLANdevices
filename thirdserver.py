import socket
import threading
import struct
import os

HEADER = 64
PORT = 5050
su = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
su.connect(("8.8.8.8", 80))
SERVER = su.getsockname()[0]
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "DISCONNECT!"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")

    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                connected = False

            print(f"[{addr}] {msg}")
            conn.send("Message received".encode(FORMAT))
            os.system("python3 newtest.py")
            os.system("python3 firstclient.py")
            print("hello????")
    conn.close()

def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}.")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target = handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")

print("[STARTING] server is starting...")
start()