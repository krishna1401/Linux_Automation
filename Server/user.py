#!/usr/bin/python

from os import system
from commands import getstatusoutput


#Controller Function 1 
def username1(client) :
	temporary = getstatusoutput("dir /home/")
	names = temporary[1]			
	client.send("dialog --inputbox \" Enter User Name : \" 10 30")
	temp = client.recv(1024)	
	if names.rfind(temp) != -1 :
		client.send("recieve only")
		client.send("dialog --infobox \" User Name already Exists...\n Sending to Main Menu...\" 7 35")
		sleep(1)		
		#import main
		main.main(client)	
	return temp


#Controller Function 2 
def username2(client) :
	temporary = getstatusoutput("dir /home/")
	names = temporary[1]			
	client.send("dialog --inputbox \" Enter User Name : \" 10 30")
	temp = client.recv(1024)	
	if names.rfind(temp) == -1 :
		client.send("recieve only")
		client.send("dialog --infobox \" No such User Exists...\n Sending to Main Menu...\" 7 35")
		sleep(1)
		#import main
		main.main(client)
	return temp

def user(client) :
	client.send("dialog --menu \"User List\" 25 40 3  1 \"User Creation \" 2 \"Password Management\" 3 \"User Deletion\"")
	
	choice = client.recv(10)
	if choice == "1" :
		name = username1(client)									
		client.send("dialog --insecure --passwordbox \"Enter Password : \" 7 25")
		password = client.recv(1024)	
		system("useradd " + name + " -p " + password )	
		client.send("recieve only")
		client.send("dialog --infobox \" User Successfully Added \n Sending to Main Menu\" 7 30")
		sleep(1)
		return
	elif choice == "2" :
		name = username1(client)
		client.send("dialog --insecure --passwordbox \"Enter Password : \" 7 25")
		pasword = client.recv(1024)
		password = password + "\n" + password
		system("echo -e " + password + " | passwd " + temp)
		client.send("recieve only")
		client.send("dialog --infobox \" Password Successfully Updated \n Sending to Main Menu\" 7 30")
		sleep(1)
		return
	elif choice == "3" :
		name = username2(client)
		temporary = getstatusoutput("userdel -r"+ name)
		client.send("recieve only")
		client.send("dialog --infobox \" User Successfully Deleted \n Sending to Main Menu\" 7 30")
		sleep(1)
		return
	else :
		return


