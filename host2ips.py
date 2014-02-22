#!/usr/bin/python
import sys
import socket
import re

if len(sys.argv) != 2:
	print(sys.argv[0] + "<mixed hostlist input file>")
	sys.exit(1)

def do_lookup( host ):
	return socket.gethostbyname(host.rstrip('\n'))

if sys.argv[1] == "-":
	f = sys.stdin
else:
	f = open(sys.argv[1], 'r')

for line in f:
	line = line.rstrip('\n')
	m = re.match(r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$', line )
	if m:
		#host is already an IP
		#print( line + " matched!")
		print(line)
		continue
	#host needs a lookup first
	#print( line + " did NOT match!")
	ip = do_lookup(line)
	if ip != "67.215.65.132": #ignore OpenDNS incase it doesn't return NXDOMAIN
		print( ip )

