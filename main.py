#!/usr/bin/env python

#source modules
from util.cve_data import *
from util.net_detect import *
from util.nmap_scan import *
#standard library
import os
import json
import socket

#open source
import netifaces
from netaddr import *

def main():
	
	if os.geteuid() != 0:
		exit("This program requrires root")
	network = net_detect()
	


if __name__ == "__main__":
	main()