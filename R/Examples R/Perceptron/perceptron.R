## ==================== ##
##     PERCEPTRON       ##
## ==================== ##

perceptron <- function(x, y, eta, niter){
  
  # Perceptron algorithm implementation
  # -----------------------------------
  # INPUT:
  # x : vector, variables
  # y : correct clasification
  # eta : tolerance rate, parameter for the uptate of the weights
  # niter : number of iterations
  # OUTPUT:
  # errors : vector with the error for every iteration
  # -----------------------------------
  
  # Create a weight vector
  weight <- rep(0, dim(x)[2] + 1)
  errors <- rep(0, niter)
  
  # loop over number of epoch niter
  for (jj in 1:niter) {
    # loop through training data set
    for (ii in 1:length(y)) {
      # Heavyside activation function to binary binaly labeled precict
      z <- sum( weight[ 2:length(weight) ] * as.numeric(x[ii, ]) ) + weight[1]
      if (z < 0) {
        ypred <- -1
      } else {
        ypred <- 1
      }
      
      # update weights
      weight.diff <- eta * ( y[ii] - ypred ) * c(1, as.numeric( x[ii, ] ))
      weight <- weight + weight.diff
      
      # update error vector
      if ( (y[ii] - ypred) != 0.0) {
        errors[jj] <- errors[jj] + 1
      }
      
    }
  }
  
  print(weight)
  return(errors)
}

# source: https://rpubs.com/FaiHas/197581