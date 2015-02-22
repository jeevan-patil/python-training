#!/usr/bin/python3

# Solution for a simple problem on hackerearth.com, my first solution in python.
# https://www.hackerearth.com/problem/algorithm/karan-and-even-numbers-1/description/

import sys

fh = open('../input/numbers.txt')
for line in fh:
    if int(line) == -1:
        break
    if -1 <= int(line) <= 1000000000:
        if int(line) % 2 == 0:
            print(line.strip())
