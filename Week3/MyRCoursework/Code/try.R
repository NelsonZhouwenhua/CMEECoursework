# usage of try function

# an example function
doit <- function(popn){
  x <- sample(popn, replace = TRUE)
  if(length(unique(x)) > 30) {#only take mean if sample was sufficient
    print(paste("Mean of this sample was:", as.character(mean(x))))
  } 
  else {
    stop("Couldn't calculate mean: too few unique values!")
  }
}

popn <- rnorm(50) #Generate your population

# lapply(1:15, function(i) doit(popn)) # repeat the sample exercise 15 times which causes error
result <- lapply(1:15, function(i) try(doit(popn), FALSE)) # use try to let lapply keep running  

# use loop can do the same thing
result <- vector("list", 15) #Preallocate/Initialize
for(i in 1:15) {
  result[[i]] <- try(doit(popn), FALSE)
}



