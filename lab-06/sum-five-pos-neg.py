#!/usr/bin/env python

neg_total = 0
pos_total = 0

i = 0
while i < 5:
    n = input()
    if n < 0:
        neg_total = neg_total + n
    else:
        pos_total = pos_total + n
    i = i + 1
print neg_total, pos_total
