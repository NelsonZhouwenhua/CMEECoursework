#!/usr/bin/env python3

"""Differentiation and plot of LV model"""

__appname__ = 'LV1.py'
__author__ = 'Wenhua Zhou (wz2812@ic.ac.uk)'
__version__ = '0.0.1'

import scipy as sc
import matplotlib.pylab as p
import scipy.integrate as integrate

def dCR_dt(pops, t=0):

    R = pops[0]
    C = pops[1]
    dRdt = r * R - a * R * C 
    dCdt = -z * C + e * a * R * C
    
    return sc.array([dRdt, dCdt])

r = 1.
a = 0.1 
z = 1.5
e = 0.75
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
p.xlabel('Time', fontsize = 5)
p.ylabel('Population density')
p.title('Consumer-Resource population dynamics')
#p.show() not to display the figure

# f1.savefig('../Results/LV_model.pdf') #Save figure

# open figure object
# f2 = p.figure()

# Plot
p.subplot(2,1,2)
p.plot(pops[:,0], pops[:,1]  , 'r-')
p.grid()
# p.legend(loc='best')
p.xlabel('Resource density')
p.ylabel('Consumer density')
# p.show() #not to display the figure

f1.savefig('../Results/LV_model.pdf') #Save figure