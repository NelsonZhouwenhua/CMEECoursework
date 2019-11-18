#!/usr/bin/env python3

"""Python 2 practical"""

__appname__ = 'LV2.py'
__author__ = 'Wenhua Zhou (wz2812@ic.ac.uk)'
__version__ = '0.0.1'

import sys
import scipy as sc
import matplotlib.pylab as p
import scipy.integrate as integrate

def dCR_dt(pops, t=0):

    R = pops[0]
    C = pops[1]
    dRdt = r * R * (1 - R/K) - a * R * C 
    dCdt = -z * C + e * a * R * C
    
    return sc.array([dRdt, dCdt])

# set default value
r = 1.
a = 0.1
z = 1.5
e = 0.75
K = 2000

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
R0 = 10
C0 = 5 
RC0 = sc.array([R0, C0])
pops, infodict = integrate.odeint(dCR_dt, RC0, t, full_output=True)

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

f1.savefig('../Results/LV2_model.pdf') #Save figure

# print population values 
print(pops[-1,:])