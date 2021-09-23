import wiringpi
import time

wiringpi.wiringPiSetup()

"""
work in progress
pilotage d'une vanne 3 voie
r2 - pin+1 : relais de commande on/off avec timer
r1 - pin : relais pour le choix du sens (ouverture/fermeture)
"""
# course en millisecondes 
# course pour une vanne SAX31 de chez Siemens
course = 150000
# sens
ouvre = 0
ferme = 1

def initv3v(pin):
    """
    configure les relais pin et pin+1 en sortie
    sortie = 1 / entrée = 0
    """
    wiringpi.pinMode(pin,1)
    wiringpi.pinMode(pin+1,1)

def v3v(pin, sens, percent):
    """
    définit le sens de fonctionnement
    manoeuvre la vanne jusqu'à un certain pourcentage
    """
    wiringpi.digitalWrite(pin, 0)
    wiringpi.digitalWrite(pin+1, 0)
    wiringpi.digitalWrite(pin, sens)
    wiringpi.digitalWrite(pin+1, 1)
    wiringpi.delay(percent*course//100)
    wiringpi.digitalWrite(pin+1, 0)
    wiringpi.digitalWrite(pin, 0)

initv3v(0)
# on ferme la vanne complètement
v3v(0,ferme,100)
# on ouvre la vanne à 40%
v3v(0,ouvre,40)
