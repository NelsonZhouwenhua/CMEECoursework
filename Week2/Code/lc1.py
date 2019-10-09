birds = ( ('Passerculus sandwichensis','Savannah sparrow',18.7),
          ('Delichon urbica','House martin',19),
          ('Junco phaeonotus','Yellow-eyed junco',19.5),
          ('Junco hyemalis','Dark-eyed junco',19.6),
          ('Tachycineata bicolor','Tree swallow',20.2),
         )

#(1) Write three separate list comprehensions that create three different
# lists containing the latin names, common names and mean body masses for
# each species in birds, respectively. 

# latin names
latin_com = [i[0] for i in birds]
print(latin_com)

# common names
common_com = [i[1] for i in birds]
print(common_com)

# mean body masses
masses_com = [i[2] for i in birds]
print(masses_com)

# (2) Now do the same using conventional loops (you can choose to do this 
# before 1 !). 

# latin names
latin_loops = []
for i in range(len(birds)):
    latin_loops.append(birds[i][0])
print(latin_loops)

# common names
common_loops = []
for i in range(len(birds)):
    common_loops.append(birds[i][1])
print(common_loops)

# mean body masses
masses_loops = []
for i in range(len(birds)):
    masses_loops.append(birds[i][2])
print(masses_loops)

