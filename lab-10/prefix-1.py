#!/usr/bin/env python

if __name__ == "__main__":
    a = ["mountain", "montagne", "mont", "mo", "montages", "zebra", "monthly"]
    s = "mont"

i = 0
while i < len(a):
    m = a[i]
    m = m[:len(s)]
    if m == s:
        print a[i]
    i = i + 1
