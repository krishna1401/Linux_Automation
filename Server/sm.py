#!/usr/bin/python


from os import system
from commands import getstatusoutput


def sm(client) :
	client.send("dialog --inputbox \"Server List\" 20 40 2 1 \"Server Installation\" 2 \"Server Un-installation\"")
	choice = client.recv(5)
	if choice == "1" :
		import smi
		smi.smi(client)
		return
	elif choice == "2" :
		import smu
		smu.smu(client)
		return
	else
		return
	return


