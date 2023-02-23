#!/usr/bin/python
# create line by line reducer 

import sys

for line in sys.stdin:
    line = line.strip()
    data = line.split('\t')
    total=0
    if len(data) != 2:
        print('Error: line does not contain 2 elements')
        continue
    word, count = data
    oldkey = None
    thiskey = word
    if oldkey and oldkey != thiskey:
        print ('%s\t%s' % (oldkey, total))
        total = 0
    oldkey = thiskey
    total+=1
if oldkey != None:
    print ('%s\t%s' % (oldkey, total))

