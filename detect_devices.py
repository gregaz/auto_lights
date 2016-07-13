import subprocess


def check_for_mac_addresses(mac_addresses=[]):
    subprocess.call('nmap -sP -n 192.168.1.0/26'.split(' '))
    devices = subprocess.check_output('arp -a'.split(' ')).decode()
    for word in devices.split(' '):
        if any(word.lower() == mac_address.lower() for mac_address in mac_addresses):
            return True
    return False

def check_for_mac_address(mac_address):
    check_for_mac_addresses([mac_address])