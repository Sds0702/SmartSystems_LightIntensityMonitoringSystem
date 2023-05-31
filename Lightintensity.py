import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
resistorPin = 4

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
    time.sleep(1)

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

