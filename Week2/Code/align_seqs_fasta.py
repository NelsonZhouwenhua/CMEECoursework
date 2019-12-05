#!/usr/bin/env python3

"""Python Practical: Align DNA sequences
convert from the align_seqs.py but define a function to read sequence in fasta files
change output as best score only since sequence are too long to compare
but it can also find the best alignment and score
"""

__appname__ = 'align_seqs_fasta.py'
__author__ = 'Wenhua Zhou (wz2812@ic.ac.uk)'
__version__ = '0.0.1'

import sys

# define a function to read two sequences from separate fasta files 
def read_fasta(f):
    """ function to read sequence from two fasta files """
    seq = []
    # forloop through the lines to output the sequence only
    for line in f:
        if not line.startswith(">"):
            seq.append(line.replace('\n','')) # remove newline characters
    combine_seq = ''.join(seq) # combine the list together to a sequence
    f.close()
    return(combine_seq)

# import two fasta files from command line
if len(sys.argv) == 3:
    f1 = open(sys.argv[1])
    f2 = open(sys.argv[2])
elif len(sys.argv) == 1: # if no input is given
    f1 = open('../../Week1/Data/407228326.fasta')
    f2 = open('../../Week1/Data/407228412.fasta')

# use read_fasta to load as sequence
seq1 = read_fasta(f1)
seq2 = read_fasta(f2)

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
    """ function to compute the score """
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
    # not necessary to print these in the functions if we only want the results
    # print("." * startpoint + matched)           
    # print("." * startpoint + s2)
    # print(s1)
    # print(score) 
    # print(" ")

    return score


# now try to find the best match (highest score) for the two sequences
my_best_align = None
my_best_score = -1

for i in range(l1): # Note that you just take the last alignment with the highest score
    z = calculate_score(s1, s2, l1, l2, i)
    if z > my_best_score:
        my_best_align = "." * i + s2 # think about what this is doing!
        my_best_score = z 

# no need to print best alignment and s1 cause they are too long!
# print(my_best_align)
# print(s1)

# print best score only is good enough
print("Best score:", my_best_score)
