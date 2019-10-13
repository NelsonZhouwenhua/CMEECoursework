#!/usr/bin/env python3

__author__ = 'Wenhua Zhou (wz2812@ic.ac.uk)'
__version__ = '0.0.1'

import sys

# What does each of foo_x do? 
def foo_1(x):
    return x ** 0.5 # calculate root of input variable

def foo_2(x, y):
    if x > y:
        return x
    return y # choose the larger output of two input variables

def foo_3(x, y, z):
    if x > y:
        tmp = y
        y = x
        x = tmp
    if y > z:
        tmp = z
        z = y
        y = tmp
    return [x, y, z] # compare 3 different inputs
# if first is larger than second, swap positions for them
# if second is larger than third, swap positions for them

def foo_4(x):
    result = 1
    for i in range(1, x + 1):
        result = result * i
    return result # calculate the factorial of input

def foo_5(x): # a recursive function that calculates the factorial of x
    if x == 1:
        return 1
    return x * foo_5(x - 1) 

def foo_6(x): # Calculate the factorial of x in a different way
    facto = 1
    while x >= 1:
        facto = facto * x
        x = x - 1
    return facto

def main(argv):
    print(foo_1(10))
    print(foo_2(10,2))
    print(foo_3(30,20,10))
    print(foo_4(10))
    print(foo_5(10))
    print(foo_6(10))
    return 0

if __name__ == '__main__':
    status = main(sys.argv)
    sys.exit(status)