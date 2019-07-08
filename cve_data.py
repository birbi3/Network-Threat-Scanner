import requests
import json

def data_nmap_handle(scan_data):

	scan_data = scan_data.split(" ")
	scan_data = [data.encode('ascii') for data in scan_data]
	scan_data = filter(None, scan_data)
	scan_data = [data.rstrip() for data in scan_data]
	scan_data = scan_data[3:]
	for data in scan_data:
		url = 'https://cve.circl.lu/api/search/' + data
		api = requests.get(url)
		response = api.json()
		if not response:
			continue
		else:
			print(response)

		


def main():
	with open('results.json') as json_file:
		data = json.load(json_file)
		for host in data:
			ports = host.get('port')
			data_nmap_handle(ports[0])
			#for port in ports:
				#data_nmap_handle(port)

main()