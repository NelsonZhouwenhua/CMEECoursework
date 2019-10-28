# R practicals
# output the given figure 
# do linear regression of predator type
# write csv of linear regression data

require(dplyr)
require(tidyr)

# read given data
MyDF <- read.csv("../Data/EcolArchives-E089-51-D1.csv")

# ggplot
p <- ggplot(MyDF, aes(x = log(Predator.mass),
                      y = log(Prey.mass),
                      colour = Predator.lifestage),
                      xlab = "Prey Mass in grams", ylab = "Predator Mass in grams"
            
            )

# separate plot
p <- p + facet_grid(Type.of.feeding.interaction ~ .)

# add labels
p <- p + xlab("Prey Mass in grams") + ylab("Predator Mass in grams")

# point and linear regression
p  <- p  + geom_point(size=I(2), shape=I(3)) + theme(legend.position="bottom",
                                                    legend.direction = "horizontal",
                                                    legend.box = "horizontal",
                                                    )
p <- p + stat_smooth(method='lm',fullrange = TRUE)

# create empty dataframe
df <- data.frame(Feedingtype = double(),
                 Predatorlifestage = double(),
                 Regressionslope = double(),
                 Regressionintercept = double(),
                 R2 = double(),
                 Fvalue = double(),
                 pvalue = double()
)

a <- levels(MyDF$Type.of.feeding.interaction)
b <- levels(MyDF$Predator.lifestage)
# linear regression for each predator lifestage and feeding type
# put result into dataframe
for (i in 1:length(a)){
  for (j in 1:length(b)){
    df[(i-1) * length(b) + j, 1] <- a[i] # assign feeding type
    df[(i-1) * length(b) + j, 2] <- b[j] # assign lifestage
    # filter the dataframe
    smalldf <- dplyr::filter(MyDF, MyDF$Predator.lifestage == b[j], MyDF$Type.of.feeding.interaction==a[i])
    if (dim(smalldf)[1] <= 5){
      df[(i-1) * length(b) + j, 3:7] <- c("NA","NA","NA","NA","NA")
    }
    else{
    my_lm <- summary(lm ( log(Predator.mass) ~ log(Prey.mass), data = smalldf))
    df[(i-1) * length(b) + j, 3] <- my_lm$coefficients[1][1]
    df[(i-1) * length(b) + j, 4] <- my_lm$coefficients[2][1]
    df[(i-1) * length(b) + j, 5] <- my_lm$r.squared
    df[(i-1) * length(b) + j, 6] <- my_lm$fstatistic[1][1]
    df[(i-1) * length(b) + j, 7] <- my_lm$coefficients[2,4]
    }
  }
}


# a little complaint about this weeks coursework:
# it is not fun! Some questiones are not clear!
# just to check if you will read our code carefully enough
# by the way I guess not :P

# save the image as a pdf
pdf("../Results/PP_Regress.pdf")
print(p)
dev.off()

# save the regression as a csv
write.csv(file='../Results/PP_Regress_Results.csv', x=df)