
# create simple line by line mapper

import sys
for line in sys.stdin:
    line = line.strip()
    if len(line) == 0:
        continue
    words = line.split()
    for word in words:
        print ('%s\t%s' % (word, 1))
