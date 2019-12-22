#!/usr/bin/env python

import sys
a = sys.stdin.readlines()
numbers = {}

with open("translation.txt") as f:
    words = f.readlines()

    i = 0
    while i < len(words):
        tokens = words[i].split()
        english = tokens[0]
        german = tokens[1]
        numbers[english] = german
        i = i + 1

i = 0
while i < len(a):
    word = a[i].strip()
    if word in numbers:
        print numbers[word]
    i = i + 1
