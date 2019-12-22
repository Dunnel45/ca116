#!/usr/bin/env python

n = input()

prev = 0
curr = 1

i = 0
while i < n:
    print prev
    old_curr = curr
    curr = prev + curr
    prev = old_curr
    i = i + 1
