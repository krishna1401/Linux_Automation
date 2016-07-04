#!/usr/bin/python


from os import system
from commands import getstatusoutput
from time import sleep

#Controller Function 
def username(client) :
	temporary = getstatusoutput("dir /home/")
	names = temporary[1]			
	client.send("dialog --inputbox \" Enter User Name : \" 10 30")
	temp = client.recv(1024)	
	if names.rfind(temp) == -1 :
		client.send("recieve only")
		client.send("dialog --infobox \" No such Directory Exists...\n Sending to Main Menu...\" 7 35")
		sleep(2.5)
		import menu
		menu.menu(client)
	system("useradd -s /sbin/login " + temp)
	password = ("dialog --insecure --passwordbox \"Enter Password : \" 7 25")
	password = password + "\n" + password
	system("echo -e " + password + " | smdpasswd -a" + temp)

def sm9(client) :
	client.send("recieve only")
	client.send("loop")	
	temp = getstatusoutput("rpm -q samba")
	if temp[0] != 0 :
		temp1 = getstatusoutput("yum install samba* -y")
		if temp1[0] != 0 :
			client.send("recieve only")
			client.send("dialog --infobox \" Download samba Software \n Sending to Main Menu\" 7 35")
			sleep(2.5)
			return
	client.send("dialog --inputbox \" Enter Folder Path : \" 10 35")
	fpath = client.recv(1024)	
	temporary = getstatusoutput("cd " + fpath)
	if temporary[0] != 0 :
		client.send("recieve only")
		client.send("dialog --infobox \" Incorrect Folder Path \n Sending to Main Menu....\" 6 30")
		sleep(2.5)
		return
	client.send("dialog --inputbox \"Enter Share Name : \" 10 30 ")	
	sname = client.recv(1024)	
	file = open("/etc/samba/smb.conf", mode = 'a')
	file.write("[" + sname + "]")
	file.write("path = " + fpath)
	file.close()
	username(client)
	system("systemctl restart smb")
	system("systemctl enable smb")
	client.send("recieve only")
	client.send("dialog --infobox \"Server Successfully Installed \n Sending to Main Menu\" 10 40")
	sleep(2.5)	
	return

	
