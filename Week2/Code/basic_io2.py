"""python script to save the elements into a file"""

__appname__ = 'basic_io2.py'
__author__ = 'Wenhua Zhou (wz2812@ic.ac.uk)'

#############################
# FILE OUTPUT
#############################
# Save the elements of a list to a file
list_to_save = range(100)

f = open('../Sandbox/testout.txt','w')
for i in list_to_save:
    f.write(str(i) + '\n') ## Add a new line at the end
f.close()