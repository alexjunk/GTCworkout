On travaille avec un raspberry, pas avec un arduino. 

On n'est pas à la recherche de performances temps réel.

https://www.circuits.dk/everything-about-raspberry-gpio/

http://gilles.thebault.free.fr/spip.php?article44

https://github.com/WiringPi/WiringPi-Python

Il faut avoir installé wiringPi

```
pip3 install wiringpi
```

# pilotage des actionneurs d'un circuit de chauffage

## montage d'une vanne en mode mélange

![](images/montage_relays_V3V_mélange.jpeg)

[code](src/relay2.py)

```
wget https://raw.githubusercontent.com/alexjunk/GTCworkout/main/src/relay2.py
```
## des bidouilleurs le font

http://sarakha63-domotique.fr/jeedom-domotiser-une-vanne-3-voies/


# produits radio

## jeelab

https://jeelabs.org/ avec un magasin en ligne : https://www.digitalsmarties.net/

the library : https://github.com/jeelabs/jeelib

la doc : https://jeelabs.org/pub/docs/jeelib/files.html

## logiciel gqrx

https://github.com/gqrx-sdr/gqrx , exploitant des récepteurs qu'on peut connecter au port usb du PC, cf https://www.sdrplay.com/

https://gqrx.dk/supported-hardware#fcd

## rpitx

utilisant le GPIO du raspberry comme antenne : https://github.com/F5OEO/rpitx

What is a band pass filter and why do I need it to use rpitx with an antenna? https://groups.io/g/rpitx/topic/what_is_a_band_pass_filter/29595643?p=

doc : https://www.rtl-sdr.com/wp-content/uploads/2016/12/ASK_erhard_e_tutorial.pdf?ffccfa&ffccfa


# reverse engineering 

## of a davis meteo station

http://madscientistlabs.blogspot.com/search?q=davis

## d'un thermostat de chaudière pour maison individuelle

https://hackingathome.com/2017/02/07/danfoss-wireless-thermostat-hacking-part-two/



# PID - contrôle temps réel

https://github.com/imax9000/Arduino-PID-Library

http://brettbeauregard.com/blog/2011/04/improving-the-beginners-pid-introduction/

https://www.rocketscream.com/blog/

https://www.abcclim.net/regulation-p-pi-pid.html

http://www.ferdinandpiette.com/blog/2011/08/implementer-un-pid-sans-faire-de-calculs/

[doc sur les régulateurs P, PI et PID](regulateurs_standards.pdf)

# culture G

[vers la maison passive](https://trystanlea.org.uk/)


