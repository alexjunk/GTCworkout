import wiringpi
import time

wiringpi.wiringPiSetup()

n=1
def test(pin):
    wiringpi.pinMode(pin,1)
    for i in range(n):
        a = wiringpi.digitalRead(pin)
        if a == 0:
            print("passage en position NO")
            wiringpi.digitalWrite(pin,1)
        if a == 1:
            print("passage en position NC")
            wiringpi.digitalWrite(pin,0)

"""
work in progress
pilotage d'une vanne 3 voie
r2 - pin+1 : relais de commande on/off avec timer
r1 - pin : relais pour le choix du sens (ouverture/fermeture)
"""
# course en millisecondes 
# cas d'une vanne de test achetée sur amazon HDQ-DN20
# cf https://www.amazon.fr/vanne-voies-motoris%C3%A9e-electrovanne-bille/dp/B07GCGSPVJ/ref=sr_1_5?keywords=vanne%2B3%2Bvoies%2Bmotoris%C3%A9e&qid=1582276603&sr=8-5&th=1
course = 15000

def readv3v(pin):
    """
    lit les valeurs des relais pour info
    """
    r1 = wiringpi.digitalRead(pin)
    r2 = wiringpi.digitalRead(pin+1)
    print("relais {} : {}".format(pin,r1))
    print("relais {} : {}".format(pin+1,r2))

def initv3v(pin):
    """
    configure les relais pin et pin+1 en sortie
    sortie = 1 / entrée = 0
    """
    wiringpi.pinMode(pin,1)
    wiringpi.pinMode(pin+1,1)

def v3v(pin,sens,percent):
    """
    sens = 0 : fermerture
    sens = 1 : ouverture
    """
    wiringpi.digitalWrite(pin,sens)
    wiringpi.digitalWrite(pin+1,0)
    wiringpi.delay(percent*course//100)
    wiringpi.digitalWrite(pin+1,1)

initv3v(0)
#readv3v(0)

# on ouvre totalement la vanne et on a la ferme de 40 %
v3v(0,1,100)
v3v(0,0,40)

# on ferme totalement la vanne et on l'ouvre de 50%
"""
v3v(0,0,100)
v3v(0,1,50)
"""
