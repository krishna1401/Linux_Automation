#!/usr/bin/python

from os import system
from commands import getstatusoutput
from time import sleep

def dir1(client) :
	client.send("dialog --inputbox \" Enter Folder Path : \" 10 35")
	fpath = client.recv(1024)	
	temporary = getstatusoutput("cd " + fpath)
	if temporary[0] != 0 :
		client.send("recieve only")
		client.send("dialog --infobox \" Incorrect Folder Path \n Sending to Main Menu....\" 6 30")
		sleep(1)
		return
	client.send("dialog --inputbox \" Enter Folder Name : \" 10 35")
	fname = client.recv(1024)
	system("mkdir " + fpath + "/" + fname)
	client.send("recieve only")
	client.send("dialog --infobox \" Directory Sucessfully Created...\n Sending to Main Menu...\" 7 35")
	sleep(1)
	return
