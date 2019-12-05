#!/usr/bin/env python3

"""Python Practical: Align DNA sequences
change the output so that all best alignments are recorded
use pickle to record the best alignments into .p file and load again
"""

__appname__ = 'align_seqs_better.py'
__author__ = 'Wenhua Zhou (wz2812@ic.ac.uk)'
__version__ = '0.0.1'

# load two sequences from the csv in data directory
import csv

f = open('../Data/DNA_seq.csv','r')

# read csv
csvread = csv.reader(f)
temp = []
for row in csvread:
    temp.append(tuple(row))
seq1 = temp[0][0] # put two sequences into seq1 and seq2
seq2 = temp[0][1]   

f.close()

# Assign the longer sequence s1, and the shorter to s2
# l1 is length of the longest, l2 that of the shortest

l1 = len(seq1)
l2 = len(seq2)
if l1 >= l2:
    s1 = seq1
    s2 = seq2
else:
    s1 = seq2
    s2 = seq1
    l1, l2 = l2, l1 # swap the two lengths

# A function that computes a score by returning the number of matches starting
# from arbitrary startpoint (chosen by user)
def calculate_score(s1, s2, l1, l2, startpoint):
    """A function that computes the score"""
    matched = "" # to hold string displaying alignements
    score = 0
    for i in range(l2):
        if (i + startpoint) < l1:
            if s1[i + startpoint] == s2[i]: # if the bases match
                matched = matched + "*"
                score = score + 1
            else:
                matched = matched + "-"

    # some formatted output
    print("." * startpoint + matched)           
    print("." * startpoint + s2)
    print(s1)
    print(score) 
    print(" ")

    return score

# Test the function with some example starting points:
# calculate_score(s1, s2, l1, l2, 0)
# calculate_score(s1, s2, l1, l2, 1)
# calculate_score(s1, s2, l1, l2, 5)

# now try to find the best match (highest score) for the two sequences
my_best_align = []
my_best_score = -1

import pickle
'''use pickle to record the best alignments into .p file and load again'''
for i in range(l1): # Note that you just take the last alignment with the highest score
    z = calculate_score(s1, s2, l1, l2, i)
    if z > my_best_score:
        my_best_align = [] # clean the previous alignments
        my_best_align.append("." * i + s2) # think about what this is doing!
        my_best_score = z 
    elif z == my_best_score:
        my_best_align.append("." * i + s2) # add another alignment if there is a tie

# print all the best alignments and the long sequence with the best score
print("My best alignments are:")
for i in my_best_align:
    print(i)
print("The long sequence:")
print(s1)
print("Best score:", my_best_score)

# put the best alignments into the results directory as best_align.p
f = open('../results/best_align.p','wb')
pickle.dump(my_best_align, f)
f.close()

## Load the data again
f = open('../results/best_align.p','rb')
best_align = pickle.load(f)
f.close()

print(best_align)