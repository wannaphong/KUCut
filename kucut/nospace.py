#!/usr/bin/python

from __future__ import absolute_import
from __future__ import print_function
import sys

for line in sys.__stdin__.readlines():
    print(''.join(line.strip().split()).replace('_',''))
