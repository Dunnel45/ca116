#!/usr/bin/env python

n = input()

if  (2 <= n) and (n % 2 == 0) and (n % 3 == 0) and (n % 5 ==0):
    print " not prime"
else:
    print "prime"
