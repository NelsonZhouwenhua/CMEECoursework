#!/usr/bin/env python3

""" R practical:
The python version of get_TreeHeight.R, get the tree height and write
as a csv file run by run_get_TreeHeight.sh"""
__author__ = 'Wenhua Zhou (wz2812@ic.ac.uk)'
__version__ = '0.0.1'


import csv
import sys
import numpy

# read the csv file first
f = open(sys.argv[1],'r')
csvread = csv.reader(f)

# put data into a tuple
tree = []
for row in csvread:
    tree.append(tuple(row))

f.close() 

# define a function to calculate tree height
def calculate_height(degrees, distance):
    """ function to calculate tree height """
    radians = degrees * numpy.pi/180
    height = distance * numpy.tan(radians)
    print("Tree height is:" + str(height))
    return(height)

# choose the degrees and distance in tree data and convert to float number
degrees = numpy.asarray([float(i) for i in [x[2] for x in tree][1:]])
distance = numpy.asarray([float(i) for i in [x[1] for x in tree][1:]])
# calculates all tree heights for trees in the data
TreeHeight = calculate_height(degrees, distance)

# append heights into tuples
tree[0] = [tree[0][0], tree[0][2], tree[0][1], 'Tree.Height.m']
for i in range(1,len(TreeHeight)):
    tree[i] = [tree[i][0], tree[i][2], tree[i][1], TreeHeight[i-1]]

# write in csv file
g = open('../Results/treeheight_py.csv','w')
csvwrite = csv.writer(g)
for row in tree:
    csvwrite.writerow(row)

g.close()