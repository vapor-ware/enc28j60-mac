from smbus import SMBus
import os
import time

# 24AA02E48 EEPROM Address
address = 0x50

# Open channel 1
bus = SMBus(1)

# Read out the 6 byte EUI-48 Node address starting at memory location 0xFA
mac = bus.read_i2c_block_data(address, 0xFA, 6)

# Print out the MAC address
mac_addr = '{}'.format(':'.join("%0.2X" % x for x in mac))
#print 'Assigning MAC Address to eth0' + mac_addr

# The following 5 lines were done after everthing was up and running
# at that point dhcp already assiged an ip based on the generated MAC address
# The unit file in /lib/systemd/system/enc28j60_mac.cervice
#
# [Unit]
# Description=Read MAC out of EEPROM
# After=multi-user.target
#
# [Service]
# Type=idle
# ExecStart=/usr/bin/python /home/pi/Set_ENC28J60_MAC.py /home/pi/Set_ENC28J60_MAC.log 2>&1
#
# [Install]
# WantedBy=multi-user.target
#os.system('ifconfig eth0 down')
#time.sleep(0.500)
#os.system('sudo ifconfig eth0 hw ether 80:1F:12:48:A7:E0') 
#os.system('ifconfig eth0 hw ether ' + mac_addr)
#os.system('ifconfig eth0 up')

# Changed up the unit file to run the script before eth0 is up with the following unit file
# The unit file in /lib/systemd/system/enc28j60_mac.cervice
#
# [Unit]
# Description=Read MAC out of EEPROM
# Wants=network-pre.target
# Before=network-pre.target
# BindTo=sys-subsystem-net-devices-eth0.device 
# After=sys-subsystem-net-devices-eth0.device
#
# [Service]
# Type=oneshot
# ExecStart=/usr/bin/python /home/pi/Set_ENC28J60_MAC.py /home/pi/Set_ENC28J60_MAC.log 2>&1
#
# [Install]
# WantedBy=multi-user.target

os.system('/sbin/ip link set dev eth0 down')
os.system('/sbin/ip link set dev eth0 address ' + mac_addr)
os.system('/sbin/ip link set dev eth0 up')
