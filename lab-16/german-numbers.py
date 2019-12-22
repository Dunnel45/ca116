#!/usr/bin/env python

import sys
words = sys.stdin.readlines()

translation = {
    "one": "eins",
    "two": "zwei",
    "three": "drei",
    "four": "vier",
    "five": "funf",
    "six": "sechs",
    "seven": "sieben",
    "eight": "acht",
    "nine": "neun",
    "ten": "zehn",
}

i = 0
while i < len(words):
    word = words[i].strip()
    if word in translation:
        sys.stdout.write(translation[word] + "\n")
    i = i + 1
