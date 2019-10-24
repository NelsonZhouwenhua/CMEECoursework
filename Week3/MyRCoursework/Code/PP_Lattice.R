# R practicals
# output 3 pdf files of lattice graphs
# calculate mean and median by feeding type

# read given data
MyDF <- read.csv("../Data/EcolArchives-E089-51-D1.csv")


library(lattice)
# lattice plot of log predator mass
pdf("../Results/Pred_Lattice.pdf", # Open blank pdf page using a relative path
    11.7, 8.3) # These numbers are page dimensions in inches
densityplot(~log(Predator.mass) | Type.of.feeding.interaction, data=MyDF,
     xlab="Logarthms of Predator Body Mass (g)", ylab="Density", main = "Lattice graph of logarithm Predator mass") 
graphics.off(); #you can also use dev.off()

# prey mass needs to be calculated with unit
# given the mass unit only contains g and mg by unique(),
# only calculation is to multiply mass with unit "mg" by 0.001 to unified the units
for (i in 1:length(MyDF$Prey.mass)){
  if (MyDF$Prey.mass.unit[i] == 'mg'){
    MyDF$Prey.mass[i] <- MyDF$Prey.mass[i]/1000
  }
  else
    MyDF$Prey.mass[i] <- MyDF$Prey.mass[i]
}

# lattice plot of log prey mass
pdf("../Results/Prey_Lattice.pdf", # Open blank pdf page using a relative path
    11.7, 8.3) # These numbers are page dimensions in inches
densityplot(~log(PreyMass) | Type.of.feeding.interaction, data = MyDF,
            xlab="Logarthms of Prey Body Mass", ylab="Density", main = "Lattice graph of logarithm Prey mass") 
graphics.off(); #you can also use dev.off()

# lattice plot of log ratio of prey mass over predator mass
pdf("../Results/SizeRatio_Lattice.pdf", # Open blank pdf page using a relative path
    11.7, 8.3) # These numbers are page dimensions in inches
densityplot(~log(PreyMass/Predator.mass) | Type.of.feeding.interaction, data = MyDF,
            xlab="Logarthms of mass ratio", ylab="Density", main = "Lattice graph of logarithm mass ratio") 
graphics.off();

# calculate mean and median by feeding type:
# create empty dataframe
df <- data.frame(Feedingtype = character(),
                 MeanLogPredatorMass = double(),
                 MedianLogPredatorMass = double(),
                 MeanLogPreyMass = double(),
                 MedianLogPreyMass = double(),
                 MeanLogMassRatio = double(),
                 MedianLogMassRatio = double()
                 )

# calculate mean and median
for (i in 1:length(levels(MyDF$Type.of.feeding.interaction))){
  smalldf <- subset(MyDF, MyDF$Type.of.feeding.interaction == levels(MyDF$Type.of.feeding.interaction)[i])
  MeanPreM <- log(mean(smalldf$Predator.mass))
  MedPreM <- log(median(smalldf$Predator.mass))
  MeanPreyM <- log(mean(smalldf$Prey.mass))
  MedPreyM <- log(median(smalldf$Prey.mass))
  MeanRatio <- log(mean(smalldf$Prey.mass/smalldf$Predator.mass))
  MedianRatio <- log(median(smalldf$Prey.mass/smalldf$Predator.mass))
  df[i,2:7] <- c(MeanPreM, MedPreM, MeanPreyM, MedPreyM, MeanRatio, MedianRatio)
}
df[,1] <- levels(MyDF$Type.of.feeding.interaction)


# save file
write.csv(file='../Results/PP_Results.csv', x=df)

