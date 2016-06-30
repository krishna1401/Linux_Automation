#!/usr/bin/python

from os import system
from commands import getstatusoutput
from time import sleep

#Controller Function 1 
def username1(client) :
	temporary = getstatusoutput("dir /home/")
	names = temporary[1]			
	client.send("dialog --inputbox \" Enter User Name : \" 10 30")
	temp = client.recv(1024)	
	if names.rfind(temp) == -1 :
		send("recieve only")
		send("dialog --infobox \" No such User Exists...\n Sending to Main Menu...\" 7 35")
		sleep(1)
		import menu
		menu.menu(client)
	return temp



def dir4(client) :
	client.send("dialog --inputbox \" Enter Folder Path : \" 10 35")
	fpath = client.recv(1024)
	temporary = getstatusoutput("cd " + fpath)
	if temporary[0] != 0 :
		client.send("recieve only")
		client.send("dialog --infobox \" Incorrect Folder Path \n Sending to Main Menu....\" 6 30")
		sleep(1)
		return
	name = username1(client)
	client.send("dialog --inputbox \" Enter Folder Name : \" 10 35")
	fname = client.recv(1024)	
	fpath += "/" + fname
	if commands.getstatusoutput("locate -c " + fpath)[1] == 0 :
		client.send("recieve only")
		client.send("dialog --infobox \" No such Directory Exists...\n Sending to Main Menu...\" 7 35")
		sleep(1)
		return
	client.send("dialog --menu \"Permission List\" 20 30 8  1 \"Change Ownership \" 2 \"Change Group\"")
	create = client.recv(1024)	
	if create == "1" :
		system("chown " + name + " " + fpath)		
		client.send("recieve only")
		client.send("dialog --infobox \" Ownership Successfully Added\n Sending to Main Menu...\" 7 35")
		sleep(1)
		return		
	elif create == "2" :
		system("chgrp " + name + " " + fpath)		
		client.send("recieve only")
		client.send("dialog --infobox \" Group Successfully Added\n Sending to Main Menu...\" 7 35")
		sleep(1)
		return
	else :
		return
	return
