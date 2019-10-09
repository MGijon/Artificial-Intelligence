## ==================== ##
##       ADALINE        ##
## ==================== ##

adalineGD <- function(X, y, n_iter = 10, eta = 0.01) {
  
  # ADAptive LInear NEuron algorithms (Gradient Descent)
  # ----------------------------------------------------
  # INPUT:
  # x : vector, variables
  # y : correct clasification
  # eta : tolerance rate, parameter for the uptate of the weights
  # niter : number of iterations
  # OUTPUT:
  # infodf : data frame that contains three vectors 
  #          (epoch, log(cost), error)
  # ----------------------------------------------------
  
  # Extends input vector and initialize extended weight
  X[, dim(X)[2] + 1] <- 1
  X <- as.matrix(X)
  w <- as.matrix( rep(0, dim(X)[2]) )
  
  # initialize cost values
  cost <- rep(0, n_iter)
  errors <- rep(0, n_iter)
  
  # loop over the number of epochs
  for (i in 1:dim(X)[1]) {
    
    # find the number of wrong prediction before weight update
    for (j in 1:dim(X)[1]) {
      
      # compute net imput 
      z <- sum(w * X[j, ])
    
      # quantizer
      if (z < 0.0) {
        ypred <- -1
      } else {
        ypred <- 1
      }
      
      # comparison with actual labels and counting error
      if (ypred != y[j]) {
        errors[i] <- errors[i] + 1
      }
    } 
    cost[i] <- sum( (y - X %*% w)^2 )/ 2
    
    # update weight accordingto gradiet descent
    w <- w + eta*t(x) %*% (y - X %*% w)
  }
  
  # data frame consisting of cost and errror infotrmation
  infomatrix <- matrix( rep(0, 3 * n_iter), nrow = n_iter, ncol = 3)
  infomatrix[, 1] <- 1:n_iter
  infomatrix[, 2] <- log(cost)
  infomatrix[, 3] <- error
  
  infodf <- as.data.frame(infomatrix)
  names(infodf) <- c("epoch", "log(cost)", "error")
  
  return(infodf)
  }

# source: https://rpubs.com/FaiHas/199387

