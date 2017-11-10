#!/usr/bin/env python

import sys
import hashlib
import random

def getr(x):
    temp = x + 1
    i = 0
    while 1:
        i += 1
        if temp % 2:
            return i
        else:
            temp /= 2

m = 424

for line in sys.stdin:
    for word in line.split():
        salt = str(int(hashlib.md5(word).hexdigest(), 16) % m)
        print "{0}\t{1}".format(salt, getr(int(hashlib.sha1(word+salt).hexdigest(), 16)))
