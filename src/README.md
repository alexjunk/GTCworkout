# mosquitto

pour tester le client mosquitto en ligne de commande :
```
sudo apt-get install mosquitto-clients
```
on peut ensuite souscrire au topic emon :
```
mosquitto_sub -v -u 'emonpi' -P 'emonpimqtt2016' -t 'emon/#'
```
pour publier :
```
mosquitto_pub -t 'emon/test/t3' -m 12
```

# uart

J'ai à un moment pensé que pour utiliser BIOS avec son récepteur radio branché sur le port USB, et pouvoir commander des relais sans avoir d'interférences avec le récpeteur enless, il convenait de désactiver l'uart qui est sur ttyAMA0

Pour y parvenir :
```
sudo raspi-config
```
ou alors mettre `enable_uart = 0` dans `/boot/config.txt`

On vérifie que l'uart n'est plus activé par la commande `python3 -m serial.tools.list_ports`

on doit avoir comme retour :

```
/dev/ttyUSB0
1 port found
```

toutefois, le problème semble plutôt venir de la carte relais (photocoupleur). En éloignant la carte relais du récepteur, on n'a pas d'interférences
