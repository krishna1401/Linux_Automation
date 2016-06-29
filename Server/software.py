#!/usr/bin/python

from os import system
from commands import getstatusoutput
from time import sleep


def software(client) :
	client.send("dialog --inputbox \" Enter Software Name : \" 10 30")
	software = client.recv(1024)	
	client.send("dialog --menu \"Software List\" 30 50 3  1 \"Installation\" 2 \"Un-installation\" 3 \"Information\"")
	choice = client.recv(5)

	if choice == "1" :
		temp = getstatusoutput("yum install " + software + " -y")
		if temp[0] != 0 :
			client.send("recieve only")
			client.send("dialog --infobox \"No such Software Exists \n Sending to Main Menu\" 7 30")		
			sleep(1)
			return
		client.send("recieve only")
		client.send("dialog --infobox \"Software Successfully Installed \n Sending to Main Menu\" 7 35")		
		sleep(1)
		return
	elif choice == "2" :
		temp = getstatusoutput("yum remove " + software + " -y")
		if temp[0] != 0 :
			client.send("recieve only")
			client.send("dialog --infobox \"No such Software Exists \n Sending to Main Menu\" 7 30")		
			sleep(1)
			return
		client.send("recieve only")
		client.send("dialog --infobox \"Software Successfully Removed \n Sending to MainMenu\" 7 35")		
		sleep(1)
		return
	elif choice == "3" :
		temp = getstatusoutput("yum info " + software)
		string = temp[1]		
		if string.rfind("Name") == -1:
			client.send("recieve only")
			client.send("dialog --infobox \"No such Software Exists \n Sending to Main Menu\" 7 30")		
			sleep(1)
			return
		client.send("recieve only")
		client.send("dialog --infobox \"" + string[string.rindex("Name"):] + "\n Sending to Software Main Menu\" 7 30")		
		sleep(2)
		return
	else :
		return



