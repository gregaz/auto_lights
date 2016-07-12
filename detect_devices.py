import subprocess


def check_for_mac_address(mac_address):
    subprocess.call('nmap -sP -n 192.168.1.0/26'.split(' '))
    devices = subprocess.check_output('arp -a'.split(' ')).decode()
    for word in devices.split(' '):
        if word.lower() == mac_address.lower():
            return True
    return False

