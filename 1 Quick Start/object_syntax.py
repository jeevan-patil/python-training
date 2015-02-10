#!/usr/bin/python3
## everything in python is an object, variables functions and even code.
## every object has type, id and value.

class Egg:
    def __init__(self, kind = 'Fried'):
        self.kind = kind

    def whatKind(self):
        return self.kind

def main():
    fried = Egg()
    scrambled = Egg('Scrambled')
    print(fried.whatKind())
    print(scrambled.whatKind())

if __name__ == '__main__' : main()
