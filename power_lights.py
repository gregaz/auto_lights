from lifxlan import *
from config import light_labels_to_power_on, light_labels_to_power_off
import sys


def power_lights(on_or_off):
    lifx = LifxLAN()
    devices = lifx.get_lights()

    if (on_or_off == 'on'):
        light_labels = light_labels_to_power_on
    else:
        light_labels = light_labels_to_power_off

    bulbs_to_power = [bulb for bulb in devices if bulb.get_label() in light_labels]
    for bulb in bulbs_to_power:
        bulb.set_power(on_or_off)