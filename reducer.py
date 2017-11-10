#!/usr/bin/env python

import sys

def getr(x):
    temp = x + 1
    i = 0
    while True:
        i += 1
        if temp % 2:
            return i
        else:
            temp /= 2

cur_stream = None
cur_sha = None

for line in sys.stdin:
    substream, shacode = line.split()
    substream = int(substream)
    shacode = int(shacode)
    if substream == cur_stream:
        cur_sha = max(shacode, cur_sha)
    else:
        if cur_stream:
            print "{0}\t{1}".format(cur_stream, cur_sha)
        cur_stream = substream
        cur_sha = shacode
print "{0}\t{1}".format(cur_stream, cur_sha)
