#!/usr/bin/env python3

__author__ = 'Wenhua Zhou(wz2812@ic.ac.uk)'
__version__ = '0.0.1'

import sys

# write functions for all these loops

# print a 'hello' when integer smaller than variable x can be divided by 3
def foo_1(x):
    for j in range(x):
        if j % 3 == 0:
            print('hello')

# print a 'hello' when integer smaller than variable x can be divided by 4 or 5
def foo_2(x):
    for j in range(x):
        if j % 5 == 3:
            print('hello')
        elif j % 4 == 3:
            print('hello')

# print a 'hello' each time and plus 3 for the variable z until z reaches 15
def foo_3(z):
    while z != 15:
        print('hello')
        z = z + 3

# add 1 to the variable z until z reaches 100,
# print 7 'hello's when z = 31, abd print 'hello' when z = 18
def foo_4(z):
    while z < 100:
        if z == 31:
            for k in range(7):
                print('hello')
        elif z == 18:
            print('hello')
        z = z + 1

# test arguments for the functions
def main(argv):
    foo_1(12) # print 4 'hello's
    foo_2(15) # print 5 'hello's
    foo_3(0) # print 5 'hello's
    foo_4(12) # print 8 'hello's
    return 0

if __name__ == "__main__":
    status = main(sys.argv)
    sys.exit(status)