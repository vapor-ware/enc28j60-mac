# PI 3 Module ENC28J60 Static MAC Address at Bootup

The ENC28j60 ethernet controller on the security and carousel controllers do not have a static MAC address assigned during bootup which 
causes the driver to assign a random MAC at bootup.  To fix this problem a external EEPROM which contains a pre-programmed MAC address 
is attached to the module I2C port.  The idea is at bootup, the PI 3 runs a Python script which will read out the MAC address from the 
attached EEPROM and set it to the eth0 interface.

There are two files to accomplish this, the actual Python script and a unit file which runs the script as a custom service during bootup.

Copy file enc28j60_mac.service to:
```
/lib/systemd/system
'''

Copy file Set_ENC28J60_MAC.py to:
```
/home/pi
```

Set the file permissions:
```
sudo chmod 644 /lib/systemd/system/enc28j60_mac.service
```

Enable the service:
```
sudo systemctl daemon-reload
sudo systemctl enable enc28j60_mac.service
```

Copy the file MAC_Read.py to:
```
/home/pi
```
We will use that script later to verify the MAC address was assigned to eth0.

Reboot:
```
sudo /sbin/reboot
```

Double check if MAC stored in the EEPROM was set to eth0:
```
ifconfig
sudo python MAC_Read.py
```

Hopefully what was return buy MAC_read.py matches what is shown for eth0 in ifconfig
