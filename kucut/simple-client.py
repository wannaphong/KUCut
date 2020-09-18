#!/usr/bin/python

from __future__ import absolute_import
from __future__ import print_function
import sys
from six.moves.xmlrpc_client import ServerProxy

server = ServerProxy(uri="http://localhost:8089",encoding='cp874')

text = sys.argv[1]

try:
	text = text.decode('utf8').encode('cp874')
except Exception as e:
	pass

tmp = []
for token in text.split():
	result = server.cutsentence(text)
	tmp.append(result)
print(' _ '.join(tmp))
