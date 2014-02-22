#!/usr/bin/python
import sys
import operator
L = [] #list of hosts
hostcount = {} #hashmap (key=host, value = frequency)


#load the host list
for line in sys.stdin:
	L.append(line.rstrip())
	#L.append( line.split("@")[1].rstrip().lower())

#initialize counters
for idx, val in enumerate(L):
	hostcount[val] = 0

#count
for idx, val in enumerate(L):
	hostcount[val] +=1

#sort into list in descending order
sorted_hosts = sorted(hostcount.items(), key=operator.itemgetter(1), reverse=True)

#print
for w in sorted_hosts:
	 print (str(w[0]) + "," + str(w[1]))

