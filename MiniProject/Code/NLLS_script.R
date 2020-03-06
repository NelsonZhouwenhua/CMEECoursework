# a separate script that does the NLLS fitting
# CID: 00731413
# Name: Wenhua Zhou

# load required packages
library("minpack.lm")

set.seed(00731413)
options(warn=-1)

# open the dataset from data_preparation step
df <- read.csv(file = '../Data/data.csv')
df$X = df$X + 1

# calculate starting values
startValA <- function(x,c){
  rmax <- 0
  for (i in 2:length(x)){
    r <- (c[i]-c[i-1])/(x[i]-x[i-1])
    if (r > rmax){
      rmax <- r
    }
  }
  return(rmax)
}

startValH <- function(x,c){
  return(1/(1.5* c[length(c)]- 0.5* c[length(c)-1]))
}

# consumption rate functions:
# model 1: quadratic
quad <- function(x,a,b,c){
  return( a* x^2 + b* x + c)
}

# model 2: cubic
cube <- function(x,a,b,c,d){
  return( a* x^3 + b* x^2 + c* x + d)
}

# model 3: Holling Type 2
Holling2 <- function(x,a,t){
  return((a*x)/(1+t*a*x))
}

# model 4: generalized Holling
HollingGen <- function(x,a,t,q){
  return((a*x^(q+1))/(1+t*a*x^(q+1)))
}


# NLLS fitting (individual)
# Quadratic fit , cubic fit, Holling type 2 fit and generalized Holling fit of consumption rates
N_quad <- rep(NA,nrow(df))
N_cubic <- rep(NA,nrow(df))
N_Holling2 <- rep(NA,nrow(df))
N_HollingGen <- rep(NA,nrow(df))
# AIC of different models
AIC_quad <- rep(NA,nrow(df))
AIC_cubic <- rep(NA,nrow(df))
AIC_Holling2 <- rep(NA,nrow(df))
AIC_HollingGen <- rep(NA,nrow(df))
# BIC of different models
BIC_quad <- rep(NA,nrow(df))
BIC_cubic <- rep(NA,nrow(df))
BIC_Holling2 <- rep(NA,nrow(df))
BIC_HollingGen <- rep(NA,nrow(df))
# R square of different models
R2_quad <- rep(NA,nrow(df))
R2_cubic <- rep(NA,nrow(df))
R2_Holling2 <- rep(NA,nrow(df))
R2_HollingGen <- rep(NA,nrow(df))


for (i in unique(df[,'ID'])){
  Data2Fit <- subset(df, ID == i)
  CubicFit <-NA
  Holling2Fit <- NA
  HollingGenFit <- NA
  # filter
  if (nrow(Data2Fit) > 4 & sum(is.na(Data2Fit$N_TraitValue)) + sum(is.na(Data2Fit$ResDensity))==0){
    # starting value of quadratic and model parameters to be random distribution with mean 0 and variance 1
    QuadFit <- nlsLM(N_TraitValue ~ quad(ResDensity, a, b, c), data = Data2Fit, start = list(a = rnorm(1,mean = mean(Data2Fit$N_TraitValue)), b = rnorm(1, mean = mean(Data2Fit$N_TraitValue)), c = rnorm(1, mean = mean(Data2Fit$N_TraitValue))))
    # cubic fit
    j1<- 0
    while (length(CubicFit)==1 && j1<20){
      CubicFit <- tryCatch({nlsLM(N_TraitValue ~ cube(ResDensity, a, b, c, d), data = Data2Fit, start = list(a = rnorm(1, mean = mean(Data2Fit$N_TraitValue)), b = rnorm(1, mean = mean(Data2Fit$N_TraitValue)), c = rnorm(1, mean = mean(Data2Fit$N_TraitValue)), d = rnorm(1, mean = mean(Data2Fit$N_TraitValue))))},
                           error = function(e){NA})
      j1 <- j1+1
    }
    # Holling2 Fit
    j2 <- 0
    while (length(Holling2Fit)==1 && j2<20){
      Holling2Fit <- tryCatch({nlsLM(N_TraitValue ~ Holling2(ResDensity, a, t), data = Data2Fit, start = list(a = startValA(Data2Fit$ResDensity,Data2Fit$N_TraitValue)*runif(1, min = 0.8, max = 1.2), t = startValH(Data2Fit$ResDensity,Data2Fit$N_TraitValue)*runif(1, min = 0.8, max = 1.2)))},
                              error = function(e){NA})
      j2 <- j2+1
    }
    # HollingGen fit
    j3 <- 0
    while (length(HollingGenFit)==1 && j3<20){
      HollingGenFit <- tryCatch({nlsLM(N_TraitValue ~ HollingGen(ResDensity, a, t, q), data = Data2Fit, start = list(a = startValA(Data2Fit$ResDensity,Data2Fit$N_TraitValue)*runif(1, min = 0.8, max = 1.2), t = startValH(Data2Fit$ResDensity,Data2Fit$N_TraitValue)*runif(1, min = 0.8, max = 1.2), q = runif(1)*3))},
                                error = function(e){NA})
      j3 <- j3+1
    }
      
    # calculate fitted value
    # calculate model AICs
    # calculate model BICs
    # calculate R square
    for (k in Data2Fit$X){
      N_quad[k] <- quad(df$ResDensity[k],coef(QuadFit)["a"],coef(QuadFit)["b"],coef(QuadFit)["c"])
      AIC_quad[k] <- AIC(QuadFit)
      BIC_quad[k] <- BIC(QuadFit)
      R2_quad[k] <- 1 - sum((Data2Fit$N_TraitValue-quad(Data2Fit$ResDensity,coef(QuadFit)["a"],coef(QuadFit)["b"],coef(QuadFit)["c"]))^2)/sum((Data2Fit$N_TraitValue- mean(Data2Fit$N_TraitValue))^2)
      if (length(CubicFit)!=1){
        N_cubic[k] <- cube(df$ResDensity[k],coef(CubicFit)["a"],coef(CubicFit)["b"],coef(CubicFit)["c"],coef(CubicFit)["d"])
        AIC_cubic[k] <- AIC(CubicFit)
        BIC_cubic[k] <- BIC(CubicFit)
        R2_cubic[k] <-  1 - sum((Data2Fit$N_TraitValue-cube(Data2Fit$ResDensity,coef(CubicFit)["a"],coef(CubicFit)["b"],coef(CubicFit)["c"],coef(CubicFit)["d"]))^2)/sum((Data2Fit$N_TraitValue- mean(Data2Fit$N_TraitValue))^2)
      }
      if (length(Holling2Fit)!=1){
        N_Holling2[k] <- Holling2(df$ResDensity[k],coef(Holling2Fit)["a"],coef(Holling2Fit)["t"])
        AIC_Holling2[k] <- AIC(Holling2Fit)
        BIC_Holling2[k] <- BIC(Holling2Fit)
        R2_Holling2[k] <- 1 - sum((Data2Fit$N_TraitValue-Holling2(Data2Fit$ResDensity,coef(Holling2Fit)["a"],coef(Holling2Fit)["t"]))^2)/sum((Data2Fit$N_TraitValue- mean(Data2Fit$N_TraitValue))^2)
      }
      if (length(HollingGenFit)!=1){
        N_HollingGen[k] <- HollingGen(df$ResDensity[k],coef(HollingGenFit)["a"],coef(HollingGenFit)["t"],coef(HollingGenFit)["q"])
        AIC_HollingGen[k] <- AIC(HollingGenFit)
        BIC_HollingGen[k] <- BIC(HollingGenFit)
        R2_HollingGen[k] <- 1 - sum((Data2Fit$N_TraitValue-HollingGen(Data2Fit$ResDensity,coef(HollingGenFit)["a"],coef(HollingGenFit)["t"],coef(HollingGenFit)["q"]))^2)/sum((Data2Fit$N_TraitValue- mean(Data2Fit$N_TraitValue))^2)
      }
    }
  } 
}


# exports the results to a csv for the plotting script to read
df$N_quad = N_quad
df$N_cubic = N_cubic
df$N_Holling2 = N_Holling2
df$N_HollingGen = N_HollingGen
df$AIC_quad = AIC_quad
df$AIC_cubic = AIC_cubic
df$AIC_Holling2 = AIC_Holling2
df$AIC_HollingGen = AIC_HollingGen
df$BIC_quad = BIC_quad
df$BIC_cubic = BIC_cubic
df$BIC_Holling2 = BIC_Holling2
df$BIC_HollingGen = BIC_HollingGen
df$R2_quad = R2_quad
df$R2_cubic = R2_cubic
df$R2_Holling2 = R2_Holling2
df$R2_HollingGen = R2_HollingGen


write.csv(df,'../Data/modelfitting_CRat.csv')







