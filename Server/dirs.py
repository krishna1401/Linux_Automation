#!/usr/bin/python

from os import system
from commands import getstatusoutput
from time import sleep

def dirs(client) :
	client.send("dialog --menu \"Directory List\" 30 50 4  1 \"Directory Creation\" 2 \"Directory Deletion\" 3 \"Permission Alteration\" 4 \"Ownership/Group Management\" ")
	choice = client.recv(10)

	if choice == "1" :
		import dir1
		dir1.dir1(client)
		return
	elif choice == "2" :
		import dir2
		dir2.dir2(client)
		return
	elif choice == "3" :
	 	import dir3
		dir3.dir3(client)
		return
	elif choice == "4" :
		import dir4
		dir4.dir4(client)
		return
	else :
		return
	return
