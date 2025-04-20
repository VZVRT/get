import RPi.GPIO as GPIO
dac = [8, 11, 7, 1, 0, 5, 12, 6]
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)
def decimal2binary(value):
    return [int(bit) for bit in bin(value)[2:].zfill(8)]
try:
    while True:
        number = input("0-255:")
        try:
            num = int(number)
            if 0 <= num <= 255:
                GPIO.output(dac, decimal2binary(num))
                v = float(num) / 256 * 3.3
                print(v)
            else:
                if num<0:
                    print("Отрицательное число")
                else:
                    print("Слишком много для этого ЦАП")
        except Exception:
            try:
                num_float = float(number)
            except ValueError:
                if number=="q":
                    break
                print("Не число")
                continue
            print("Не целое")
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()