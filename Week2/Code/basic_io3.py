#!/usr/bin/env python3

"""python script to store the object for later use and then load into"""

__appname__ = 'basic_io3.py'
__author__ = 'Wenhua Zhou (wz2812@ic.ac.uk)'


#############################
# STORING OBJECTS
#############################
# To save an object (even complex) for later use
my_dictionary = {"a key": 10, "another key": 11}

import pickle

f = open('../Sandbox/testp.p','wb') ## note the b: accept binary files
pickle.dump(my_dictionary, f)
f.close()

## Load the data again
f = open('../Sandbox/testp.p','rb')
another_dictionary = pickle.load(f)
f.close()

print(another_dictionary)