```
python3 -m serial.tools.list_ports
/dev/ttyAMA0        
1 ports found
```

`dtoverlay = pi3-disable-bt` rajouté dans /boot/config.txt

`enable_uart = 1` pas rajouté à /boot/config.txt

`console=serial0,115200` supprimé dans cmdline.txt

pour donner à l'utilisateur les privilèges sur le port série :

```
sudo usermod -a -G dialout,tty alexandrecuer
```

# voltage conversion

https://forum.raspberry-pi.fr/t/com-rs232-entre-rpi-3b-et-controleur-radio/7704

https://qastack.fr/electronics/110478/difference-between-uart-and-rs-232

http://raspberrypi.tomasgreno.cz/uart-to-rs-232.html

https://www.framboise314.fr/le-port-serie-du-raspberry-pi-3-pas-simple/

https://www.raspberrypi.org/forums/viewtopic.php?t=227262

# pyserial

https://github.com/pyserial/pyserial/issues/216

https://stackoverflow.com/questions/29557353/how-can-i-improve-pyserial-read-speed/56240817#56240817
