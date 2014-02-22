#!/usr/bin/python
from netaddr import *
import sys
with open(sys.argv[1]) as fh:
	for content in fh:
		for ip in IPNetwork(content):
			print('%s' % ip)

