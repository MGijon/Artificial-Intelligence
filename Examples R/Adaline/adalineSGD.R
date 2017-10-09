## ==================== ##
##       ADALINE        ##
## ==================== ##

adalineSGD <- function(X, y, n_iter = 10, eta = 0.01) {
  
  # ADAptive LInear NEuron algorithms (Stochastic Gradient Descent)
  # ---------------------------------------------------------------
  # INPUT:
  # x : vector, variables
  # y : correct clasification
  # eta : tolerance rate, parameter for the uptate of the weights
  # niter : number of iterations
  # OUTPUT:
  # infodf : data frame that contains three vectors 
  #          (epoch, log(cost), error)
  # ---------------------------------------------------------------
  
  # Extends input vector and initialize extended weight
  X[, dim(X)[2] + 1] <- 1
  X <- as.matrix(X)
  w <- as.matrix( rep(0, dim(X)[2]) )
  
  # initialize cost values
  cost <- rep(0, n_iter)
  errors <- rep(0, n_iter)
  
  # loop through each epoch
  for (i in 1:n_iter) {
    
    # loop through each data point
    for ( j in sample(1:dim(X)[1], dim(X)[1], replace = FALSE) ) {
      
      # tracking the incorrect predictions
      z <- sum(w * X[j, ])
      
      # quantizer
      if(z < 0.0) {
        ypred <- -1
      } else {
        ypred <- 1
      }
      
      if (ypred != y[j]) {
        errors[i] = errors[i] + 1
      }
      
      # update weight
      w <-  w + eta * (y[j] -z) * X[j, ]
    }
    
    # compute cost function
    cost[i] <- sum( (y - X %*% w) ^2) / 2
  }
  
  # data frame consisting of cost and errror information
  infomatrix <- matrix( rep(0, 3 * n_iter), nrow = n_iter, ncol = 3)
  infomatrix[, 1] <- 1:n_iter
  infomatrix[, 2] <- log(cost)
  infomatrix[, 3] <- error
  
  infodf <- as.data.frame(infomatrix)
  names(infodf) <- c("epoch", "log(cost)", "error")
  
  return(infodf)
}

# source: https://rpubs.com/FaiHas/199387