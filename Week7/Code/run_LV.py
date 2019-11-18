#!/usr/bin/env python3

"""scripts to run LV1 and LV2 and compare speed"""

__appname__ = 'run_LV.py'
__author__ = 'Wenhua Zhou (wz2812@ic.ac.uk)'
__version__ = '0.0.1'

import os

os.system('python3 -m cProfile LV1.py')
os.system('python3 -m cProfile LV2.py 1 0.2 1.5 0.75 1000')
os.system('python3 -m cProfile LV3.py 1 0.2 1.5 0.75 1000')
