# a separate script that does the model plotting
# CID: 00731413
# Name: Wenhua Zhou

# load required packages
library("ggplot2")

# read the model fitting data
df1 <- read.csv(file = '../Data/modelfitting_CRat.csv')

# not display the warnings in plotting
options(warn=-1)

# filter out the Model fitting results with no fitting values for all four models
df1 <- df1[rowSums(is.na(df1[,c('N_quad','N_cubic','N_Holling2','N_HollingGen')])) != 4, ]

# plot the fit for different models
for (i in unique(df1[,'ID'])){
  Data2Fit <- subset(df1, ID == i)
  name <- paste0("../Results/plot/Functional_response_curve_", i ,".pdf")
  pdf(name)
  Myplot <- ggplot(Data2Fit, aes(x = ResDensity, y = N_TraitValue)) + 
    geom_point(size = 1) +
    geom_line(aes(ResDensity, N_quad, col = 'Quadratic'), alpha = 0.5) +
    geom_line(aes(ResDensity, N_cubic, col = 'Cubic'), alpha = 0.5) +
    geom_line(aes(ResDensity, N_Holling2, col = 'Holling 2'), alpha = 0.5) +
    geom_line(aes(ResDensity, N_HollingGen, col = 'General Holling'), alpha = 0.5) +
    scale_colour_manual(name = "Model:", 
                        #breaks = c("Quadratic", "Cubic", "Holling 2", "General Holling"),
                        values = c('Quadratic' = "red", 'Cubic' = "blue", 'Holling 2' = "green",'General Holling' = "orange")) +
    labs(x = "Resource Density", y = "Consumption rate") +
    theme_bw(base_size = 16)
  print(Myplot)
  dev.off()
}

# compute AIC between models
# use unique ID and count the number in each id
df_unique <- df1[!duplicated(df1[,c('ID')]),]
df_unique$number <- rep(0,nrow(df_unique))
for (i in 1:nrow(df1)){
  df_unique$number[df_unique$ID == df1$ID[i]] = df_unique$number[df_unique$ID == df1$ID[i]] +1
}

AIC_quad_total <- sum(!is.na(df_unique$AIC_quad))
AIC_cubic_total <- sum(!is.na(df_unique$AIC_cubic))
AIC_Holling2_total <- sum(!is.na(df_unique$AIC_Holling2))
AIC_HollingGen_total <- sum(!is.na(df_unique$AIC_HollingGen))

AIC_quad_bestfit <- 0
AIC_cubic_bestfit <- 0
AIC_Holling2_bestfit <- 0
AIC_HollingGen_bestfit <- 0

for (i in 1:nrow(df_unique)){
  AIC <- df_unique[i,c('AIC_quad','AIC_cubic','AIC_Holling2','AIC_HollingGen')]
  AIC[is.na(AIC)] <- 10000
  AIC_min <- min(AIC)
  if (AIC[1]- AIC_min < 2){
    AIC_quad_bestfit <- AIC_quad_bestfit + 1
  }
  if (AIC[2]- AIC_min < 2){
    AIC_cubic_bestfit <- AIC_cubic_bestfit + 1
  }
  if (AIC[3]- AIC_min < 2){
    AIC_Holling2_bestfit <- AIC_Holling2_bestfit + 1
  }
  if (AIC[4]- AIC_min < 2){
    AIC_HollingGen_bestfit <- AIC_HollingGen_bestfit + 1
  }
}

AIC_quad_fitrate <- AIC_quad_bestfit/AIC_quad_total
AIC_cubic_fitrate <- AIC_cubic_bestfit/AIC_cubic_total
AIC_Holling2_fitrate <- AIC_Holling2_bestfit/AIC_Holling2_total
AIC_HollingGen_fitrate <- AIC_HollingGen_bestfit/AIC_HollingGen_total

# AICc

AICc_quad_total <- sum(!is.na(df_unique$AIC_quad))
AICc_cubic_total <- sum(!is.na(df_unique$AIC_cubic))
AICc_Holling2_total <- sum(!is.na(df_unique$AIC_Holling2))
AICc_HollingGen_total <- sum(!is.na(df_unique$AIC_HollingGen))

AICc_quad_bestfit <- 0
AICc_cubic_bestfit <- 0
AICc_Holling2_bestfit <- 0
AICc_HollingGen_bestfit <- 0

for (i in 1:nrow(df_unique)){
  AICc <- df_unique[i,c('AIC_quad','AIC_cubic','AIC_Holling2','AIC_HollingGen')]
  AICc[is.na(AICc)] <- 10000
  # calculate AICc rather than AIC
  AICc[1] <- AICc[1] + 24/(df_unique$number-4)
  AICc[2] <- AICc[2] + 40/(df_unique$number-5)
  AICc[3] <- AICc[3] + 12/(df_unique$number-3)
  AICc[4] <- AICc[4] + 24/(df_unique$number-4)
  AICc_min <- min(AICc)
  if (AICc[1]- AICc_min < 2){
    AICc_quad_bestfit <- AICc_quad_bestfit + 1
  }
  if (AICc[2]- AICc_min < 2){
    AICc_cubic_bestfit <- AICc_cubic_bestfit + 1
  }
  if (AICc[3]- AICc_min < 2){
    AICc_Holling2_bestfit <- AICc_Holling2_bestfit + 1
  }
  if (AICc[4]- AICc_min < 2){
    AICc_HollingGen_bestfit <- AICc_HollingGen_bestfit + 1
  }
}

AICc_quad_fitrate <- AICc_quad_bestfit/AICc_quad_total
AICc_cubic_fitrate <- AICc_cubic_bestfit/AICc_cubic_total
AICc_Holling2_fitrate <- AICc_Holling2_bestfit/AICc_Holling2_total
AICc_HollingGen_fitrate <- AICc_HollingGen_bestfit/AICc_HollingGen_total
