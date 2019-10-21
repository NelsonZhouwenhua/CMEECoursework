#!/usr/bin/env python3

"""python script with bug to test debugger"""

__appname__ = 'debugme.py'
__author__ = 'Wenhua Zhou (wz2812@ic.ac.uk)'
__version__ = '0.0.1'

def createabug(x):
    y = x**4
    z = 0.
    import ipdb; ipdb.set_trace()
    y = y/z
    return y

createabug(25)