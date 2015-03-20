import socket
import sys
import Adafruit_BBIO.GPIO as GPIO
import time
 
HOST = ''
PORT = 8888
 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print 'Socket created'

GPIO.setup("P9_14", GPIO.OUT)
 
try:
    s.bind((HOST, PORT))
except socket.error as msg:
    print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
    sys.exit()
     
print 'Socket bind complete'
 
s.listen(10)
print 'Socket now listening'
 
while 1:
    conn, addr = s.accept()
    print 'Connected with ' + addr[0] + ':' + str(addr[1])
    GPIO.output("P9_14", GPIO.HIGH)
    time.sleep(0.1)
    GPIO.output("P9_14", GPIO.LOW)

     
s.close()
GPIO.cleanup()
