#!/usr/bin/python
### populate_nodes.py
### get me some nodes!

import xmlrpclib

api_server = xmlrpclib.ServerProxy('https://www.planet-lab.org/PLCAPI/')

auth = {}

#auth['Username'] = "utoronto_infotrace"
auth['Username'] = "email"
auth['AuthString'] = "pass"
auth['AuthMethod'] = "password"

#debug auth problems
#authorized = api_server.AuthCheck(auth)
#if authorized:
#    print 'We are authorized!'

node_list = [line.strip() for line in open("nodedel.txt")]

api_server.DeleteSliceFromNodes(auth, "utoronto_infotrace", node_list)

