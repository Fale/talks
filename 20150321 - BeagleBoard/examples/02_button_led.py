import Adafruit_BBIO.GPIO as GPIO
import time
 
GPIO.setup("P9_14", GPIO.OUT)
GPIO.setup("P9_42", GPIO.IN)

while True:
    if GPIO.input("P9_42"):
        print("HIGH")
        GPIO.output("P9_14", GPIO.LOW)
    else:
        print("LOW")
        GPIO.output("P9_14", GPIO.HIGH)

GPIO.cleanup()
