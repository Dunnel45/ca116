#!/usr/bin/env python

import sys
file_name = sys.argv[1]

with open(file_name, "r") as f:
    numbers = f.readlines()

with open(file_name, "w") as f:
    total = 0
    i = 0
    while i < len(numbers):
        total = total + int(numbers[i])
        i = i + 1

    total = str(total)
    sys.stdout.write(total + "\n")