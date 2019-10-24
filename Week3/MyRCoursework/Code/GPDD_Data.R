# R practicals
# use maps package to map

# install maps
install.packages('maps')
library(maps)

# load GPDD data
load('../Data/GPDDFiltered.RData')

# create world map
map(database = "world")

# point out all the location on map
for (i in 1:dim(gpdd)[1]){
  points(gpdd[i,3],gpdd[i,2],col=2,pch=18)
}

# from the map most points are in North America and Europe,
# only 1 point in South Africa and 1 point in East Asia
# when we do analysis, these two points are highly-likely
# to affect the results a lot which may cause bias.