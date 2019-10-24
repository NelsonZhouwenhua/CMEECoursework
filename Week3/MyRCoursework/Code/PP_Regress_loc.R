# R practicals
# write a csv of the same in PP_Regress with one more filter location

require(dplyr)
require(tidyr)

# read given data
MyDF <- read.csv("../Data/EcolArchives-E089-51-D1.csv")

# create empty dataframe
df <- data.frame(Feedingtype = double(),
                 Predatorlifestage = double(),
                 Location = double(),
                 Regressionslope = double(),
                 Regressionintercept = double(),
                 R2 = double(),
                 Fvalue = double(),
                 pvalue = double()
)

a <- levels(MyDF$Type.of.feeding.interaction)
b <- levels(MyDF$Predator.lifestage)
c <- levels(MyDF$Location)
# linear regression for each predator lifestage and feeding type
# put result into dataframe
for (i in 1:length(a)){
  for (j in 1:length(b)){
    for (k in 1:length(c)){
      df[(i-1) * length(b)*length(c) + (j-1)*length(c) + k , 1] <- a[i] # assign feeding type
      df[(i-1) * length(b)*length(c) + (j-1)*length(c) + k , 2] <- b[j] # assign lifestage
      df[(i-1) * length(b)*length(c) + (j-1)*length(c) + k , 3] <- c[k]
      # filter the dataframe
      smalldf <- dplyr::filter(MyDF, MyDF$Predator.lifestage == b[j], MyDF$Type.of.feeding.interaction==a[i], MyDF$Location == c[k])
      if (dim(smalldf)[1] <= 5){
        df[(i-1) * length(b)*length(c) + (j-1)*length(c) + k , 4:8] <- c("NA","NA","NA","NA","NA")
      }
      else{
        my_lm <- summary(lm ( log(Predator.mass) ~ log(Prey.mass), data = smalldf))
        df[(i-1) * length(b)*length(c) + (j-1)*length(c) + k , 4] <- my_lm$coefficients[1][1]
        df[(i-1) * length(b)*length(c) + (j-1)*length(c) + k , 5] <- my_lm$coefficients[2][1]
        df[(i-1) * length(b)*length(c) + (j-1)*length(c) + k , 6] <- my_lm$r.squared
        df[(i-1) * length(b)*length(c) + (j-1)*length(c) + k , 7] <- my_lm$fstatistic[1][1]
        df[(i-1) * length(b)*length(c) + (j-1)*length(c) + k , 8] <- my_lm$coefficients[2,4]
      }
    }
  }
}


# save the regression as a csv
write.csv(file='../Results/PP_Regress_loc_Results.csv', x=df)
