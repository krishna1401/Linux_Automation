#!/usr/bin/python


from os import system
from commands import getstatusoutput
from time import sleep

def lvm1(client) :

	client.send("dialog --inputbox \" Enter Device Path : \" 10 35")
	name = client.recv(1024)	
	if name.rfind("/dev/") == -1 :	
		client.send("recieve only")
		client.send("dialog --infobox \" No such Device Exists \n Sending to Main Menu....\" 6 30")
		sleep(1)
		return
	client.send("dialog --menu \"Physical List\" 25 40 2  1 \"Physical Volume Creation\" 2 \"Physical Volume Deletion\"")
	create = client.recv(5)
	if create == "1" : 
		temp = getstatusoutput("pvcreate " + name)
		if temp[0] != 0 :
			client.send("recieve only")
			client.send("dialog --infobox \" Physical Volume cannot be Created \n Sending to Main Menu....\" 6 40")
			sleep(1)
			return
		else :
			client.send("recieve only")
			client.send("dialog --infobox \" Physical Volume Successfully Created \n Sending to Main Menu....\" 6 45")
			sleep(1)
			return
	elif create == "2" :
		temp = getstatusoutput("pvremove " + name)
		if temp[0] != 0 :
			client.send("recieve only")
			client.send("dialog --infobox \" Physical Volume cannot be Removed \n Sending to Main Menu....\" 6 40")
			sleep(1)
			return
		else :
			client.send("recieve only")
			client.send("dialog --infobox \" Physical Volume Successfully Removed \n Sending to Main Menu....\" 6 45")
			sleep(1)
			return
	return

