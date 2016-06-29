#!/usr/bin/python


from os import system
from commands import getstatusoutput
from time import sleep


def lvm(client) :

	client.send("dialog --menu \"LVM List\" 30 40 3  1 \"Physical Volume Management\" 2 \"Volume Group Management\" 3 \"Logical Volume Management\"")
	choice = client.recv(5)

	if choice == "1" :
		import lvm1
		lvm1.lvm1(client)
		return
	elif choice == "2" :
		import lvm2
		lvm2.lvm2(client)
		return
	elif choice == "3" :
		import lvm3
		lvm3.lvm3(client)
		return
	else :
		return
