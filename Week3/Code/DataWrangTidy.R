# R practicals
# use dplyr and tidyr to do the data wrangling steps

# load the data in R
MyData <- as.matrix(read.csv("../Data/PoundHillData.csv",header = F,  stringsAsFactors = F))
MyMetaData <- read.csv("../Data/PoundHillMetaData.csv",header = T,  sep=";", stringsAsFactors = F)

# have a look at the metadata file
MyMetaData

# replace blanks with zeros
MyData[MyData == ""] = 0

# use dplyr and tidyr for data wrangling
# transpose the data
require(dplyr)
require(tidyr)
MyData <- t(MyData) 

# check and assign the column names
colnames(MyData) <- MyData[1,]

# create a temporary dataframe without the column names
TempData <- dplyr::tbl_df(MyData[-1,]) # do not convert columns to factor

# can get rid of row names by
rownames(TempData) <- NULL


# convert the data to long format
# wrangle the dataset into submission
MyWrangledData <- tidyr::gather(TempData,"Species","Count",5:45)

