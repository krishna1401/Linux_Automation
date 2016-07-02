#!/usr/bin/python


from os import system
from commands import getstatusoutput
from time import sleep

def lvm3(client) :

	client.send("dialog --menu \"Logical List\" 25 40 4  1 \"Logical Volume Creation\" 2 \"Logical Volume Deletion\" 3 \"Logical Volume Extention\" 4 \"Logical Volume Reduction\"")
	create = client.recv(5)	
	if create == "1" :
		client.send("dialog --inputbox \" Enter Logical Volume Name : \" 10 40")
		lvname = client.recv(1024)		
		temp = getstatusoutput("lvs")
		if temp[1].rfind(lvname) != -1 :
			client.send("recieve only")
			client.send("dialog --infobox \" Logical Volume already Exists \n Sending to Main Menu....\" 6 45")
			sleep(2.5)
			return
		client.send("dialog --inputbox \" Enter Volume Group Name : \" 10 40")
		vgname = client.recv(1024)		
		temp = getstatusoutput("vgs")
		if temp[1].rfind(vgname) == -1 :
			client.send("recieve only")
			client.send("dialog --infobox \" Volume Group does not Exists \n Sending to Main Menu....\" 6 42")
			sleep(2.5)
			return
		client.send("dialog --inputbox \" Enter Logical Volume Size : \" 10 40")
		lvsize = client.recv(1024)
		temp = getstatusoutput("lvcreate --name " + lvname + " --size " + lvsize + " " + vgname)
		if temp[0] != 0 : 
			client.send("recieve only")
			client.send("dialog --infobox \" Insufficient Space.. \n Sending to Main Menu....\" 6 40")
			sleep(2.5)
			return
	 	else :
			system("mkfs /dev" + vgname + "/" + lvname)
			system("mkdir /media/" + lvname + "_mount")
			system("mount /dev" + vgname + "/" + lvname + "/media/" + lvname + "_mount")
			client.send("recieve only")
			client.send("dialog --infobox \" Logical Volume Successfully \n Sending to Main Menu....\" 6 40")
			sleep(2.5)
			return
	elif create == "2" : 
		client.send("dialog --inputbox \" Enter Logical Volume Name : \" 10 40")
		lvname = client.recv(1024)		
		temp = getstatusoutput("lvs")
		if temp[1].rfind(lvname) != -1 :
			client.send("recieve only")
			client.send("dialog --infobox \" Logical Volume already Exists \n Sending to Main Menu....\" 6 45")
			sleep(2.5)
			return
		system("umount /media" + lvname + "_mount")
		client.send("dialog --inputbox \" Enter Volume Group Name : \" 10 40")
		vgname = client.recv(1024)		
		temp = getstatusoutput("vgs")
		if temp[1].rfind(vgname) == -1 :
			client.send("recieve only")
			client.send("dialog --infobox \" Volume Group does not Exists \n Sending to Main Menu....\" 6 42")
			sleep(2.5)
			return
		temp  = getstatusoutput("lvremove /dev/" + vgname + "/" + lvname + " -y")
		if temp[0] != 0 : 
			client.send("recieve only")
			client.send("dialog --infobox \" Logical Volume cannot be Deleted \n " + temp[1] + " \nSending to Main Menu....\" 6 42")
			sleep(2.5)
			return
	 	else :
			client.send("recieve only")
			client.send("dialog --infobox \" Logical Volume Successfully \n Sending to Main Menu....\" 6 40")
			sleep(2.5)
			return
	elif create == "3" :
		client.send("dialog --inputbox \" Enter Logical Volume Name : \" 10 40")
		lvname = client.recv(1024)		
		temp = getstatusoutput("lvs")
		if temp[1].rfind(lvname) != -1 :
			client.send("recieve only")
			client.send("dialog --infobox \" Logical Volume already Exists \n Sending to Main Menu....\" 6 45")
			sleep(2.5)
			return
		client.send("dialog --inputbox \" Enter Volume Group Name : \" 10 40")
		vgname = client.recv(1024)		
		temp = getstatusoutput("vgs")
		if temp[1].rfind(vgname) == -1 :
			client.send("recieve only")
			client.send("dialog --infobox \" Volume Group does not Exists \n Sending to Main Menu....\" 6 42")
			sleep(2.5)
			return
		client.send("dialog --inputbox \" Enter Logical Volume Size : \" 10 40")
		lvsize = client.recv(1024)		
		temp  = getstatusoutput("lvresize --size +" + lvsize + " /dev/" + vgname + "/" + lvname + " -y")
		if temp[0] != 0 : 
			client.send("recieve only")
			client.send("dialog --infobox \" Insufficient Space.. \n Sending to Main Menu....\" 6 40")
			sleep(2.5)
			return
		else :
			system("resize2fs /dev/" + vgname + "/" + lvname)
			client.send("recieve only")
			client.send("dialog --infobox \" Logical Volume Successfully \n Sending to Main Menu....\" 6 40")
			sleep(2.5)
			return
	elif create == "4" :
		client.send("dialog --inputbox \" Enter Logical Volume Name : \" 10 40")
		lvname = client.recv(1024)		
		temp = getstatusoutput("lvs")
		if temp[1].rfind(lvname) != -1 :
			client.send("recieve only")
			client.send("dialog --infobox \" Logical Volume already Exists \n Sending to Main Menu....\" 6 45")
			sleep(2.5)
			return
		client.send("dialog --inputbox \" Enter Volume Group Name : \" 10 40")
		vgname = client.recv(1024)
		temp = getstatusoutput("vgs")
		if temp[1].rfind(vgname) == -1 :
			client.send("recieve only")
			client.send("dialog --infobox \" Volume Group does not Exists \n Sending to Main Menu....\" 6 42")
			sleep(2.5)
			return
		client.send("dialog --inputbox \" Enter Logical Volume Size : \" 10 40")
		lvsize = client.recv(1024)		
		temp  = getstatusoutput("lvresize --size -" + lvsize + " /dev/" + vgname + "/" + lvname + " -y")
		if temp[0] != 0 : 
			client.send("recieve only")
			client.send("dialog --infobox \" Insufficient Space.. \n Sending to Main Menu....\" 6 40")
			sleep(2.5)
			return
		else :
			system("resize2fs /dev/" + vgname + "/" + lvname)
			client.send("recieve only")
			client.send("dialog --infobox \" Logical Volume Successfully \n Sending to Main Menu....\" 6 40")
			sleep(2.5)
			return
	else :
		return
	return

