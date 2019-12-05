#!/usr/bin/env python3

"""python script to open a file and print lines(skip blank lines) in that file"""

__appname__ = 'basic_io1.py'
__author__ = 'Wenhua Zhou (wz2812@ic.ac.uk)'

#############################
# FILE INPUT
#############################
# Open a file for reading
f = open('../Sandbox/test.txt', 'r')
# use "implicit" for loop:
# if the object is a file, python will cycle over lines
for line in f:
    print(line)

# close the file
f.close()

# Same example, skip blank lines
f = open('../Sandbox/test.txt', 'r')
for line in f:
    if len(line.strip()) > 0:
        print(line)

f.close()