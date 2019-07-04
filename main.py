#!/usr/bin/env python

#source modules
import net_detect, nmap_scan
#standard library
import os
import json
import socket

#open source
import pyping, netifaces
from netaddr import *

def main():
	
	if os.geteuid() != 0:
		exit("This program requrires root")
	network = net_detect()
	


if __name__ == "__main__":
	main()