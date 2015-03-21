#!/usr/bin/python3
# This program shows how to pass arguments to a function
# arguments could be simple variable, touple or keyword arguments

def main():
    passParams(1, 2, 3, 4, 5, 6, one = 1, two = 2, three = 3)

def passParams(first, second, third, *vtouple, **kwargs):
    print(first, second, third, vtouple, kwargs)

    for ar in kwargs: print(ar, ' -> ', kwargs[ar])

if __name__ == "__main__" : main()
