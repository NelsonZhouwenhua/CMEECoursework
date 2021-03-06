#!/usr/bin/env python3

"""python 2 practicals for regex"""

__appname__ = 'blackbirds.py'
__author__ = 'Wenhua Zhou (wz2812@ic.ac.uk)'
__version__ = '0.0.1'

import re

# Read the file (using a different, more python 3 way, just for fun!)
with open('../Data/blackbirds.txt', 'r') as f:
    text = f.read()

# replace \t's and \n's with a spaces:
text = text.replace('\t',' ')
text = text.replace('\n','?')
# You may want to make other changes to the text. 


# In particular, note that there are "strange characters" (these are accents and
# non-ascii symbols) because we don't care for them, first transform to ASCII:

text = text.encode('ascii', 'ignore') # first encode into ascii bytes
text = text.decode('ascii', 'ignore') # Now decode back to string

# Now extend this script so that it captures the Kingdom, Phylum and Species
# name for each species and prints it out to screen neatly.
found_kingdom = re.findall(r"Kingdom\s*Animalia\s+\w+,\s+\w+,\s+\w+", text)
found_phylum = re.findall(r"Phylum\s+Chordata\s+\w+,\s+\w+,\s+\w+", text)
found_species = re.findall(r"Species\s+\w+\s+\w+\s+\([A-Z\w\s]+,\s+\d+\)[\w\s\-\'\,]+", text)
for i in range(len(found_kingdom)):
    print(found_kingdom[i])
    print(found_phylum[i])
    print(found_species[i])
    print('\n')

# Hint: you may want to use re.findall(my_reg, text)... Keep in mind that there
# are multiple ways to skin this cat! Your solution could involve multiple
# regular expression calls (easier!), or a single one (harder!)