#!/usr/bin/python
from lifxlan import *
from config import light_labels
import sys

lifx = LifxLAN()
devices = lifx.get_lights()
bulbs_to_power_on = [bulb for bulb in devices if bulb.get_label() in light_labels]
for bulb in bulbs_to_power_on:
    bulb.set_power(sys.argv[1])