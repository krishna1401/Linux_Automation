#!/usr/bin/python


from os import system
from commands import getstatusoutput
from time import sleep

def dpm(client) :
	client.send("dialog --menu \"Menu List\" 30 40 2  1 \"Partition Creation\" 2 \"Partition Deletion\"")
	choice = client.recv(5)

	if choice == "1" :
		client.send("dialog --inputbox \" Enter Partition Name : \" 10 30")
		name = client.recv(1024)
		test = getstatusoutput("parted /dev/sda print | tail -2")[1].split()
		if test[4] == "primary" :
			string = getstatusoutput("parted /dev/sda  print free | tail -2 ")[1].split()			
			system("parted /dev/sda mkpart extended " + string[0] + " " + string[1])
		string = getstatusoutput("parted /dev/sda  print free | tail -3 | head -1")[1].split()
		space = "Available Space " + string[2]	
		client.send("dialog --inputbox \"" + space + "\nEnter Partition Size (in GiB)\" 10 30")
		size = client.recv(10)
		if size > string[2] :
			client.send("recieve only")
			client.send("dialog --infobox \" Specified Space Not Available\n Sending to Main Menu...\" 7 35")
			sleep(1)
			return
		end = int(string[0].split("G")[0]) + float(size.split("G")[0])
		system("parted /dev/sda mkpart logical " + string[0] + " {}".format(end) + "G")
		system("mkdir /media/" + name)
		form = "/dev/sda" + getstatusoutput("parted /dev/sda print | tail -2")[1].split()[0]		
		system("mkfs.ext4 " + form)
		system("mount " + form + " /media/" + name)
		file = open("/etc/fstab", mode = "a")
		file.write(form  + "    " + "/media/" + name + "       ext4 	default 0  0")
		file.close()
		client.send("recieve only")
		client.send("dialog --infobox \" Partition Successfully Created\n Sending to Main Menu...\" 7 37")
		sleep(1)
		return
	elif choice == "2" :
		string = getstatusoutput("parted /dev/sda print | tail -2")[1].split()
		system("umount /dev/sda" + string[0])
		system("parted /dev/sda rm " + string[0])
		temp = getstatusoutput("cat /etc/fstab")[1]
		count = temp.find("/dev/sda" + string[0])
		if count > 0:		
			temp = temp[0:count]
			file = open("/etc/fstab",mode = 'w')
			file.write(temp)
			file.close()
		client.send("recieve only")
		client.send("dialog --infobox \" Partition Successfully Removed\n Sending to Main Menu...\" 7 37")
		sleep(1)
		return
	else :
		return
	return
