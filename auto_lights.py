from detect_devices import check_for_mac_address
import time, subprocess, datetime

MAC_ADDRESS = 'MAC ADDRESS OF YOUR PHONE HERE'

while True:
    time.sleep(30)

    if check_for_mac_address(MAC_ADDRESS) and datetime.datetime.now().hour > 9:
        subprocess.call(['./power_up_lights.py'])