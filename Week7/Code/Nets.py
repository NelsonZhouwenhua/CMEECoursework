#!/usr/bin/env python3

"""python 2 practical
Python version to draw networks from nets in R"""

__appname__ = 'Nets.py'
__author__ = 'Wenhua Zhou (wz2812@ic.ac.uk)'
__version__ = '0.0.1'


import networkx as nx
import scipy as sc
import matplotlib.pyplot as p
import csv
import numpy as np
import matplotlib.lines as mlines
# pip install pandas
# import pandas as pd

# 	ICL	UoR	CEH	ZSL	CEFAS	Nonacademic/CASE
# ICL	0	0	10	9	5	70
# UoR		0	12	0	2	76
# CEH			0	0	0	6
# ZSL				0# plot(net, edge.arrow.size=1, edge.curved=.1,
#      vertex.color="orange", vertex.frame.color="#555555",
#      vertex.label=V(net)$Type, vertex.label.color="black",
#      vertex.label.cex=.7) 	0	28
# CEFAS					0	0
# Nonacademic/CASE						0

# Read files containing:
f = open('../Data/QMEE_Net_Mat_edges.csv','r')
csvread = csv.reader(f)
links = []
for row in csvread:
    links.append(tuple(row))
f.close()

f = open('../Data/QMEE_Net_Mat_nodes.csv','r')
csvread = csv.reader(f)
nodes = []
for row in csvread:
    nodes.append(tuple(row))
f.close()

# generate networkx graph object
G = nx.DiGraph()

#Test plot
# plot(net, edge.arrow.size=1, edge.curved=.1,
#      vertex.color="orange", vertex.frame.color="#555555",
#      vertex.label=V(net)$Type, vertex.label.color="black",
#      vertex.label.cex=.7) 

# link to node one 
node_net = [x[0] for x in nodes[1:]]
nodesize = np.asarray([x[2] for x in nodes[1:]], dtype=np.float32)*50
linklist = [['ICL','CEH'],['ICL','ZSL'],['ICL','CEFAS'],['ICL','NonAc'],['UoR','CEH'],['UoR','CEFAS'],['UoR','NonAc'],['CEH','NonAc'],['ZSL','NonAc']]
linka = [x[0] for x in linklist]
linkb = [x[1] for x in linklist]
edgelist = list(zip(linka + linkb,linkb + linka))
# pos = nx.circular_layout(node_net)
# pos = nx.bipartite_layout(node_net)
# pos = nx.kamada_kawai_layout(node_net)
# pos = nx.random_layout(node_net)
# pos = nx.rescale_layout(node_net)
# pos = nx.shell_layout(node_net)
# pos = nx.spring_layout(node_net)
# pos = nx.spectral_layout(node_net)
# pos = nx.planar_layout(node_net)
pos = nx.fruchterman_reingold_layout(node_net)
# pos = nx.spiral_layout(node_net)

G.add_nodes_from(node_net)
G.add_edges_from(tuple(edgelist)) 

edgewidth = [10,9,5,70,12,2,76,6,28]
edgewidth = [1 + float(i)/10 for i in edgewidth]

# # Generate colors based on partner type:
# colrs <- c("green", "red", "blue")
# V(net)$color <- colrs[nodes$Type]

# # Set node size based on Number of PIs:
# # V(net)$size <- V(net)$Pis*0.9

# V(net)$size <- 50

# # Set edge width based on weight (PhD Students):
# E(net)$width <- E(net)$weight

# #change arrow size and edge color:
# E(net)$arrow.size <- 1
# E(net)$edge.color <- "gray80"

# E(net)$width <- 1+E(net)$weight/10

# open figure object
f1 = p.figure()
nx.draw_networkx(G, pos, node_size = nodesize, edge_color= 'grey' , width= edgewidth + edgewidth, node_color = ['b','b','g','g','g','r'])
colors = ['blue','green','red']
legend = [mlines.Line2D([], [], color=c, marker='o', linestyle='None', markersize=10) for c in colors]
labels = ['University','Hosting Partner','Non-hosting Partner']
p.legend(legend,labels, bbox_to_anchor = (0.6,0.6))

f1.savefig('../Results/QMEENet_py.svg') #Save figure
