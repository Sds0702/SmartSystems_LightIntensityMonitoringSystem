# Lightintensity_server.py
import socket
import time

def check():
    with open('received_file') as f:
        datafile = f.readlines()
    found = False  
    for line in datafile:
        #next line: change to the word you are looking for
        if 'pulseaudio' in line:
            return True
    return False  

host = '192.168.251.13'        # Symbolic name meaning all available interfaces
port = 12341     # Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(6)
conn, addr = s.accept()
lightinfo = conn.recv(1024).decode()
print ('lightinfo =', lightinfo) 
light = float(lightinfo.split(' ')[0])
print ('light =', light, '\n')
if (light > 0.017):
    print ('larger\n') 
    conn.sendall(b'larger')
else:
    print ('lower \n') 
    conn.sendall(b'lower ') 
    #both with 6 characters to avoid issues with recv on the other side active = s.recv(6)
time.sleep(100)
conn.close()
s.close()

