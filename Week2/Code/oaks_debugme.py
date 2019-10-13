import csv
import sys
import doctest # Import the doctest module

#Define function
def is_an_oak(name):
    """ Returns True if name is starts with 'quercus' 
    Test if function is working.

    >>> is_an_oak('Fagus sylvatica')
    False

    >>> is_an_oak('Quercus')
    True
   
    >>> is_an_oak('Quercus cerris')
    False

    >>> is_an_oak('Quercus12313582345')
    False

    """
    # The script is using .startwith, so the genus with name starts with 'quercus'
    # but now actually 'Quercus' will also be consider as a oak (e.g Quercus12345)
    # return name.lower().startswith('quercus,') # misspelling here in first version
    return bool(name.lower() == 'quercus')
    # since the name we need will return the first genus only from main(argv)
    # we can filter that only genus named 'quercus' will be recorded as an oak

def main(argv): 
    f = open('../Data/TestOaksData.csv','r')
    g = open('../Data/JustOaksData.csv','w')
    taxa = csv.reader(f)
    csvwrite = csv.writer(g)
    headers = next(taxa, None) # skip the header
    if headers:
        csvwrite.writerow(headers) # write header into output file in there is a header
    oaks = set()
    for row in taxa:
        print(row)
        print ("The genus is: ") 
        print(row[0] + '\n')
        # import ipdb; ipdb.set_trace()
        if is_an_oak(row[0]): # we are only use the first colomn genus to compare
            print('FOUND AN OAK!\n')
            csvwrite.writerow([row[0], row[1]])    

    return 0
    
if (__name__ == "__main__"):
    status = main(sys.argv)
    doctest.testmod()   # To run with embedded tests