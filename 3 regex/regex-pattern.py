#!/usr/bin/python3

## 're' is regular expressions module library
import re

def main():
    fh = open('../input/everything-i-do.txt')
    pattern = re.compile('(i do | true)', re.IGNORECASE) ## re.I would also work

    for line in fh:
        if re.search(pattern, line):
            print(pattern.sub('###', line), end = '')

if __name__ == '__main__' : main()
