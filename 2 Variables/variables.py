#!/usr/bin/python3
## All the variables in python are objects and every object has type, id and value.

def main():
    print('## checking simple variables and their attributes')
    n = 12
    print(type(n), n)

    f = 34.23
    print(type(f), f)

    print(f / 4)

    print(f // 4)

    print(round(f / 4), end = '\n\n')

    print('## type casting ##')
    a = int(23.33)
    print(type(a), a)

    b = float(324)
    print(type(b), b, end = '\n\n')

    print('## check immutability of objects ##')
    num = 3
    print('id of object {} is - '.format(num), id(num))

    num = 4
    print('after changing value of object to {}, id changed to {}'.format(num, id(num)))

    num = 3
    print('restored value of object to original value {}, now id is {}'.format(num, id(num)), end = '\n\n')

if __name__ == '__main__' : main()
