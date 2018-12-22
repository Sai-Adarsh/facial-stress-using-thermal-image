import RPi.GPIO as GPIO
import time
import sys

flag=sys.argv[1]
count=len(sys.argv[1:])

'''
if count < 2:
    print "Argument not supplied"
    exit()
'''

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

if flag == "1":
    GPIO.setup(12,GPIO.OUT)
    GPIO.output(12,GPIO.HIGH)
    time.sleep(2)
    GPIO.output(12,GPIO.LOW)

if flag == "0":
    ct=0
    GPIO.setup(12,GPIO.OUT)
    while ct < 5:
        GPIO.output(12,GPIO.HIGH)
        time.sleep(0.2)
        GPIO.output(12,GPIO.LOW)
        time.sleep(0.2)
        ct = ct + 1

