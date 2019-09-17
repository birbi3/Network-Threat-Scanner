#This function is to 
def net_detect():
	"""determines what the network and subnet mask is. 
	Return:
		network (string): the network and subnet
	"""
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
	network = device_ip[0].get("addr")
	network = (".".join(network.split(".",3)[:3])) + ".0" 
	network += "/" + subnet
	return str(network)
  
#Credit for this https://stackoverflow.com/questions/17679887/python-check-whether-a-network-interface-is-up
#Check if interface has IP associated with it.
def is_interface_up(interface):
    addr = netifaces.ifaddresses(interface)
    return netifaces.AF_INET in addr



