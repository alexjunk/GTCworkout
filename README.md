On travaille avec un raspberry, pas avec un arduino. On n'est pas à la recherche de performances temps réelle.

http://gilles.thebault.free.fr/spip.php?article44

https://github.com/WiringPi/WiringPi-Python

https://github.com/alexandrecuer/tf_works/blob/master/BIOS/maquette/

Il faut avoir installé wiringPi

```
pip3 install wiringpi
```

# GTCworkout - pilotage des actionneurs d'un circuit de chauffage

## montage en mode mélange

![](images/montage_relays_V3V_mélange.jpeg)

[code](src/relay2.py)

```
wget https://raw.githubusercontent.com/alexjunk/GTCworkout/main/src/relay2.py
```

## cas d'une vanne TOR

### notations

On part du principe qu'on travaille avec une vanne tout ou rien (TOR) et non avec une vanne proportionnelle

Text = température extérieure

Tc = température de consigne de l'eau

Tdep = température de départ dans le circuit

pompe = 1 pour pompe en marche, 0 pour pompe arrêtée

V3V = 1 pour vanne 3 voies en position ouverte, 0 pour vanne 3 voies en position fermée

## algorithme

distribution | action
-- | --
passage de ON à OFF | V3V = 0 puis pompe = 0
passage de OFF à ON | V3V = 1 puis pompe = 1

Lorsqu'on ne chauffe pas, on peut maintenir l'activité de la pompe jusqu'à ce que la chaleur du circuit se soit dissipée. Mais ce n'est pas très utile en pratique.
distribution | monitoring | action
-- | -- | --
OFF | Tdep > 30 | pompe = 1
OFF | Text >=4 & Tdep <= 25 | pompe = 0 

Lorsqu'on ne chauffe pas et que le bâtiment n'est pas occupé, et s'il y a une vague de froid, on envoie de l'eau à 20°c pour maintenir le hors-gel
distribution | monitoring | action
-- | -- | -- 
OFF | Text < 4 | pompe = 1
OFF | Text < 4 & Tdep < 19 | V3V = 1
OFF | Text < 4 & Tdep > 21 | V3V = 0
