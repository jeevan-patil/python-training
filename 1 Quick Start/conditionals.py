#!/usr/bin/python3

def main():
    simpleConditions()
    print()
    shortHandConditions()

def simpleConditions():
    print('traditional if else conditions --->>>')
    a, b = 1, 1

    if a > b :
        print('a ({}) is greater than b ({}).'.format(a, b))
    elif b > a:
        print('a ({}) is less than b ({})'.format(a, b))
    else :
        print('They are equal.')

def shortHandConditions():
    print('shorthand if else conditions --->>>')
    a, b = 1, 2
    result = '{} less than {}'.format(a, b) if a < b else '{} not less than {}'.format(a, b)
    print(result)

if __name__ == '__main__' : main()
