# work for practicals
# originally is a function calculate the tree height
# now is modified to load data from trees.csv to calculate all tree heights in the data
# save the results into Results directory that contains
# both original data and the calculate tree height in the given format


# This function calculates heights of trees given distance of each tree 
# from its base and angle to its top, using  the trigonometric formula 
#
# height = distance * tan(radians)
#
# ARGUMENTS
# degrees:   The angle of elevation of tree
# distance:  The distance from base of tree (e.g., meters)
#
# OUTPUT
# The heights of the tree, same units as "distance"

# load data from trees.csv
TreeData <- read.csv("../Data/trees.csv", header = TRUE)

TreeHeight <- function(degrees, distance){
  radians <- degrees * pi / 180
  height <- distance * tan(radians)
  print(paste("Tree height is:", height))
  
  return (height)
}


# calculates all tree heights for trees in the data
TreeHt <- TreeHeight(TreeData[,3], TreeData[,2])

# write the tree heights into TreeData dataframe
TreeData[,"Tree.Height.m"] <- TreeHt

# swap columns of the dataframe to make it in the right format
TreeData <- TreeData[c("Species","Angle.degrees","Distance.m","Tree.Height.m")]

# save this new dataframe into TreeHts.csv file in Results directory
write.csv(TreeData, "../Results/TreeHts.csv", row.names = FALSE) # ignore row names

