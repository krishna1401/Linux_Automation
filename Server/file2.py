#!/usr/bin/python

from os import system
from commands import getstatusoutput
from time import sleep

def file2(client) :
	client.send("dialog --inputbox \" Enter Folder Path : \" 10 35")
	fpath = client.recv(1024)	
	temporary = getstatusoutput("cd " + fpath)
	if temporary[0] != 0 :
		client.send("recieve only")
		client.send("dialog --infobox \" Incorrect Folder Path \n Sending to Main Menu....\" 6 30")
		sleep(2.5)
		return
	client.send("dialog --inputbox \" Enter File Name : \" 10 35")
	fname = client.recv(1024)
	fpath += "/" + fname
	if commands.getstatusoutput("locate -c " + fpath)[1] == 0 :
		client.send("recieve only")
		client.send("dialog --infobox \" No such File Exists...\n Sending to Main Menu...\" 7 35")
		sleep(2.5)
		return		
	getstatusoutput("rm " + fpath + "/" + fname)
	client.send("recieve only")
	client.send("dialog --infobox \" File Sucessfully Removed...\n Sending to Main Menu...\" 7 35")
	sleep(2.5)
	return


