#!/usr/bin/env python3

"""Python 2 practical"""

__appname__ = 'LV3.py'
__author__ = 'Wenhua Zhou (wz2812@ic.ac.uk)'
__version__ = '0.0.1'

import sys
import scipy as sc
import matplotlib.pylab as p
import scipy.integrate as integrate
import numpy as np

# def dCR_dt(pops, t=0):

#     R = pops[0]
#     C = pops[1]
#     dRdt = r * R * (1 - R/K) - a * R * C 
#     dCdt = -z * C + e * a * R * C
    
#     return sc.array([dRdt, dCdt])

# set default value
r = 1.
a = 0.1
z = 1.5
e = 0.75
K = 30

# take arguments from the command line
if len(sys.argv) > 1:
    r = sys.argv[1]
if len(sys.argv) > 2:
    a = sys.argv[2]
if len(sys.argv) > 3: 
    z = sys.argv[3]
if len(sys.argv) > 4:
    e = sys.argv[4] 
if len(sys.argv) > 5:
    K = sys.argv[5]
t = sc.linspace(0, 15, 1000)
R = 10
C = 5 
pops = np.zeros((len(t),2))
for i in range(len(t)):
    R1 = R * (1 + r * (1 - R/K) - a * C)
    C1 = C * (1 - z + e * a * R)
    R = R1
    C = C1
    pops[i,:] = [R1,C1]

# open figure object
f1 = p.figure()

p.subplot(2,1,1)
p.plot(t, pops[:,0], 'g-', label='Resource density') # Plot
p.plot(t, pops[:,1]  , 'b-', label='Consumer density')
p.grid()
p.legend(loc='best')
p.xlabel('')
p.ylabel('Population density')
# make title include parameters
title = 'r = ' + str(r) + ', a = ' + str(a) + ', z = ' + str(z) + ', e = ' + str(e) + ', K = ' + str(K) + ', t = (' + str(int(min(t))) +','+ str(int(max(t)))+')' 
p.title(title)
#p.show() not to display the figure

# Plot
p.subplot(2,1,2)
p.plot(pops[:,0], pops[:,1]  , 'r-')
p.grid()
# p.legend(loc='best')
p.xlabel('Resource density')
p.ylabel('Consumer density')
# p.show() #not to display the figure

f1.savefig('../Results/LV3_model.pdf') #Save figure

# print population values 
print(pops[-1,:])