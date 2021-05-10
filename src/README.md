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
