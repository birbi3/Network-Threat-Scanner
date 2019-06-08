#!/usr/bin/env python

#open source
import pyping, netifaces
from netaddr import *

##TODO assure that network address and broadcast address are not pinged.

#This function is to determine what the network and subnet mask is. 
def net_detect():
	#fetches interfaces
	net_info = netifaces.interfaces()
	for device in net_info:
		current = is_interface_up(device)
		if device == "lo": continue 
		if "tun" in device: continue 
		if current == True:
			#creates a list of information about interface associated with an IP address.
			device_ip = netifaces.ifaddresses(device)[netifaces.AF_INET]
			break
	subnet = device_ip[0].get("netmask")
	subnet = str(IPAddress(subnet).netmask_bits())
	network = clean_network(device_ip[0].get("addr"))
	network += "/" + subnet
	return str(network)
  
#Credit for this https://stackoverflow.com/questions/17679887/python-check-whether-a-network-interface-is-up
#Check if interface has IP associated with it.
def is_interface_up(interface):
    addr = netifaces.ifaddresses(interface)
    return netifaces.AF_INET in addr

#this function just cleans up the the IP address associated with interface for network address.
def clean_network(addy):
	new_addy = ""
	count = 0

	for i in addy:
		if i == ".": count += 1
		new_addy += i
		if count == 3: break
	new_addy += "0"
	return new_addy

def main():
	network = net_detect()
	ping_sweep(network)

if __name__ == "__main__":
	main()
