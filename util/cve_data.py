import requests
import re
import json

def data_nmap_handle(scan_data):

	scan_data = scan_data.split(" ")
	scan_data = [data.encode('ascii') for data in scan_data]
	scan_data = filter(None, scan_data)
	scan_data = [data.rstrip() for data in scan_data]

	scan_data = scan_data[3:]
	program_list = []
	version = ""
	for data in scan_data:
		if re.match(r'[a-z]+',data):
			program_list.append(data)
		else:
			version = data
	if not program_list:
		del program_list
	else:	
		for data in program_list:
			url = 'https://cve.circl.lu/api/search/' + data
			api = requests.get(url)
			response = api.json()
			if not response:
				continue
			for _r in response:
				if _r == version:
					print (data + version + "is vuln")

		


def main():
	with open('results.json') as json_file:
		data = json.load(json_file)
		for host in data:
			ports = host.get('port')
			data_nmap_handle(ports[0])
			#for port in ports:
				#data_nmap_handle(port)

main()