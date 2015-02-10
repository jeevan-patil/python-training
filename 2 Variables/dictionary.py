#!/usr/bin/python3
## dictionary in python is very much anologous to maps in Java.

def main():
    ## this is a way to define dictionary
    data = { 1 : 'one', 2 : 'two', 3 : 'three', 4 : 'four', 5 : 'five' }
    for key in data:
        print(key, data[key])
    print('\n')

    print('Correct way to define dict is as shown below: ')

    ## creating dictionary using dict object, order of elements is not guarunteed though.
    months = dict(
        Jan = 1, Feb = 2, Mar = 3, Apr = 4, May = 5, Jun = 6,
        Jul = 7, Aug = 8, Sep = 9, Oct = 10, Nov = 11
    )

    ## You can insert elements in dictionary later since this is mutable object
    months['Dec'] = 12
    for mon in sorted(months.keys()):
        print(mon, months[mon])

if __name__ == '__main__' : main()
