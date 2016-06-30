#!/usr/bin/python

from os import system
from commands import getstatusoutput
from time import sleep

def files(client) :
	
	client.send("dialog --menu \"File List\" 30 50 4  1 \"File Creation\" 2 \"File Deletion\" 3 \"Permission Alteration\" 4 \"Ownership/Group Management\" ")
	choice = client.recv(5)

	if choice == "1" :
		import file1
		file1.file1(client)
		return
	elif choice == "2" :
		import file2
		file2.file2(client)
		return	
	elif choice == "3" :
	 	import file3
		file3.file3(client)
		return
	elif choice == "4" :
		import file4
		file4.file4(client)
		return
	else :
		return
	return

