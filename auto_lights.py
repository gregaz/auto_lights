#!/usr/bin/python3.4

from detect_devices import check_for_mac_addresses
from status import Status
import time, subprocess, datetime, logging
from config import *


logging.basicConfig(filename=log_file, level=logging.DEBUG,
                    format='%(asctime)s %(process)d %(levelname)s %(name)s %(message)s')
logger=logging.getLogger(__name__)

logger.log(logging.DEBUG, 'Started script')

for MAC_ADDRESS in phone_macs:
    logger.log(logging.DEBUG, 'Registered mac address as phone: ' + MAC_ADDRESS)

status = Status()

while True:
    try:
        time.sleep(15)

        if datetime.datetime.now().hour > wake_time:
            if check_for_mac_addresses(phone_macs):
                if status.is_away():
                    logger.log(logging.DEBUG, 'Lights powered up and set to home mode')
                    subprocess.call(['./power_lights.py', 'on'])
                    status.set_home()
                elif status.is_leaving():
                    logger.log(logging.DEBUG, 'Returned before full shutoff delay time, set back to home mode')
                    status.set_home()
            else:
                if status.is_home():
                    logger.log(logging.DEBUG, 'Initiated leaving protocol, countdown to shutdown started')
                    status.set_leaving()
                elif status.is_leaving() and abs((status.departure_time - datetime.datetime.now()).total_seconds()) > shutoff_delay:
                    logger.log(logging.DEBUG, 'Lights powered down and went to away mode')
                    subprocess.call(['./power_lights.py', 'off'])
                    status.set_away()

    except Exception as e:
        logger.error(e)
