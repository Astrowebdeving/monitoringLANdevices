import socket
import subprocess
import os
from time import process_time
HEADER = 64
PORT = 6060
SIZE = 1024
#namedebug = process_time()
contentfiletest = subprocess.check_output("ip=$(hostname -I | awk '{print $1}')\n cat /etc/hosts | grep $ip | awk '{print $2}'", shell=True, text=True)
#namedebugstop = process_time()
#print("Time elapsed:", namedebugstop-namedebug)
#filey1 = open("debugfile1.txt", "w")
#filey1.write(namedebugstop-namedebug)
#filey1.close()
ListofWorkers = ["manager"]
SERVER = ListofWorkers[0]
DISCONNECT_MESSAGE = "DISCONNECT!"
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
#seconddebug = process_time()
filelist = [f"updatedmemoryram_{contentfiletest.strip()}.csv", f"updatedstorage_{contentfiletest.strip()}.csv", f"updatedstorage3_{contentfiletest.strip()}.csv", f"allinfile_{contentfiletest.strip()}.txt", "test-100M.csv"]
#seconddebugstop = process_time()
#print("time elapsed:", seconddebugstop-seconddebug)
#filey2 = open("debugfile2.txt", "w")
#filey2.write(seconddebugstop-seconddebug)
#filey2.close()
def main(filename):
    #SIZE = os.path.getsize(filename)
    print(filename)
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(ADDR)
    file = open(f"{filename}", "r")
    print(file)
    #client.send(f"{SIZE}".encode(FORMAT))
    #msg = client.recv(SIZE).decode(FORMAT)
    #print(f"[SERVER]: {msg}")
    client.send(f"{filename}".encode(FORMAT))
    msg = client.recv(SIZE).decode(FORMAT)
    print(f"[SERVER]: {msg}")
    data = file.read(1024)
    while (data):
        client.send(data.encode(FORMAT))
        msg = client.recv(SIZE).decode(FORMAT)
        data = file.read(1024)
    print(f"[SERVER]:{msg}")
    file.close()
    client.close()

#for file_name in filelist:
#    msg = f"FILENAME:{file_name}"
#    print(f"[CLIENT] Sending file name: {file_name}")
#    client.send(msg.encode(FORMAT))
print(filelist)
if __name__ == "__main__":
    for filename in filelist:
        main(filename)
