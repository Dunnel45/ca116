#!/usr/bin/env python

a = []

s = raw_input()
while s != "end":
    t = int(s)
    a.append(t)
    s = raw_input()

i = 0
lowest = 0
while i < len(a):
    if a[i] < a[lowest]:
        lowest = i
    i = i + 1
print lowest
