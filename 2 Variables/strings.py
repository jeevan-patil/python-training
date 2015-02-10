#!/usr/bin/python3

def main():
    s = 'string using single quotes.'
    print(s)

    t = "string using double quotes."
    print(t)

    essay = '''\
    This allows to write text
    on multiple lines and lots of it :)
    '''
    print(essay, end = '\n\n')

    print('some string operations: ')
    string = 'sachin tendulkar'
    print('character at index 4 of string {} is - {}'.format(string, string[4]))
    print('all the characters from index 2 to 4 are - {}'.format(string[1:12]))


if __name__ == '__main__' : main()
