# Lightintensity_client.py
import RPi.GPIO as GPIO
import time
import socket
import os

host = '192.168.251.13'
port = 12341                  # The same port as used by the server
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((host,port))

#data = s.recv(1024).decode()
#data=str(data,'utf-8')

GPIO.setmode(GPIO.BCM)
resistorPin = 4

GPIO.setup(12,GPIO.OUT)

while True:
  GPIO.setup(resistorPin, GPIO.OUT)
  GPIO.output(resistorPin,GPIO.LOW)
  time.sleep(0.1)
  
  GPIO.setup(resistorPin,GPIO.IN)
  currentTime =time.time()
  diff=0
  
  while(GPIO.input(resistorPin)==GPIO.LOW):
    diff=time.time()-currentTime
    
    print(diff*1000)
    c=diff*1000
    s.send(bytes(f'{c}','utf-8'))
    #s.sendall(bytes((diff*1000), encoding='ascii'))

    data = 'resistorPin'
        #print('Does have the word metadata? Answer:', data)
    if (data == 0.017):
        print ("FAN on")
        GPIO.output(12,GPIO.HIGH)
        time.sleep(4)
    else:
        print ("FAN off")
        GPIO.output(12,GPIO.LOW)
        time.sleep(4)
    time.sleep(1)
GPIO.cleanup()
s.close()
