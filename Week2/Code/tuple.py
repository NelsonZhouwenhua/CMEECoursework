#!/usr/bin/env python3

"""Python practical
print out tuples in separate lines
"""

__appname__ = 'tuple.py'
__author__ = 'Wenhua Zhou (wz2812@ic.ac.uk)'
__version__ = '0.0.1'

birds = ( ('Passerculus sandwichensis','Savannah sparrow',18.7),
          ('Delichon urbica','House martin',19),
          ('Junco phaeonotus','Yellow-eyed junco',19.5),
          ('Junco hyemalis','Dark-eyed junco',19.6),
          ('Tachycineata bicolor','Tree swallow',20.2),
        )

# Birds is a tuple of tuples of length three: latin name, common name, mass.
# write a (short) script to print these on a separate line or output block by species 
# Hints: use the "print" command! You can use list comprehensions!

# use for loop or comprehension to print the tuple into separate lines
for i in birds:
    print ('('+ i[0] + ' , ' + i[1] + ' , ' + str(i[2]) +')'+ '\n') # for loop is used 
    # each line of elements are printed out with commas and newline character