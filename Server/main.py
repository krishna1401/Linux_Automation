#!/usr/bin/python

from os import system
from commands import getstatusoutput
from time import sleep

def main(client) :
	temporary = getstatusoutput("dir /home/")
	names = temporary[1]
	names = names + "root"	
	client.send("dialog --inputbox \" User Name : \" 9 30")
	user = client.recv(2048)
	client.send("dialog --insecure --passwordbox \" Password : \" 9 30")
	password = client.recv(2048)	
	print "{}    {}".format(user,password)
	if names.rfind(user) == -1 or password != "redhat" :
		client.send("recieve only")
		client.send("dialog --infobox \"Incorrect Password or User Name \n Terminating....\" 5 40")
		sleep(1)
		client.send("false")
	else :
		client.send("recieve only")
		client.send("dialog --infobox \"Authentified User \n Processing...\" 5 25")	
		sleep(1)
		import menu
		menu.menu(client)
	
 
