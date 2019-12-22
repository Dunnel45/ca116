#!/usr/bin/env python

import sys
words = sys.stdin.readlines()

not_seen = {}

i = 0
while i < len(words):
    word = words[i].strip()
    if word not in not_seen:
        not_seen[word] = True
    else:
        not_seen[word] = False
    i = i + 1

while not_seen[word] == False:
    print "snap" + ":" + not_seen[word]
