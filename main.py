import net_detect, nmap_scan


def main():
	
	if os.geteuid() != 0:
		exit("This program requrires root")
	network = net_detect()
	


if __name__ == "__main__":
	main()