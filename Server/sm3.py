#!/usr/bin/python


from os import system
from commands import getstatusoutput
from time import sleep

def sm3(client) :

	temp = getstatusoutput("rpm -q ypserv")
	if temp[0] != 0 :
		temp1 = getstatusoutput("yum install ypserv -y")
		if temp1[0] != 0 :
			client.send("recieve only")
			client.send("dialog --infobox \" Download ypserv Software \n Sending to Main Menu\" 7 35")
			sleep(1)
			client.system("sm.py")
	client.send("dialog --inputbox \"Enter Domain Name for Uniqueness :\" 10 35 ")
	dname = client.recv(1024)	
	system("nisdomainname " + dname)
	system("cd /var/yp/")
	system("make")
	system("systemctl restart ypserv")
	system("systemctl enable vpserv")
	client.send("recieve only")
	client.send("dialog --infobox \"Server Successfully Installed \n Sending to Main Menu\" 10 40")
	sleep(1)	
	return


