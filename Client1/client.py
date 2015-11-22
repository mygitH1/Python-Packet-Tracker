
# *******************************************************************
# This file illustrates how to send a file using an
# application-level protocol where the first 10 bytes
# of the message from client to server contain the file
# size and the rest contain the file data.
# *******************************************************************
import socket
import os
import sys
import subprocess

def upload(cmd):
	fileName = cmd[1]
	fileData = None
	fileObj = open(str(fileName), "r")
	
	while True:
		fileData = fileObj.read(65536)
		
		# Make sure we did not hit EOF
		if fileData:
			dataSizeStr = str(len(fileData))
			while len(dataSizeStr) < 10:
				dataSizeStr = "0" + dataSizeStr
			fileData = dataSizeStr + fileData
			numSent = 0
			# Send the data!
			while len(fileData) > numSent:
				numSent += connSock.send(fileData[numSent:])
				#print(numSent)
			print fileName+" "+str(numSent)+" Byte transferred"
		else:
			break
		fileData
	fileObj.close()
	connSock.send(fileName)
	i=0
        with open(fileName) as fp:
            for line in fp:
                print "sending package ",(i+1),"..... packet sent"
                i=i+1
        print "total packet sent : ",i
        fp.close()

serverAddr="localhost"

connSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Connect to the server
serverAddr=raw_input("Enter the Destination IP Address :")
connSock.connect(("localhost", 1234))
while True:
	cmd=raw_input("ftp>")
	
	cmd=cmd.split( );
	if len(cmd)<2 and not (cmd[0]=="ls" or cmd[0]=="quit"):
		print "provide Arguments"
		continue 
	connSock.send(cmd[0])
	if cmd[0]=="put":
		upload(cmd)
	elif cmd[0]=="ls":
		s=""
		p = subprocess.Popen('dir /b', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
		for line in p.stdout.readlines():
			s+=line
		print s
	elif cmd[0]=="quit":
		connSock.close()
		break;
	else:
		print "invalid command......."
connSock.close()
