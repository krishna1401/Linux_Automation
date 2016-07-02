#!/usr/bin/python


from os import system
from commands import getstatusoutput


def menu(client) :
	while True :	
		client.send("dialog --menu \"Menu List\" 30 50 8  1 \"User Management\" 2 \"Directory Management\" 3 \"File Management\" 4 \"Software Management\" 5 \"Device Partition Management\" 6 \"Logical Volume Management\" 7 \"Server Management\" 8 \"Exit\" ")
		choice = client.recv(10)

		if choice == "1" :   
			import user
			user.user(client)
		elif choice == "2" : 
			import dirs
			dirs.dirs(client)
		elif choice == "3" : 
			import files
			files.files(client)
		elif choice == "4" :
			import software
			software.software(client)	
		elif choice == "5" :
			import dpm
			dpm.dpm(client)
		elif choice == "6" :
			import lvm
			lvm.lvm(client)
		elif choice == "7" :
			import sm
			sm.sm(client)
		elif choice == "8" :
			client.send("recieve only")
			client.send("dialog --infobox \"Thank You... \n Exiting....\" 5 18")
			client.send("false")


