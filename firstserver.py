import socket
import os
import time
HEADER = 64
SIZE = 1024
PORT = 6060
su = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
su.connect(("8.8.8.8", 80))
SERVER = su.getsockname()[0]
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "DISCONNECT!"

def main():
    print("[STARTING] Server is starting.")
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(ADDR)
    server.listen()
    print("[LISTENING] Server is listening.")
    connected = True
    while connected:
        start_time = time.process_time()
        conn, addr = server.accept()
        print(f"[NEW CONNECTION] {addr} connected")
        #SIZE = int(conn.recv(1024).decode(FORMAT))
        #print(SIZE)
        #print(f"[FurtherConnection ] {addr} connected")
        filename = conn.recv(SIZE).decode(FORMAT)
        print(f"[RECV] Receiving the filename.")
        file = open(filename, "w")
        conn.send("Filename received.".encode(FORMAT))
        print(f"[RECV] Receiving the file data.")
        while True:
            data = conn.recv(1024).decode(FORMAT)
            conn.send("File data being received".encode(FORMAT))
            if not data:
               break
            file.write(data)
        print(f"Completed Download of", filename)
        file.close()
        conn.close()
        print(f"[DISCONNECTED] {addr} disconnected")
        end_time = time.process_time()
        print(f"CPU time used: {end_time - start_time} seconds")
if __name__ == "__main__":
    main()

