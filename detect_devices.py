import subprocess
import os


def call_nmap_on_lan(mask='26'):
    with open(os.devnull, 'w') as the_void:
        return subprocess.call(('nmap -sP -n 192.168.1.0/'+mask).split(' '), stdout=the_void)

def call_arp():
    return subprocess.check_output('arp -a'.split(' ')).decode()

def call_nmap_and_return_arp(mask = '26'):
    call_nmap_on_lan(mask=mask)
    return call_arp()

def get_ips_for_mac_addresses(mac_addresses):
    mac_ip_dict = {}
    devices = call_nmap_and_return_arp()
    for line in devices.split('\n'):
        words = line.split(' ')
        if len(words) > 3:
            for mac_address in mac_addresses:
                if( words[3].lower() == mac_address.lower()):
                    mac_ip_dict[words[3].lower()] = words[1].replace('(','').replace(')','')
    return  mac_ip_dict

def check_for_mac_addresses(mac_addresses):
    mac_ip_dict = get_ips_for_mac_addresses(mac_addresses)
    return any(mac_address.lower() in mac_ip_dict for mac_address in mac_addresses)

def check_for_mac_address(mac_address):
    check_for_mac_addresses([mac_address])

def get_ip_for_mac_address(mac_address):
    return get_ips_for_mac_addresses([mac_address]).get(mac_address.lower())

