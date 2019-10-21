#!/usr/bin/env python3

"""Python practical:
populate a dictionary with different sets of taxa
"""

__appname__ = 'dictionary.py'
__author__ = 'Wenhua Zhou (wz2812@ic.ac.uk)'
__version__ = '0.0.1'

taxa = [ ('Myotis lucifugus','Chiroptera'),
         ('Gerbillus henleyi','Rodentia',),
         ('Peromyscus crinitus', 'Rodentia'),
         ('Mus domesticus', 'Rodentia'),
         ('Cleithrionomys rutilus', 'Rodentia'),
         ('Microgale dobsoni', 'Afrosoricida'),
         ('Microgale talazaci', 'Afrosoricida'),
         ('Lyacon pictus', 'Carnivora'),
         ('Arctocephalus gazella', 'Carnivora'),
         ('Canis lupus', 'Carnivora'),
        ]

# Write a short python script to populate a dictionary called taxa_dic 
# derived from  taxa so that it maps order names to sets of taxa. 
# E.g. 'Chiroptera' : set(['Myotis lucifugus']) etc. 

# create the empty string
taxa_dic = {}
# put the sets in taxa into different sets
for i in taxa:
        taxa_dic[i[1]] = set()
# maps the order names to those sets
for i in taxa:
        taxa_dic[i[1]].add(i[0])
print(taxa_dic)        
