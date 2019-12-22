#!/usr/bin/env python

integers = []

line = raw_input()
while line != "end":
    integers.append(int(line))
    line = raw_input()

n = input()
i = 0
while i < len(integers):
    print integers[i] + n
    i = i + 1
