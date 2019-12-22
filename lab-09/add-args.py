#!/usr/bin/env python

import sys
args = sys.argv[1:]

n = 0
i = 0
while i < len(args):
    v = int(args[i])
    n = v + n
    i = i + 1

print n
