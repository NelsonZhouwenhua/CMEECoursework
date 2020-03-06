# a script that imports the data and prepapres it for NLLS fitting.
# CID: 00731413
# Name: Wenhua Zhou

# read the data
data <- read.csv(file = '../Data/CRat.csv')

# Create unique ids to identify unique dataset
#data[, "unique_ID"] <- seq.int(nrow(data))
#data = data[,c(ncol(data),seq(ncol(data)-1))]

# filter out datasets with less than x data points, where x is the minimum number
# needed to fit the models
# check the columns with missing value more than 5% 
for (i in 1:ncol(data)){
  if (sum(is.na(data[,i])) > nrow(data)*0.05){
    print('Column names:')
    print(colnames(data)[i])
    print('Number of missing values:')
    print(sum(is.na(data[,i])))
  }
}

# deal with missing and other problematic data values


# save the modified data to one csv
write.csv(data,'../Data/modified_CRat.csv')
