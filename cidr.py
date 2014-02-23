#!/usr/bin/python
from netaddr import *
import sys

if len(sys.argv) != 2:
	print(sys.argv[0] + " <filename> or - to read from stdin")
	sys.exit(1)

if sys.argv[1] == "-":
	fh = sys.stdin
else:
	fh = open(sys.argv[1],"r")
for content in fh:
	for ip in IPNetwork(content):
		print('%s' % ip)

