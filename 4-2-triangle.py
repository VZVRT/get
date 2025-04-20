import RPi.GPIO as GPIO
import time
dac = [8,11,7,1,0,5,12,6]
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)
def dec2bin(value):
    return [int(bit) for bit in bin(value)[2:].zfill(8)]
num=0
fl=0
try:
    per=float(input('per:'))
    while True:
        GPIO.output(dac, dec2bin(num))
        if fl:
            num-=1
        else:
            num+=1
        if num==254:
            fl=1
        if num==0:
            fl=0
        time.sleep(per/512)
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()