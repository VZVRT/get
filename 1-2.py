import RPi.GRIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(20, GPIO.OUT)
GPIO.setup(25, GPIO.IN)
t=GPIO.input(25)
GPIO.output(20,t)