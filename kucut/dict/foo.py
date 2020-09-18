#!/usr/bin/python

from __future__ import absolute_import
from __future__ import print_function
import sys
from six.moves import map

tmp = []
lines = sys.__stdin__.readlines()
for line in map(str.strip,lines):
	if line not in tmp:
		tmp.append(line)

for word in tmp:
	print(word)
	
