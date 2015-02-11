#!/usr/bin/python3

## 're' is regular expressions module library
import re

def main():
    fh = open('../input/everything-i-do.txt')
    for line in fh.readlines():
        if re.search('(I do | true)', line):  ## these searches are case sensitive
            print(line, end = '')

if __name__ == '__main__' : main()
