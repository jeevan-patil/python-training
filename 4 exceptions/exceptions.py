#!/usr/bin/python3

## This program explains how to handle and throw exceptions.

def main():
    try:
        for line in readFile('../input/everything-i-do.txt'):
            print(line.strip())
    except IOError as io:
        print('File not found, ', io)
    except ValueError as ve:
        print(ve)
    except:
        print('Something went wrong.')

def readFile(fileName):
    if fileName.endswith('doc'):
        raise ValueError('File format not supported.')
    fh = open(fileName)
    return fh.readlines()

if __name__ == '__main__' : main()
