#!/usr/bin/env python3

"""Python 2 practical
Draw food networks"""

__appname__ = 'DrawFW.py'
__author__ = 'Wenhua Zhou (wz2812@ic.ac.uk)'
__version__ = '0.0.1'

import networkx as nx
import scipy as sc
import matplotlib.pyplot as p

def GenRdmAdjList(N = 2, C = 0.5):
    """ 
    """
    Ids = range(N)
    ALst = []
    for i in Ids:
        if sc.random.uniform(0,1,1) < C:
            Lnk = sc.random.choice(Ids,2).tolist()
            if Lnk[0] != Lnk[1]: #avoid self (e.g., cannibalistic) loops
                ALst.append(Lnk)
    return ALst

MaxN = 30
C = 0.75
AdjL = sc.array(GenRdmAdjList(MaxN, C))
Sps = sc.unique(AdjL)
SizRan = ([-10,10]) #use log10 scale
Sizs = sc.random.uniform(SizRan[0],SizRan[1],MaxN)
pos = nx.circular_layout(Sps)
G = nx.Graph()
G.add_nodes_from(Sps)
G.add_edges_from(tuple(AdjL))
NodSizs= 1000 * (Sizs-min(Sizs))/(max(Sizs)-min(Sizs)) 

# open figure object
f1 = p.figure()
nx.draw_networkx(G, pos, node_size = NodSizs)

f1.savefig('../Results/FW.pdf') #Save figure
