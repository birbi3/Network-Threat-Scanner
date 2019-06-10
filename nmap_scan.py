import os

#TODO get example nmap output file for prasing. 

#Will run the nmap scan in the config file 
def heavy_scan(network):
	with open("config", "r") as config: 
		scan = config.readline()
     os.system(scan + network + " > scan-results.txt")
     with open("scan-results.txt", "r") as scan_results:
         for stuff in scan_results:


