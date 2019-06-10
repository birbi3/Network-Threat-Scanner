import os

#Will scan every port and parse the data 
def heavy_scan(network):
     os.system("nmap -sU -sT -p0-65535 -sV " + network + " > scan-results.txt")
     with open("scan-results.txt", "r") as scan_results:
         for stuff in scan_results:

#Will scan all udp ports   
def udp_scan(network):
     os.system("nmap -sU -p0-65535 -sV " + network + " > scan-results.txt")
     with open("scan-results.txt", "r") as scan_results:
         for stuff in scan_results:

#Will scan all tcp ports
def tcp_scan(network):
     os.system("nmap -sU -sT -p0-65535 -sV " + network + " > scan-results.txt")
     with open("scan-results.txt", "r") as scan_results:
         for stuff in scan_results:     	

#Will do a normal scan
def tcp_scan(network):
     os.system("nmap -sV " + network + " > scan-results.txt")
     with open("scan-results.txt", "r") as scan_results:
         for stuff in scan_results:     	


             

n_of_maps("10.0.0.0/24")     
