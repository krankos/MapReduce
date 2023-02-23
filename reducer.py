
# create line by line reducer 

import sys

total=0
oldkey = None
for line in sys.stdin:
    line = line.strip()
    data = line.split('\t')

    if len(data) != 2:
        print('Error: line does not contain 2 elements')
        continue
    word, count = data
    thiskey = word
    if oldkey and oldkey != thiskey:
        print ('%s\t%s' % (oldkey, total))
        total = 0
    oldkey = thiskey
    total+=1
if oldkey != None:
    print ('%s\t%s' % (oldkey, total))

