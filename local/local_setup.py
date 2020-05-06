wpa_supplicant_string = '''\
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1

network={{
	ssid="{0}"
	psk="{1}"
	scan_ssid=1
	key_mgmt=WPA-PSK
	priority=1
}}
'''


import os

# dir
dst_dir = input('Destination directory:')
dst_dir = os.path.expanduser(dst_dir)
print('\n* Destination set to ' + dst_dir)

# create 'ssh' file
os.chdir(dst_dir)
open('ssh', 'w').close()

# create 'wpa_supplicant' file
with open('wpa_supplicant.conf', 'w') as f:
	ssid = input('ssid: ')
	print('\n* SSID set to: ' + ssid)
	psk  = input('psk: ')
	print('\n* PSK set')
	f.write(wpa_supplicant_string.format(ssid, psk))