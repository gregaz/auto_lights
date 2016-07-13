#!/usr/bin/python3.4

from detect_devices import check_for_mac_address
from status import Status
import time, subprocess, datetime, logging


logging.basicConfig(filename='/tmp/auto_lights.log', level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s %(name)s %(message)s')
logger=logging.getLogger(__name__)

MAC_ADDRESS = 'your mac address here'

status = Status()

while True:
    try:
        time.sleep(30)

        if check_for_mac_address(MAC_ADDRESS) and datetime.datetime.now().hour > 9:
            if status.isAway():
                logger.log(logging.DEBUG, 'Lights powered up and set to home mode')
                subprocess.call(['./power_up_lights.py'])
                status.setHome()
        else:
            if status.isHome():
                logger.log(logging.DEBUG, 'Went to away mode')
                status.setAway()
    except Exception as e:
        logger.error(e)
