#!/usr/bin/python3.4

from detect_devices import get_ip_for_mac_address

with open('/home/gregory/RaspberryPi/mac_address.txt') as f:
    MAC_ADDRESS = f.readlines()

print(get_ip_for_mac_address(MAC_ADDRESS[0].replace('\n','')))