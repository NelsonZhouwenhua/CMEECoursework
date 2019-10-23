# R practicals
# take a csv file name from the command line
# output the same results as TreeHeight.R with different name


# read data from the command line
args <- commandArgs(trailingOnly = TRUE)

# load data from trees.csv
TreeData <- read.csv(args, header = TRUE)

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

# read name of the input file without extension and relative path
Name <- tools::file_path_sans_ext(basename(args))
# combine to get the output path name
OutputName <- paste("../Results/",Name,"_treeheights.csv",sep = "")

# save this new dataframe into TreeHts.csv file in Results directory
write.csv(TreeData, OutputName, row.names = FALSE) # ignore row names

