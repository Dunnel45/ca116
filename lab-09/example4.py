#!/usr/bin/env python

not_seen = []

s = raw_input()
while s != "end":
    if s not in not_seen:
        not_seen.append(s)
    s = raw_input()

i = 0
while i < len(not_seen):
    print not_seen[i]
    i = i + 1
