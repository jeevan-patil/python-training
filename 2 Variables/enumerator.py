#!/usr/bin/python3

def main():
    print('iterating over a string:')
    s = 'this is a statement'
    for index, char in enumerate(s):
        print(index, char)

    print('\n\nReading file now:')

    fh = open('../input/input.txt')
    for index, line in enumerate(fh.readlines()):
        print('index is - {}'.format(index), 'and line content is - {}'.format(line), end = '')

if __name__ == '__main__' : main()
