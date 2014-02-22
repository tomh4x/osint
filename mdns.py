#!/usr/bin/python
import sys
import socket

if (len(sys.argv) != 3):
	 print("Usage: " + sys.argv[0] + " [-f|-r] list.txt")
	 sys.exit(1)

if sys.argv[1] == "-r":
	with open(sys.argv[2]) as fh:
		for eachip in fh:
			eachip = eachip.rstrip('\n')
			try:
				print(eachip + " = " + socket.gethostbyaddr(eachip)[0])
			except socket.herror:
				print(eachip + " = NO_REVERSE")
				continue
elif sys.argv[1] == "-f":
	with open(sys.argv[2]) as fh:
		for eachhost in fh:
			eachhost = eachhost.rstrip('\n')
			try:
				print(eachhost + " = " + socket.gethostbyname(eachhost))
			except socket.herror:
				print(eachhost + " = NO_IP")
				continue
else:
	print("Usage: " + sys.argv[0] + " [-f|-r] list.txt")
	sys.exit(1)
