import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
dac = [8, 11, 7, 1, 0, 5, 12, 6]
comp = 14
troyka = 13
GPIO.setup(dac, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(comp, GPIO.IN)
def dec2bin(num):
    return [int(elem) for elem in bin(num)[2:].zfill(8)]
def adc():
    value = 128
    GPIO.output(dac, dec2bin(value))
    time.sleep(0.001)
    if GPIO.input(comp) == 1:
        value -= 128

    value += 64
    GPIO.output(dac, dec2bin(value))
    time.sleep(0.001)
    if GPIO.input(comp) == 1:
        value -= 64

    value += 32
    GPIO.output(dac, dec2bin(value))
    time.sleep(0.001)
    if GPIO.input(comp) == 1:
        value -= 32

    value += 16
    GPIO.output(dac, dec2bin(value))
    time.sleep(0.001)
    if GPIO.input(comp) == 1:
        value -= 16

    value += 8
    GPIO.output(dac, dec2bin(value))
    time.sleep(0.001)
    if GPIO.input(comp) == 1:
        value -= 8

    value += 4
    GPIO.output(dac, dec2bin(value))
    time.sleep(0.001)
    if GPIO.input(comp) == 1:
        value -= 4

    value += 2
    GPIO.output(dac, dec2bin(value))
    time.sleep(0.001)
    if GPIO.input(comp) == 1:
        value -= 2

    value += 1
    GPIO.output(dac, dec2bin(value))
    time.sleep(0.001)
    if GPIO.input(comp) == 1:
        value -= 1
    return value
try:
    while True:
        print(adc() * 3.3 / 256)
finally:
    GPIO.output(dac, 0)
    GPIO.output(troyka, 0)
    GPIO.cleanup()