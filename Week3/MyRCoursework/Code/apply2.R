# example of another apply functions

SomeOperation <- function(v){ # (What does this function do?)
  if (sum(v) > 0){
    return (v * 100) # if the sum of input greater than 0, return 100*input
  }
  return (v) # otherwise return same input
}

M <- matrix(rnorm(100), 10, 10)
print (apply(M, 1, SomeOperation))