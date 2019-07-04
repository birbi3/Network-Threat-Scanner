def heavy_scan(network):
	"""runs and nmap scan and dumps output to a textfile
	Args:
		network (string): The network and subnet going to be scanned
	"""
	with open("config", "r") as config: 
		#reads a nmap command form the config file. This might not be here long. 
		scan = config.readline(0)
     	os.system(scan + network + " > scan-results.txt")

  
def results_data(host,mac,port):
	"""Data structure for all the results data.
	Args: 
		host (string): host ip for device data
		mac (string): mac address for device data
		port (list): all the ports associtated with the host

	Return: 
		resilts (dict): all the data in a dict for easier management
	"""
	results = {"hosts": host, 
	"mac": mac, 
	"port": port
		}
	
	return results

def parse_scan():
	"""prases output text file
	"""
	heavy_scan()
	with open('scan-results.txt', 'r') as results:
		data = []
		host = ""
		mac = ""
		flag = False
		for line in results:

			if "PORT" and "STATE"in line.strip():
				flag = True
				ports = []

			elif "MAC" and "Address:" in line.strip():
				mac = line.split(' ')[2]
				host_info = results_data(host,mac,ports)
				data.append(host_info)
				host_info = None
				
				flag = False
			
			elif socket.gethostname() in line.strip():
				break
			
			elif "Nmap scan report for " in line.strip():
				host = line.split(' ')[4]

			elif flag == True:
				ports.append(line)
				
			
	with open('results.json', 'w') as results:
		results.write(json.dumps(data, indent=4, sort_keys=True))







