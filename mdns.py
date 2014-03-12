#!/usr/bin/python
import sys
import socket

if (len(sys.argv) != 3):
         print("Usage: " + sys.argv[0] + " [-f|-r] list.txt")
         sys.exit(1)


def v6_lookup(host):
        try:
                ret = str(socket.getaddrinfo(host, None, socket.AF_INET6)[0][4][0])
        except socket.gaierror:
                ret = "NO_IP6"
        return(ret)

def v4_lookup(host):
        try:
                ret = str(socket.getaddrinfo(host, None, socket.AF_INET)[0][4][0])
        except socket.gaierror:
                ret = "NO_IP4"
        return(ret)


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
                        print(eachhost + " = " + v6_lookup(eachhost))
                        print(eachhost + " = " + v4_lookup(eachhost))
else:
        print("Usage: " + sys.argv[0] + " [-f|-r] list.txt")
        sys.exit(1)
