# R practicals
# read data and compute correlation and p-value

# read data from KeyWestAnnualMeanTemperature.Rdata
load(file = "/home/nelson/Documents/CMEECoursework/Week3/MyRCoursework/Data/KeyWestAnnualMeanTemperature.RData")

# correlation
correlation <- cor(ats[,2][1:99],ats[,2][2:100])

# function of compute randomly permuting time series and calculate correlation
random_correlation <- function(x){
  a <- sample(x[,2],100) # random sample the 100 years of time series
  return(cor(a[1:99],a[2:100]))p # return the calculated correlation
}

# calculate the random correlation 10000 times
RandCor <- sapply(1:10000, function(i) random_correlation(ats)) 

# calculate the fraction of the correlation coefficients(p-value)
p <- sum(RandCor > correlation)/10000