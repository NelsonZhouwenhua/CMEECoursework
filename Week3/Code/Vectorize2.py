#!/usr/bin/env python3

"""python version of Vectorize2.R, 
compute the computational speed between python and R"""

__appname__ = 'Vectorize2.py'
__author__ = 'Wenhua Zhou (wz2812@ic.ac.uk)'
__version__ = '0.0.1'

import sys
import random
import numpy
import timeit

def Stochrick(p0 = [random.uniform(0.5,1.5) for i in range(1000)], r = 1.2, K = 1, sigma = 0.2, numyears = 100):
    """Stochastic Ricker equation model, python edition"""
    N = numpy.zeros((numyears,len(p0))) # initialize
    N[1] = p0

    for i in range(len(p0)): # loop through the population
        for j in range(2,numyears):  # loop through years  
            N[j][i] = N[j-1][i] * numpy.exp(r * (1 - N[j-1][i]) + numpy.random.normal(scale = 0.2)) # use function in numpy to replace rnorm
    return(N)

def Stochrickvect(p0 = [random.uniform(0.5,1.5) for i in range(1000)], r = 1.2, K = 1, sigma = 0.2, numyears = 100):
    """Stochastic Ricker vectorized model, python edition, use list comprehension instead"""
    N = numpy.zeros((numyears,len(p0))) # initialize
    N[1] = p0
    
    # use one loop only
    for j in range(2,numyears):
        # use list comprehension instead of loop
        N[j] = [(N[j-1][i] * numpy.exp(r * (1 - N[j-1][i]) + numpy.random.normal(scale = 0.2))) for i in range(len(p0))] # use function in numpy to replace rnorm
    return(N)

def main(argv):
    """calculate the time taken use for loop and list comprehension"""
    start = timeit.default_timer() # start timing
    Stochrick() # use for loop function to calculate matrix
    stop = timeit.default_timer() # stop timing
    print('Time taken Ricker function using loops: ' + str(stop - start) +'s') # print the time difference 

    start = timeit.default_timer() # start timing
    Stochrickvect() # use list comprehension to calculate matrix
    # stop = timeit.default_timer() # stop timing
    print('Time taken for Ricker function using list comprehension: ' + str(stop - start) + 's') # print the time difference    

    return 0

if __name__ == "__main__": 
    status = main(sys.argv)
    sys.exit(status)