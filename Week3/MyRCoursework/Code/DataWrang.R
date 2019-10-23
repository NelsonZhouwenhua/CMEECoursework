# load the data in R
MyData <- as.matrix(read.csv("../Data/PoundHillData.csv",header = F,  stringsAsFactors = F))
MyMetaData <- read.csv("../Data/PoundHillMetaData.csv",header = T,  sep=";", stringsAsFactors = F)

# have a look at the metadata file
MyMetaData

# replace blanks with zeros
MyData[MyData == ""] = 0

# transpose the data
MyData <- t(MyData) 
head(MyData)

# check the column names
colnames(MyData) # this is NULL since MyData is a matrix

# create a temporary dataframe without the column names
TempData <- as.data.frame(MyData[-1,],stringsAsFactors = F) # do not convert columns to factor
head(TempData)

# assign the column names to the temporary dataframe
colnames(TempData) <- MyData[1,] # assign column names from original data
head(TempData)

# can get rid of row names by
rownames(TempData) <- NULL
head(TempData)

# convert the data to long format
require(reshape2) # load the reshape2 package

# wrangle the dataset into submission
MyWrangledData <- melt(TempData, id=c("Cultivation", "Block", "Plot", "Quadrat"), variable.name = "Species", value.name = "Count")
head(MyWrangledData); tail(MyWrangledData)

# assign the correct data types to each column
MyWrangledData[, "Cultivation"] <- as.factor(MyWrangledData[, "Cultivation"])
MyWrangledData[, "Block"] <- as.factor(MyWrangledData[, "Block"])
MyWrangledData[, "Plot"] <- as.factor(MyWrangledData[, "Plot"])
MyWrangledData[, "Quadrat"] <- as.factor(MyWrangledData[, "Quadrat"])
MyWrangledData[, "Count"] <- as.integer(MyWrangledData[, "Count"])
str(MyWrangledData)


