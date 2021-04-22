import RPi.GPIO as GPIO
from time import sleep
pin=2
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(2,GPIO.OUT,initial=GPIO.HIGH)
GPIO.setup(3,GPIO.OUT,initial=GPIO.HIGH)
GPIO.setup(4,GPIO.OUT,initial=GPIO.HIGH)
GPIO.setup(17,GPIO.OUT,initial=GPIO.HIGH)
GPIO.setup(27,GPIO.OUT,initial=GPIO.HIGH)
GPIO.setup(22,GPIO.OUT,initial=GPIO.HIGH)
GPIO.setup(10,GPIO.OUT,initial=GPIO.HIGH)
