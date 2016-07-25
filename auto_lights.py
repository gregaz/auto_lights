#!/usr/bin/python3.4

from detect_devices import check_for_mac_addresses
from status import Status
import time, subprocess, datetime, logging


logging.basicConfig(filename='/tmp/auto_lights.log', level=logging.DEBUG,
                    format='%(asctime)s %(process)d %(levelname)s %(name)s %(message)s')
logger=logging.getLogger(__name__)

logger.log(logging.DEBUG, 'Started script')

with open('/home/pi/mac_addresses.txt') as f:
    MAC_ADDRESSES = f.readlines()

MAC_ADDRESSES = [MAC_ADDRESS.replace('\n','') for MAC_ADDRESS in MAC_ADDRESSES]

for MAC_ADDRESS in MAC_ADDRESSES:
    logger.log(logging.DEBUG, 'Registered mac address as phone: ' + MAC_ADDRESS)

status = Status()

while True:
    try:
        time.sleep(15)

        if datetime.datetime.now().hour > 9:
            if check_for_mac_addresses(MAC_ADDRESSES):
                if status.isAway():
                    logger.log(logging.DEBUG, 'Lights powered up and set to home mode')
                    subprocess.call(['./power_up_lights.py'])
                    status.setHome()
            else:
                if status.isHome():
                    logger.log(logging.DEBUG, 'Lights powered down and went to away mode')
                    subprocess.call(['./power_down_lights.py'])
                    status.setAway()
    except Exception as e:
        logger.error(e)
