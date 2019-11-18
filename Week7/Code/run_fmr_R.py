#!/usr/bin/env python3

"""Python 2 practical
running R script fmr.R on python"""

__appname__ = 'run_fmr_R.py'
__author__ = 'Wenhua Zhou (wz2812@ic.ac.uk)'
__version__ = '0.0.1'

import subprocess

# run fmr.R
subprocess.Popen("Rscript --verbose fmr.R" , shell= True).wait()
