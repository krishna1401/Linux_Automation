#!/usr/bin/python


from os import system
from socket import socket
from time import sleep

system("yum install dialog -y")
ob = socket()
sip = raw_input("Enter Server IP Address : ")
port = 14010

ob.connect((sip,port))
ob.send("Connected")

welcome = ob.recv(2048)
system(welcome)

while True:
	message= ob.recv(2048)
	print message
	if message == "false" :
		print "Connection Cancelled"
		break
	if message == "recieve only" :
		message = ob.recv(2048)
		continue
	message = message + "2> /tmp/data.txt"
	system(message)
	sleep(5)
	file = open("/tmp/data.txt")
	sdata = file.read()
	ob.send(sdata)
	
	
