Week 2 summary

Author: Wenhua Zhou(wz2812@ic.ac.uk)

Date: 7/10~~13/10

Chapter covered: Biological Computing in Python 1 

Status: chapter covered and practicals done

###############################################################

Chapter 5: Biological Computing in Python 1

Code directory:

basic_io1.py
# python script to open a file and print lines(skip blank lines) in that file

basic_io2.py
# python script to save the elements into a file

basic_io3.py
# python script to store the object for later use and then load into

basic_io.py
# combination of the previous 3 scripts

basic_csv.py
# python script to read data and use it from csv files

cfexercises1.py
# originally a python script containing some functions
# after practicals work, it is modified and the output is evaluated automatically
# the input variables are:
# print(foo_1(10))
# print(foo_2(10,2))
# print(foo_3(30,20,10))
# print(foo_4(10))
# print(foo_5(10))
# print(foo_6(10))

loops.py
# a python script including for loops and while loops examples

cfexercises2.py
# a python script including some loops
# after practicals work, it is modified 
# all loops are changed into functions with input variables set to be original default 

oaks.py
# a python script using for loops and list comprehensions to deal with data

scope.py 
# a python script using examples to introduce properties of global variables

boilerplate.py
# a python script containing an example template for python programs

using_name.py
# a python script to illustrate if a script is run by itself or not

control_flow.py
# a example python script using various control flow tools within a python program

lc1.py
# work for practicals, create lists by for loops and line comprehensions

lc2.py
# work for practicals, create filtered lists by for loops and line comprehensions

dictionary.py
# work for practicals, populate a dictionary with different sets of taxa

tuple.py
# work for practicals, print out tuples in separate lines

test_control_flow
# a python script to test even_or_odd function in control_flow.py 

debugme.py
# a python script with bug to test debugger

align_seqs.py
# work for practical of align DNA sequences
# convert from the original align_seqs.py from repository
# now read csv files including the two example sequences originally given
# and find the best alignment and score

align_seqs_fasta.py
# work for practical of align DNA sequences
# convert from the align_seqs.py but define a function to read sequence in fasta files
# change output as best score only since sequence are too long to compare
# but it can also find the best alignment and score

align_seqs_better.py
# work for practical of align DNA sequences
# change the output so that all best alignments are recorded
# use pickle to record the best alignments into .p file and load again

oaks_debugme.py
# work for missing oaks problem from last practical
# fix the bug of misspelling
# write a doctest to make sure of no bug
# rewrite the is_an_oak function so that only 'quercus' not any genus startswith 'quercus' will be considered as an oak
# remove header when read csv and put header into out put file

Data directory:

testcsv.csv
# test csv file for basic_csv.py script, including sets of data with different species

bodymass.csv
# csv written that only contains species name and body mass

DNA_seq.csv
# csv file with example DNA sequence input for aligning DNA sequences

TestOaksData.csv
# csv data of oaks downloaded

JustOaksData.csv
# output file of oaks_debugme.py from practical