#!/usr/bin/python

from os import system
from commands import getstatusoutput
from time import sleep


def file3(client) :

	client.send("dialog --inputbox \" Enter Folder Path : \" 10 35")
	fpath = client.recv(1024)	
	temporary = getstatusoutput("cd " + fpath)
	if temporary[0] != 0 :
		client.send("recieve only")
		client.send("dialog --infobox \" Incorrect Folder Path \n Sending to Main Menu....\" 6 30")
		sleep(1)
		return
	client.send("dialog --inputbox \" Enter File Name : \" 10 35")
	fname = client.recv(1024)	
	fpath += "/" + fname
	if commands.getstatusoutput("locate -c " + fpath)[1] == 0 :
		client.send("recieve only")
		client.send("dialog --infobox \" No such File Exists...\n Sending to Main Menu...\" 7 35")
		sleep(1)
		return
	client.send("dialog --inputbox \"Press \'u\' to change Owner Permission \nPress \'g\' to change Group Permission  \nPress \'o\' to change Others Permission \nPress \'a\' to change Everyone Permission\" 11 50")
	who = client.recv(5)
	client.send("dialog --inputbox \"Press \'r\' to provide Read Permission \nPress \'w\' to provide Write Permission  \nPress \'x\' to provide Executable Permission \n**You can assign more than one Permissions\" 11 52")
	perm = client.recv(5)
	client.send("dialog --menu \"Permission List\" 20 30 8  1 \"Add Permissions\" 2 \"Remove Pemissions\"")
	create = client.recv(5)	
	if create == "1" :
		temporary = getstatusoutput("chmod " + who + "+" + perm + " " + fpath)
		if temporary[0] != 0 :
			client.send("recieve only")
			client.send("dialog --infobox \" Incorrect Permission\n Sending to Main Menu...\" 7 30")
			sleep(1)
			return
		else :
			client.send("recieve only")
			client.send("dialog --infobox \" Permission Successfully Added\n Sending to Main Menu...\" 7 35")
			sleep(1)
			return
	elif create == "2" :
		temporary = getstatusoutput("chmod " + who + "-" + perm + " " + fpath)
		if temporary[0] != 0 :
			client.send("recieve only")
			client.send("dialog --infobox \" Incorrect Permission\n Sending to Main Menu...\" 7 30")
			sleep(1)
			return
		else :
			client.send("recieve only")
			client.send("dialog --infobox \" Permission Successfully Removed\n Sending to Main Menu...\" 7 35")
			sleep(1)
			return
	else :
		return


