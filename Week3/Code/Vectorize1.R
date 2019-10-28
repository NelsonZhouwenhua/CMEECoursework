# example of computational difference between for loops and in-built vectorized function
M <- matrix(runif(1000000),1000,1000)

SumAllElements <- function(M){
  Dimensions <- dim(M)
  Tot <- 0
  for (i in 1:Dimensions[1]){
    for (j in 1:Dimensions[2]){
      Tot <- Tot + M[i,j]
    }
  }
  return (Tot)
}

# print time using loops
print("Using loops, the time taken is:")
print(system.time(SumAllElements(M)))

# print time using in-built vectorized function
print("Using the in-built vectorized function, the time taken is:")
print(system.time(sum(M)))