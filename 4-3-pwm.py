import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(26, GPIO.OUT)
n = 10
p = GPIO.PWM(26, 1000)
p.start(0)
try:
    while True:
        a=input()
        try:
            A=int(a)
            if 0 <= A <= 100:
                p.ChangeDutyCycle(A)
                print(3.3 * A/100)
            else:
                print("Номер должен быть от 0 до 100")
        except ValueError:
            print("Плохо")
finally:
    p.stop()
    GPIO.output(26, 0)
    GPIO.cleanup()