import wiringpi

wiringpi.wiringPiSetup()

"""
code pour prétests en chaufferie afin de connecter la vanne dans le bon sens
status : work in progress
pilotage d'une vanne 3 voies
r2 - pin+1 : relais de commande on/off avec timer
r1 - pin : relais pour le choix du sens (ouverture/fermeture)
"""
# course en millisecondes 
# course pour une vanne SAX31 de chez Siemens
course = 150000
# sens
# qd action vaut 1, on chauffe, qd action vaut 0, on coupe le chauffage
ouvre = 1
ferme = 0

def initv3v(pin):
    """
    configure les relais pin et pin+1 en sortie
    sortie = 1 / entrée = 0
    """
    wiringpi.pinMode(pin,1)
    wiringpi.pinMode(pin+1,1)

import click
@click.command()
@click.option('--pin', type=int, prompt='numéro du relais')
@click.option('--sens', type=int, prompt='sens/action : 1=chauffage 0=pas de chauffage')
@click.option('--percent', type=int, prompt='% de la course à appliquer')
def v3v(pin, sens, percent):
    """
    définit le sens de fonctionnement
    manoeuvre la vanne jusqu'à un certain pourcentage
    """
    initv3v(pin)
    wiringpi.digitalWrite(pin, 0)
    wiringpi.digitalWrite(pin+1, 0)
    wiringpi.digitalWrite(pin, sens)
    wiringpi.digitalWrite(pin+1, 1)
    wiringpi.delay(percent*course//100)
    wiringpi.digitalWrite(pin+1, 0)
    wiringpi.digitalWrite(pin, 0)

if __name__ == "__main__":
    v3v()
