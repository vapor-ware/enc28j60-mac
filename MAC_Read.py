from smbus import SMBus

# 24AA02E48 EEPROM Address
address = 0x50

# Open channel 1
bus = SMBus(1)

# Read out the 6 byte EUI-48 Node address starting at memory location 0xFA
mac = bus.read_i2c_block_data(address, 0xFA, 6)

# Print out the MAC address
print 'MAC Address ' + '{}'.format(':'.join("%0.2X" % x for x in mac))
