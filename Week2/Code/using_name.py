#!/usr/bin/env python3

"""python script to illustrate if a script is run by itself or not"""

__appname__ = 'using_name.py'
__author__ = 'Wenhua Zhou (wz2812@ic.ac.uk)'
__version__ = '0.0.1'

#!/usr/bin/env python3
# Filename: using_name.py

if __name__ == '__main__':
    print('This program is being run by itself')
else:
    print('I am being imported from another module')