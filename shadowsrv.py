#!/usr/bin/python3
import socket
import sys


def recvall(sock):
	databuf = []
	while 1:
		data = sock.recv(1480)
		if not data: break
		databuf.append(data.decode('utf-8', errors='ignore'))  #python3 requires decoding from byte to unicode, also ignore non-unicode chars 
	return ''.join(databuf).strip()

# MAIN:
# prepare socket for IP list
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
shadowserv = socket.gethostbyname( 'asn.shadowserver.org'  )
s.connect((shadowserv, 43))
s.send('begin origin\r\n'.encode())


# load and send IPs
if len(sys.argv) > 1: 
	f = open( sys.argv[1], "r")
	for line in f.readlines():
		s.send(line.encode())
else:
	for line in sys.stdin:
		s.send(line.encode())

s.send('end origin\r\n'.encode())


# puke output!
retbuf = recvall(s)
print(retbuf)
s.close()
