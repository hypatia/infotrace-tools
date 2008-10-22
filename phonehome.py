#!/usr/bin/python
### phonehome.py
### Hello World demonstration script

phonehome_url = "http://infotrace.citizenlab.org"

#import sys, urllib, popen2
import sys, urllib, commands

#trace_output = popen2.popen2("tcptraceroute en.wikipedia.org")[0].read()
trace_output = commands.getoutput('tcptraceroute en.wikipedia.org')

#urllib.urlopen(phonehome_url, trace_output)
print trace_output

