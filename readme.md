## Auto Lights ##
A quick python script that will automatically turn your LIFX lightbulb on when you get home and turn it off when you leave.

### Quick Start Guide ###
1. Clone this repository onto your raspberry pi.
```
git clone https://github.com/gregaz/auto_lights.git
```

2. Install lifxlan:
```
sudo pip3 install lifxlan
```

2. Complete the required fields in config.py. Example:
```python
#required
light_labels_to_power_off = ['living_room', 'dining_room']
light_labels_to_power_on = ['living_room']
phone_macs = ['2E-D0-10-48-44-91', '0B-53-FD-DF-8A-62' ]
```

3. Change permissions on the script in order to run it:
```
chmod 777 auto_lights.py
```

4. Run the auto_lights.py script:
```
nohup ./auto_lights.py &
```

### How it works ###
This script continuosly polls your home wifi network for your phone's MAC address. If it finds your phone connected/disconnected to your home network, it knows that you are home/away and sends a command to your LIFX lightbulbs to turn on/off.

### Testing and Issues ###
I have had this running on my raspberry PI zero for two phones and two LIFX bulbs for about a year without any major issues. One small issue we've noticed is that when my iPhone is low on batteries it will disconnect itself from the network to conserve power which will cause our lights to turn off. YMMV depending on what type of phone you have.

### Utility Scripts ###
Some scripts that can be useful:
1. get_ip_for_mac_address(mac_address) - useful for finding your raspberry pi's ip address on your lan when you know it's MAC address.
2. check_for_mac_addresses(mac_addresses) - useful to determine if certain devices are on your lan network.