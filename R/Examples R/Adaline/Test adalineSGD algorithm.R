adalineSGD <- function(X, y, n_iter = 10, eta = 0.01) {

  X[, dim(X)[2] + 1] <- 1
  X <- as.matrix(X)
  w <- as.matrix( rep(0, dim(X)[2]) )
  
  cost <- rep(0, n_iter)
  errors <- rep(0, n_iter)
  
  for (i in 1:n_iter) {
    
    for ( j in sample(1:dim(X)[1], dim(X)[1], replace = FALSE) ) {
      
      z <- sum(w * X[j, ])
      
      if(z < 0.0) {
        ypred <- -1
      } else {
        ypred <- 1
      }
      
      if (ypred != y[j]) {
        errors[i] = errors[i] + 1
      }
      
      w <-  w + eta * (y[j] -z) * X[j, ]
    }

    cost[i] <- sum( (y - X %*% w) ^2) / 2
  }
  
  infomatrix <- matrix( rep(0, 3 * n_iter), nrow = n_iter, ncol = 3)
  infomatrix[, 1] <- 1:n_iter
  infomatrix[, 2] <- log(cost)
  infomatrix[, 3] <- error
  
  infodf <- as.data.frame(infomatrix)
  names(infodf) <- c("epoch", "log(cost)", "error")
  
  return(infodf)
}


# Standardized vs non-standard data: Cost and error function

n_eta = 0.0001
n_iter = 100
result1 <- adalineSGD(X, y, n_iter, n_eta)
label <- rep("non-standard", dim(result1)[1])
result2 <- adalineSGD(X_std, y, n_iter, eta)
label <- rep("standard", dim(result2)[1])
result2 <- cbind(label, result2)

result2 <- adalineSGD(X_std, y, n_iter, eta)
label <- rep("standard", dim(result2)[1])
result2 <- cbind(label, result2)

df <- rbind(result1, result2)

# long format of data frame
dflong <- melt(df, id.vars=c("epoch", "label"))
head(dflong)

ggplot(dflong, aes(x=epoch, y=value)) + 
  geom_line(aes(color=label, linetype=label), size = 1) +
  facet_grid(variable ~ .) + xlab("Epoch #") + ylab("") +
  ggtitle("Cost and error function for a dataset \n and its standardized form: eta = 0.0001 (Stochastic Gradient Descent)")


# source: https://rpubs.com/FaiHas/199387

