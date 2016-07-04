#!/usr/bin/python


from os import system
from commands import getstatusoutput
from time import sleep


#Controller Function 
def control(client,name) :
	client.send("recieve only")
	client.send("loop")	
	temp = getstatusoutput("rpm -q " + name)
	if temp[0] == 0 :
		system("yum remove " + name + " -y")
		client.send("recieve only")
		client.send("dialog --infobox \"Server Successfully Removed \n Sending to Main Menu\" 10 40")
		sleep(2.5)	
	return


def smu(client) :

	client.send("dialog --menu \"Server Installation List\" 30 55 8  1 \"Apache Server\" 2 \"File Transfer Protocol Server\" 3 \"Network Information System Server\" 4 \"Network File Sharing Server\" 5 \"Dynamic Host Configuration Protocol Server\" 6 \"Mail Server\" 7 \"Remote Login Server\" 8 \"MariaDB Server\"")
	choice = client.recv(5)

	if choice == "1" :
		control(client,"httpd")
		return
	elif choice == "2" :
		control(client,"vsftpd")
		return
	elif choice == "3" :
		control(client,"ypserv")
		return
	elif choice == "4" :
		control(client,"nfs-utils")
		return
	elif choice == "5" :
		control(client,"dhcp")
		return	
	elif choice == "6" :
		control(client,"postfix")
		return
	elif choice == "7" :
		client.send("dialog --menu \"Remote Server List\" 20 50 2  1 \"Telnet Server\" 2 \"SSH Server\" ")
		create = client.recv(5)		
		if create == "1" :
			control(client,"telnet-server")
			return
		elif create == "2" :
			control(client,"openssh-server")
			return
		else : 
			return
	elif choice == "8" :
		control(client,"mariadb-server")
	else :
		return
	return
