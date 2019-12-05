#!/usr/bin/env python3

"""python version of Vectorize1.R, 
compute the computational speed between python and R"""

__appname__ = 'Vectorize1.py'
__author__ = 'Wenhua Zhou (wz2812@ic.ac.uk)'
__version__ = '0.0.1'

import sys
import numpy # package for create matrix and sum
import timeit # package for calculating time

def SumAllElements(M):
    """sum by for loops"""
    TotalSum = 0
    for i in range(numpy.shape(M)[0]):
        for j in range(numpy.shape(M)[1]):    
            TotalSum += M[i][j]
    return(TotalSum)


def main(argv):
    """set a random matrix by numpy"""
    M = numpy.random.rand(1000,1000)

    """calculate the time taken use for loop and in-built function"""
    start = timeit.default_timer() # start timing
    SumAllElements(M) # calculate sum
    stop = timeit.default_timer() # stop timing
    print('Time taken for sum using loops: ' + str(stop - start) + 's') # print the time difference 
    
    start = timeit.default_timer() # start timing
    numpy.sum(M) # calculate sum
    stop = timeit.default_timer() # stop timing
    print('Time taken for sum using in-built function: ' + str(stop - start) + 's') # print the time difference    

    return 0

if __name__ == "__main__": 
    status = main(sys.argv)
    sys.exit(status)