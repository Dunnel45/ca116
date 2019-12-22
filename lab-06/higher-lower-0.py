#!/usr/bin/env python

n = input()

while n != 0:  
    n2 = input()
    if n == n2:
        print "equal"
    elif n < n2:
        print "higher"
    else:
        print "lower"
    n = input()
