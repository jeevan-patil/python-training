#!/usr/bin/python3

try:
    fh = open('input.txt')

    for line in fh.readlines():
        print(line, end = '')
except IOError as e:
    print('Exception occurred while reading file! {}'.format(e))
