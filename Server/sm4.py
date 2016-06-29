#!/usr/bin/python


from os import system
from commands import getstatusoutput
from time import sleep

#Controller Function
def control_nfs(client) :
	client.send("dialog --inputbox \"Enter Folder Path \n (To be Shared): \" 10 35 ")
	fpath = client.recv(1024)
	temporary = getstatusoutput("cd " + fpath)
	if temporary[0] != 0 :
		client.send("recieve only")
		client.send("dialog --infobox \"Incorrect Path, No such Path Exists \n Sending to Main Menu \" 10 40")
		sleep(1)
		import menu
		menu.menu(client)
	client.send("dialog --inputbox \"Enter IP address of client or press * for all :\" 10 45 ")
	ip = client.recv(1024)
	client.send("dialog --inputbox \"Enter Permissions \n (Read & Write -> \'rw\' | Read only -> \'r\' ) :\" 12 35 ")
	per = client.recv(1024)	
	file = open("/etc/exports", mode = 'a')
	file.write(fpath + " " + ip + "(" + per + ") \n") 
	file.close()


def sm4(client) :

	temp = getstatusoutput("rpm -q nfs-utils")
	if temp[0] != 0 :
		temp1 = getstatusoutput("yum install nfs-server -y")
		if temp1[0] != 0 :
			client.send("recieve only")
			client.send("dialog --infobox \" Download nfs-server Software \n Sending to Main Menu\" 7 35")
			sleep(1)
			return
	control_nfs(client)
	system("systemctl restart nfs-server")
	system("systemctl enable nfs-server")
	client.send("recieve only")
	client.send("dialog --infobox \"Server Successfully Installed \n Sending to Main Menu\" 10 40")
	sleep(1)	
	return


