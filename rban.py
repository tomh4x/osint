#!/usr/bin/python
import sys
import re

def is_v6(rban_line):
	if (re.search( r"(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]).){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]).){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))", rban_line)):
		return True
	else:
		return False

def print_rban( ent ):
	print("----------------------------------")
	print( "regexp: " + ent['regexp'])
	print( "regexp_num: " + ent['regexp_num'])
	print( "nick: " + ent['nick1'])
	print( "ident: " + ent['ident'])
	print( "hostname: " + ent['hostname'])
	print( "ip: " + ent['ip_addr'])
	print( "rizon_mask: " + ent['rizon_mask'])
	#print( "nick2: " + ent['nick2'])
	print( "umodes: " + ent['umode'])
	print( "server: " + ent['server'])
	print("----------------------------------")




fh = open( sys.argv[1], "r")
rbans = []
for line in fh:
	L = re.match( r".*(\[RBan\].*)", line )
	if L and not is_v6(L.group(1)):
		m = re.match( r"^\[RBan\] (?P<regexp>(.*)) (?P<regexp_num>(.*))\ \-\ (?P<nick1>(.*))\!(?P<ident>(.*))\@(?P<hostname>(.*)):(?P<ip_addr>(.*)):(?P<rizon_mask>(.*))\((?P<nick2>(.*))\)\((?P<umode>(.*))\)\[(?P<server>(.*))\]$", L.group(1) )
		if m:
			rban = {
				"regexp" : m.group('regexp'),
				"regexp_num":  m.group('regexp_num'),
				"nick1" : m.group('nick1'),
				"ident" : m.group('ident'),
				"hostname" : m.group('hostname'),
				"ip_addr" : m.group('ip_addr'),
				"rizon_mask" : m.group('rizon_mask'),
				"umode" : m.group('nick2'),
				"server" : m.group('server')
			}
			rbans.append( rban )

#print( "Parsed " + str(len(rbans)) + " rbans.\n\n")
for i in range(0, len(rbans)):
	if '(r#35)' in rbans[i]['regexp_num']:
		#print_rban( rbans[i] )
		print( rbans[i]['hostname'] + "," + rbans[i]['ip_addr'])
