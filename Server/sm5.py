#!/usr/bin/python


from os import system
from commands import getstatusoutput
from time import sleep


def sm5(client) :
	client.send("recieve only")
	client.send("loop")	
	temp = getstatusoutput("rpm -q dhcp")
	if temp[0] != 0 :
		temp1 = getstatusoutput("yum install dhcp -y")
		if temp1[0] != 0 :
			client.send("recieve only")
			client.send("dialog --infobox \" Download dhcp Software \n Sending to Main Menu\" 7 35")
			sleep(2.5)
			return
	client.send("dialog --inputbox \"Enter the network card of the IP Address \n (NetMask : 255.255.255.0) :\" 10 40 ")
	ncard = client.recv(1024)
	file = open("/etc/dhcp/dhcp.conf", mode = 'a')
	file.write("subnet " + ncard + ".1 netmask 255.255.255.0{\n")
	file.write("\t range " + ncard + ".2 " + ncard + ".254;\n}")
	file.close()
	system("systemctl restart dhcpd")
	system("systemctl enable dhcpd")
	client.send("recieve only")
	client.send("dialog --infobox \"Server Successfully Installed \n Sending to Main Menu\" 10 40")
	sleep(2.5)	
	return



