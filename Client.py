#!/usr/bin/python


from os import system
from socket import socket
from time import sleep
from commands import getstatusoutput

getstatusoutput("yum install dialog -y")
ob = socket()
sip = raw_input("Enter Server IP Address : ")
port = 14011

ob.connect((sip,port))

welcome = ob.recv(2048)
system(welcome)

while True:
	message= ob.recv(2048)
	if message == "false" :
		print "Connection Cancelled"
		message = ""
		break
	if message == "recieve only" :
		message = ob.recv(2048)
		continue
	message = message + " 2> /tmp/data.txt"
	system(message)
	file = open("/tmp/data.txt")
	sdata = file.read()
	ob.send(sdata)
	message = ""
	
