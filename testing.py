import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
relay_pin = 17
GPIO.setup(relay_pin, GPIO.OUT)
GPIO.setwarnings(False)

while True:
    GPIO.output(relay_pin, 1)
    time.sleep(3)
    GPIO.output(relay_pin, 0)
    time.sleep(3)