#!/usr/bin/env python

n = input()
total = 0

while n != 0:
    if n < 0:
        total = total + (-1) * n
    else:
        total = total + n
    n = input()
print total
