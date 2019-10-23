# example of the computational difference between not-allocated and pre-allocated vector loop

# function of not-allocated vector loop
NotAllocated <- function(n){
  a <- NA
  for (i in 1:n) {
    a <- c(a, i)
    # no need to print
    # print(a)
    # print(object.size(a))
  }
  
}

# function with pre-allocated vector loop
PreAllocated <- function(n){
  a <- rep(NA, n)
  for (i in 1:n) {
    a[i] <- i
    # no need to print
    # print(a)
    # print(object.size(a))
  }  
}

print("Loop of not allocated vector, with sample size 10000, the time taken is:")
#print(system.time(NotAllocated(100000))) # use n = 100000 and 10000
print(system.time(NotAllocated(10000)))
print("Loop of pre-allocated vector, with sample size 10000, the time taken is:")
#print(system.time(PreAllocated(100000)))
print(system.time(PreAllocated(10000))) # use n = 100000 and 10000
# as n goes large pre-allocated loop is taking only slightly more time
# but not allocated vector takes way much time than pre-allocated vector