import wiringpi
import time

wiringpi.wiringPiSetup()
n=2
def test(pin):
    wiringpi.pinMode(pin,1)
    for i in range(n):
        a = wiringpi.digitalRead(pin)
        if a == 0:
            print("ouverture")
            wiringpi.digitalWrite(pin,1)
        if a == 1:
            print("fermeture")
            wiringpi.digitalWrite(pin,0)
        time.sleep(5)
test(0)
test(1)
test(7)
