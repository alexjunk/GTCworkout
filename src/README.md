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
