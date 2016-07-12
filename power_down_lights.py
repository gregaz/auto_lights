#!/usr/bin/python
from lifxlan import *

lifx = LifxLAN(1)
devices = lifx.get_lights()
bulb = devices[0]
bulb.set_power("off")