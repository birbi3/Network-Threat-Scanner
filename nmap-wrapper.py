import os


def n_of_maps(network):
     os.system("nmap -sU -sT -p0-65535 -sV " + network + " > scan-results.txt")
     with (open "scan-results.txt" as scan_results):
         for stuff in scan_results:
             

n_of_maps("192.168.43.0/24")     
