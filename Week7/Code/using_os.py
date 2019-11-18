#!/usr/bin/env python3

"""Python 2 practical using subprocess.os"""

__appname__ = 'using_os.py'
__author__ = 'Wenhua Zhou (wz2812@ic.ac.uk)'
__version__ = '0.0.1'



# Use the subprocess.os module to get a list of files and directories 
# in your ubuntu home directory
# Hint: look in subprocess.os and/or subprocess.os.path and/or 
# subprocess.os.walk for helpful functions

import subprocess

#################################
#~Get a list of files and 
#~directories in your home/ that start with an uppercase 'C'

# Type your code here:

# Get the user's home directory.
home = subprocess.os.path.expanduser("~")

# Create a list to store the results.
FilesDirsStartingWithC = []

# Use a for loop to walk through the home directory.
for (dir, subdir, files) in subprocess.os.walk(home):
    for i in subdir:
        if i[0] == 'C':
            FilesDirsStartingWithC.append(i)
    for j in files:
        if j[0] == 'C':
            FilesDirsStartingWithC.append(j)
  
#################################
# Get files and directories in your home/ that start with either an 
# upper or lower case 'C'

# Type your code here:

# Get the user's home directory.
home = subprocess.os.path.expanduser("~")

# Create a list to store the results.
FilesDirsStartingWithCorc = []

# Use a for loop to walk through the home directory.
for (dir, subdir, files) in subprocess.os.walk(home):
    for i in subdir:
        if (i[0] == 'C') or (i[0] == 'c') :
            FilesDirsStartingWithCorc.append(i)
    for j in files:
        if (j[0] == 'C') or (j[0] == 'c'):
            FilesDirsStartingWithCorc.append(j)


#################################
# Get only directories in your home/ that start with either an upper or 
#~lower case 'C' 

# Type your code here:
# Get the user's home directory.
home = subprocess.os.path.expanduser("~")

# Create a list to store the results.
FilesDirsStartingWithCorc = []

# Use a for loop to walk through the home directory.
for (dir, subdir, files) in subprocess.os.walk(home):
    for i in subdir:
        if (i[0] == 'C') or (i[0] == 'c') :
            FilesDirsStartingWithCorc.append(i)