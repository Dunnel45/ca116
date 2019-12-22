#!/usr/bin/env python

total = 0

i = 0
while i < 5:
    n = input()
    if n < 0:
        total = total + (-1) * n
    else:
        total = total + n
    i = i + 1
print total
