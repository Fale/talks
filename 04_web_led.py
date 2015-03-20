from flask import Flask
import Adafruit_BBIO.GPIO as GPIO

app = Flask(__name__)

@app.route('/on')
def on():
    GPIO.setup("P9_14", GPIO.OUT)
    GPIO.output("P9_14", GPIO.HIGH)
    return 'LED ON!'

@app.route('/off')
def off():
    GPIO.setup("P9_14", GPIO.OUT)
    GPIO.output("P9_14", GPIO.LOW)
    return 'LED OFF!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
