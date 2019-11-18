# Linear Fitting notes from notebook
# Week 5
# 29/10/2019
# Wenhua Zhou

# For starters, clear all variables and graphic devices and load necessary packages:
rm(list = ls())
graphics.off()

# install package for fitting linear models
install.packages("minpack.lm")
require("minpack.lm")

# create a fuction object for power law model
powMod <- function(x, a, b) {
  return(a * x^b)
}

# read data from directory
MyData <- read.csv("../Data/GenomeSize.csv")
head(MyData)

#subset data, remove NAs
Data2Fit <- subset(MyData,Suborder == "Anisoptera")

Data2Fit <- Data2Fit[!is.na(Data2Fit$TotalLength),] # remove NA's

# plot data
plot(Data2Fit$TotalLength, Data2Fit$BodyWeight)

# ggplot
library("ggplot2")
ggplot(Data2Fit, aes(x = TotalLength, y = BodyWeight)) + 
  geom_point(size = (3),color="red") + theme_bw() + 
  labs(y="Body mass (mg)", x = "Wing length (mm)")

# NLLS
PowFit <- nlsLM(BodyWeight ~ powMod(TotalLength, a, b), data = Data2Fit, start = list(a = .1, b = .1))
summary(PowFit)
#anova(PowFit)
Lengths <- seq(min(Data2Fit$TotalLength),max(Data2Fit$TotalLength),len=200)
coef(PowFit)["a"]
coef(PowFit)["b"]
Predic2PlotPow <- powMod(Lengths,coef(PowFit)["a"],coef(PowFit)["b"])
plot(Data2Fit$TotalLength, Data2Fit$BodyWeight)
lines(Lengths, Predic2PlotPow, col = 'blue', lwd = 2.5)
confint(PowFit)

# exercise
# (a)
# plot above plot in ggplot
Lengths <- seq(min(Data2Fit$TotalLength),max(Data2Fit$TotalLength),len=60)
#Predic2PlotPow <- powMod(Lengths,coef(PowFit)["a"],coef(PowFit)["b"])
ggplot(Data2Fit) + 
  geom_point(size = (3),color="red",aes(x = TotalLength, y = BodyWeight))+ 
  geom_line(color = 'blue', aes(x = Lengths, y = 3.94 * 10^-6 * Lengths^2.59), lwd = 1.5)
  theme_bw() + 
  labs(y="Body mass (mg)", x = "Wing length (mm)")

#(b)

#(c)
# model fittign with Zygoptera data subset
#subset data, remove NAs  
Data3Fit <- subset(MyData,Suborder == "Zygoptera")
Data3Fit <- Data3Fit[!is.na(Data3Fit$TotalLength),] # remove NA's
# NLLS  
PowFit1 <- nlsLM(BodyWeight ~ powMod(TotalLength, a, b), data = Data3Fit, start = list(a = .1, b = .1))
summary(PowFit1)
Lengths1 <- seq(min(Data3Fit$TotalLength),max(Data3Fit$TotalLength),len=38)
ggplot(Data3Fit) + 
  geom_point(size = (3),color="red",aes(x = TotalLength, y = BodyWeight))+ 
  geom_line(color = 'blue', aes(x = Lengths1, y = summary(PowFit1)$coefficients[1] * Lengths1^summary(PowFit1)$coefficients[2]), lwd = 1.5)
  theme_bw() + 
  labs(y="Body mass (mg)", x = "Wing length (mm)")
# (d)
PowFit2 <- lm(log(Data2Fit$BodyWeight) ~ log(Data2Fit$TotalLength), data = Data2Fit)
summary(PowFit2)
exp(PowFit2$coefficients[1]) # 7.37e-06 
PowFit2$coefficients[2] # 2.42
coef(PowFit)["a"] # 3.94e-06
coef(PowFit)["b"] # 2.59
# close results for two fitting but slightly different results

# (e)
# NLLS of HeadLength and ThoraxLength
PowFit <- nlsLM(HeadLength ~ powMod(ThoraxLength, a, b), data = Data2Fit, start = list(a = .1, b = .1))
Lengths <- seq(min(Data2Fit$ThoraxLength),max(Data2Fit$ThoraxLength),len=60)
ggplot(Data2Fit) + 
  geom_point(size = (3),color="red",aes(x = ThoraxLength, y = HeadLength))+ 
  geom_line(color = 'blue', aes(x = Lengths, y = coef(PowFit)["a"] * Lengths^coef(PowFit)["b"]), lwd = 1.5)
  #labs(y="Body mass (mg)", x = "Wing length (mm)") +
  theme_bw()
  
# Comparing Models
QuaFit <- lm(BodyWeight ~ poly(TotalLength,2), data = Data2Fit)
Predic2PlotQua <- predict.lm(QuaFit, data.frame(TotalLength = Lengths))
plot(Data2Fit$TotalLength, Data2Fit$BodyWeight)
lines(Lengths, Predic2PlotPow, col = 'blue', lwd = 2.5)
lines(Lengths, Predic2PlotQua, col = 'red', lwd = 2.5)
  
# calculate R residual
RSS_Pow <- sum(residuals(PowFit)^2)  # Residual sum of squares
TSS_Pow <- sum((Data2Fit$BodyWeight - mean(Data2Fit$BodyWeight))^2)  # Total sum of squares
RSq_Pow <- 1 - (RSS_Pow/TSS_Pow)  # R-squared value

RSS_Qua <- sum(residuals(QuaFit)^2)  # Residual sum of squares
TSS_Qua <- sum((Data2Fit$BodyWeight - mean(Data2Fit$BodyWeight))^2)  # Total sum of squares
RSq_Qua <- 1 - (RSS_Qua/TSS_Qua)  # R-squared value

RSq_Pow 
RSq_Qua

# AIC
n <- nrow(Data2Fit) #set sample size
pPow <- length(coef(PowFit)) # get number of parameters in power law model
pQua <- length(coef(QuaFit)) # get number of parameters in quadratic model

AIC_Pow <- n + 2 + n * log((2 * pi) / n) +  n * log(RSS_Pow) + 2 * pPow
AIC_Qua <- n + 2 + n * log((2 * pi) / n) + n * log(RSS_Qua) + 2 * pQua
AIC_Pow - AIC_Qua
AIC(PowFit) - AIC(QuaFit)

# exercise
# (a)
# BIC
BIC(PowFit) - BIC(QuaFit)
# power law model is better
  
# (b)
linear <- lm(Data2Fit$BodyWeight ~ Data2Fit$TotalLength)
Predic2PlotLinear <- predict.lm(linear, data.frame(TotalLength = Lengths))
plot(Data2Fit$TotalLength, Data2Fit$BodyWeight)
lines(Lengths, Predic2PlotPow, col = 'blue', lwd = 2.5)
lines(Lengths, Predic2PlotQua, col = 'red', lwd = 2.5)
lines(Lengths, linear$coefficients[1] + Lengths*linear$coefficients[2], col = 'green', lwd = 2.5)

AIC(linear) - AIC(PowFit)
# power law still wins

# (c)
linear <- lm(Data3Fit$BodyWeight ~ Data3Fit$TotalLength)

  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
