#!/usr/bin/python3.5

from detect_devices import get_ip_for_mac_address
from config import pi_mac

print(get_ip_for_mac_address(pi_mac))