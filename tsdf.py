#!/usr/bin/python
import urllib.request
import json
import sys
from time import localtime

APIKEY = '' #get your own!

qtype_verbs = { 
	"email", 
	"ip", 
	"domain", 
	"fprint", 
	"phone",
	"md5"
	}

def print_usage():
	print("\n" + sys.argv[0] + " <query type> <query value> [j]\n")
	print("[*]\ttypes are: email ip domain fprint phone md5")
	print("[*]\ta value of \"-\" can be used for lists piped from stdin.  e.g.:\n")
	print("[*]\tcat emaillist.txt|" + sys.argv[0] + " email -\n")
	print("[*]\tOPTIONAL: 3rd argument \"j\" will output records in json blocks\n")


def print_rec( dictobj, JSON=False ):
	if JSON:
		print( json.dumps(dictobj, sort_keys=True, ensure_ascii=True,indent=4, separators=(',', ': ')) )
		print("\n")
		return
	keylist = sorted( dictobj.keys() )
	doublespace = { "type", "city", "ip", "code" }
	for akey in keylist:
		spacer = "\t\t"
		if akey in doublespace:
			spacer = "\t\t\t"
		val = dictobj[akey]
		if not val:
			print( akey + " =>" + spacer + "None" )
		else:
			try:
				print( akey + " =>" + spacer + dictobj[akey])
			except UnicodeEncodeError:
				print("EXCEPT: " + dictobj[akey].__class__.__name__)
				outstr = dictobj[akey].encode('ascii','ignore')
				print( akey + " =>" + spacer + str(outstr) )
	print("----------------------------------------------------------\n")

def print_set( ds ):
	for i in range(len(ds['response'])):
		print_rec( ds['response'][i], jsonout )


def sdf_lookup( qt, qv ):
	url = 'http://api.thesecuredomain.org:1222/' + APIKEY + '/' + qt + '/' + qv
	request = urllib.request.Request(url)
	response = urllib.request.urlopen(request)
	dataset = json.loads(response.read().decode('utf-8', 'ignore'))
	return dataset

if len(sys.argv) < 3 or len(sys.argv) > 4:
	print_usage()
	sys.exit(1)

qtype = sys.argv[1]
qval = sys.argv[2]

if qtype not in qtype_verbs:
	print("Invalid query type: " + qtype)
	print_usage()
	sys.exit(1)

jsonout=False
if len(sys.argv) == 4 and sys.argv[3] == "j":
	jsonout=True

if qval == "-": 
	#list mode activatez!
	for line in sys.stdin:
		print( "querying " + line.rstrip('\n'), file=sys.stderr )
		print_set( sdf_lookup( qtype, line.rstrip('\n') ) )
else:
	print_set( sdf_lookup( qtype, qval ) )

