#!/usr/bin/python


from os import system
from commands import getstatusoutput
from time import sleep

def lvm2(client) :
	
	client.send("dialog --menu \"Volume List\" 25 40 4  1 \"Volume Group Creation\" 2 \"Volume Group Deletion\" 3 \"Volume Group Extention\" 4 \"Volume Group Reduction\"")
	create = client.recv(5)	
	if create == "1" : 
		client.send("dialog --inputbox \" Enter Volume Group Name : \" 10 40")
		vgname = client.recv(1024)		
		temp = getstatusoutput("vgs")
		if temp[1].rfind(vgname) != -1 :
			client.send("recieve only")
			clientsend("dialog --infobox \" Volume Group already Exists \n Sending to Main Menu....\" 6 42")
			sleep(1)
			return
		client.send("dialog --inputbox \" Enter 1st Device Name : \" 10 40")
		name1 = client.recv(1204)		
		temp = getstatusoutput("pvdisplay " + name1)
		if temp[0] != 0 :	
			client.send("recieve only")
			client.send("dialog --infobox \" Device is not Physical Volume \n Sending to Main Menu....\" 6 42")
			sleep(1)
			return
		client.send("dialog --inputbox \" Enter 2st Device Name(if required) :\n Else Press \'n\' \" 10 42")
		name2 = client.recv(1024)		
		temp = getstatusoutput("pvdisplay " + name2)
		if temp[0] != 0 and name2 != "n":	
			client.send("recieve only")
			client.send("dialog --infobox \" Device is not Physical Volume \n Sending to Main Menu....\" 6 42")
			sleep(1)
			return
		if name2 != "n" :
			temp = getstatusoutput("vgcreate " + vgname + " " + name1 + " " + name2)
		else :
			temp = getstatusoutput("vgcreate " + vgname + " " + name1)
		if temp[0] != 0 :
			client.send("recieve only")
			client.send("dialog --infobox \" Volume Group cannot be Created \n Sending to Main Menu....\" 6 40")
			sleep(1)
			return
		else :	
			client.send("recieve only")
			client.send("dialog --infobox \" Volume Group Successfully Created \n Sending to Main Menu....\" 6 45")
			sleep(1)
			return
	elif create == "2" :
		client.send("dialog --inputbox \" Enter Volume Group Name : \" 10 40")
		vgname = client.recv(1024)		
		temp = getstatusoutput("vgs")
		if temp[1].rfind(vgname) != -1 :
			client.send("recieve only")
			client.send("dialog --infobox \" Volume Group does not Exists \n Sending to Main Menu....\" 6 42")
			sleep(1)
			return
		temp = getstatusoutput("vgremove " + vgname)
		if temp[0] != 0 :
			client.send("recieve only")
			client.send("dialog --infobox \" Volume Group cannot be Removed \n Sending to Main Menu....\" 6 40")
			sleep(1)
			return
		else :	
			client.send("recieve only")
			client.send("dialog --infobox \" Volume Group Successfully Removed \n Sending to Main Menu....\" 6 45")
			sleep(1)
			return
	elif create == "3" :
		client.send("dialog --inputbox \" Enter Volume Group Name : \" 10 40")
		vgname = client.recv(1024)		
		temp = getstatusoutput("vgs")
		if temp[1].rfind(vgname) != -1 :
			client.send("recieve only")
			client.send("dialog --infobox \" Volume Group already Exists \n Sending to Main Menu....\" 6 42")
			sleep(1)
			return
		client.send("dialog --inputbox \" Enter 1st Device Name : \" 10 40")
		name1 = client.recv(1024)		
		temp = getstatusoutput("pvdisplay " + name1)
		if temp[0] != 0 :	
			client.send("recieve only")
			client.send("dialog --infobox \" Device is not Physical Volume \n Sending to Main Menu....\" 6 42")
			sleep(1)
			return
		temp = getstatusoutput("vgextend " + vgname + " " + name1)
		if temp[0] != 0 :
			client.send("recieve only")
			client.send("dialog --infobox \" Volume Group cannot be Extended \n Sending to Main Menu....\" 6 40")
			sleep(1)
			return
		else :	
			client.send("recieve only")
			client.send("dialog --infobox \" Volume Group Successfully Extended \n Sending to Main Menu....\" 6 45")
			sleep(1)
			return
	elif create == "4" :
		client.send("dialog --inputbox \" Enter Volume Group Name : \" 10 40")
		vgname = client.recv(1024)		
		temp = getstatusoutput("vgs")
		if temp[1].rfind(vgname) != -1 :
			client.send("recieve only")
			client.send("dialog --infobox \" Volume Group already Exists \n Sending to Main Menu....\" 6 42")
			sleep(1)
			return
		client.send("dialog --inputbox \" Enter 1st Device Name : \" 10 40")
		name1 = client.recv(1024)		
		temp = getstatusoutput("pvdisplay " + name1)
		if temp[0] != 0 :	
			client.send("recieve only")
			client.send("dialog --infobox \" Device is not Physical Volume \n Sending to Main Menu....\" 6 42")
			sleep(1)
			return
		temp = getstatusoutput("vgreduce " + vgname + " " + name1)
		if temp[0] != 0 :
			client.send("recieve only")
			client.send("dialog --infobox \" Volume Group cannot be Reduced \n Sending to Main Menu....\" 6 40")
			sleep(1)
			return
		else :	
			client.send("recieve only")
			client.send("dialog --infobox \" Volume Group Successfully Reduced \n Sending to Main Menu....\" 6 45")
			sleep(1)
			return



