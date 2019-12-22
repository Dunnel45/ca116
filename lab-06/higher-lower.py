#!/usr/bin/env python

n = input()

i = 0
while i < 5:
    n2 = input()
    if n == n2:
        print "equal"
    elif n < n2:
        print "higher"
    else:
        print "lower"
    n = n2
    i = i + 1
