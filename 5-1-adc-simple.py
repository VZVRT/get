import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
dac = [8,11,7,1,0,5,12,6]
comp = 14
troyka = 13
GPIO.setup(dac, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(comp, GPIO.IN)
def dec2bin(num):
    return [int(elem) for elem in bin(num)[2:].zfill(8)]
def adc():
    for i in range(256):
        dac_val = dec2bin(i)
        GPIO.output(dac, dac_val)
        comp_val = GPIO.input(comp)
        time.sleep(0.001)
        if comp_val == 1:
            return i
    return 255
try:
    while True:
        print(adc()*3.3/256)
finally:
    GPIO.output(dac, 0)
    GPIO.output(troyka, 0)
    GPIO.cleanup()