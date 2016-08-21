#!/usr/bin/python
from lifxlan import *
from config import light_labels_to_power_on, light_labels_to_power_off
import sys

lifx = LifxLAN()
devices = lifx.get_lights()

if (sys.argv[1] == 'on'):
    light_labels = light_labels_to_power_on
else:
    light_labels = light_labels_to_power_off

bulbs_to_power = [bulb for bulb in devices if bulb.get_label() in light_labels]
for bulb in bulbs_to_power:
    bulb.set_power(sys.argv[1])