#!/usr/bin/python


from os import system
from commands import getstatusoutput
from time import sleep


#Controller Function 
def control(client,name1, name2) :
	client.send("recieve only")
	client.send("loop")	
	temp = getstatusoutput("rpm -q " + name1)
	if temp[0] != 0 :
		temp1 = getstatusoutput("yum install " + name1 + " -y")
		if temp1[0] != 0 :
			client.send("recieve only")
			message = "Download " + name1 + " Software"
			client.send("dialog --infobox \"" + message + "\n Sending to Main Menu\" 7 35")
			sleep(2.5)
			return
	system("systemctl restart " + name2)
	system("systemctl enable " + name2)
	client.send("recieve only")
	client.send("dialog --infobox \"Server Successfully Installed \n Sending to Main Menu\" 10 40")
	sleep(2.5)	
	return

def smi(client) :

	client.send("dialog --menu \"Server List\" 30 55 9  1 \"Apache Server\" 2 \"File Transfer Protocol Server\" 3 \"Network Information System Server\" 4 \"Network File Sharing Server\" 5 \"Dynamic Host Configuration Protocol Server\" 6 \"Mail Server\" 7 \"Remote Login Server\" 8 \"MariaDB Server\" 9 \"Samba Server\"")
	choice = client.recv(5)

	if choice == "1" :
		control(client,"httpd","httpd")
		return
	elif choice == "2" :
		control(client,"vsftpd","vsftpd")
		return
	elif choice == "3" :
		import sm3
		sm3.sm3(client)
		return
	elif choice == "4" :
		import sm4
		sm4.sm4(client)
		return
	elif choice == "5" :
		import sm5
		sm5.sm5(client)
		return	
	elif choice == "6" :
		control(client,"postfix","postfix")
		return
	elif choice == "7" :
		client.send("dialog --menu \"Remote Server List\" 20 50 2  1 \"Telnet Server\" 2 \"SSH Server\" ")
		create = client.recv(5)		
		if create == "1" :
			control(client,"telnet-server","telnet.socket")
			return
		elif create == "2" :
			control(client,"openssh-server","sshd")
			return
		else : 
			return
	elif choice == "8" :
		control(client,"mariadb-server","mariadb")
	elif choice == "9" :
		import sm9
		sm9.sm9(client)
		return
	else :
		return
	return
