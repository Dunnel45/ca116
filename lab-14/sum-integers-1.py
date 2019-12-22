#!/usr/bin/env python

import sys

numbers = sys.stdin.readlines()
total = 0

i = 0
while i < len(numbers):
    total = total + int(numbers[i])
    i = i + 1

total = str(total)
sys.stdout.write(total + "\n")
