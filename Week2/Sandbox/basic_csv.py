import csv

# Read a file containing:
# 'Species','Infraorder','Family','Distribution','Body mass male (Kg)'
f = open('/home/nelson/Documents/CMEECoursework/Week2/Data/testcsv.csv','r')

csvread = csv.reader(f)
temp = []
for row in csvread:
    temp.append(tuple(row))
    print(row)
    print("The species is", row[0])

f.close()

# write a file containing only species name and Body mass
f = open('/home/nelson/Documents/CMEECoursework/Week2/Data/testcsv.csv','r')
g = open('/home/nelson/Documents/CMEECoursework/Week2/Data/bodymass.csv','w')

csvread = csv.reader(f)
csvwrite = csv.writer(g)
for row in csvread:
    print(row)
    csvwrite.writerow([row[0], row[4]])

f.close()
g.close()
