#/usr/bin/python

import socket
from os import system
from commands import getstatusoutput
from time import sleep

ob = socket.socket()
ip = raw_input("Enter Ip : ") 
ob.bind((ip,14011))
ob.listen(6)
client,addr = ob.accept()
client.send("dialog --infobox \"  Welcome to Linux Automation \n *****************************\" 5 35")
sleep(2.5)
import main
main.main(client)
raw_input()
