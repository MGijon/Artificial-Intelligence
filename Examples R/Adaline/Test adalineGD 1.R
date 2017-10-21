##
## Iris dataset and preprocesing:
## ==============================

data (iris)

X <- iris[1:100, 1:4]
names(X) <- tolower(names(X))

X_std <- iris[1:100, 1:4]

for (i in 1:4){
  X_std[, i] <- (X[, i] - mean(X[, i])) / sd(X[, i])
}

Y <- rep(1, 100)
Y[which(iris[, 5] == "setosa")] <- -1
Y[which(iris[, 5] == "versicolor")] <- 1

Xns <- iris[51:150, 1:4]
names(Xns) <- tolower(names(Xns))

Xns_std <- iris[51:150, 1:4]

for (i in 1:4){
  Xns_std[, i] <- (Xns_std[, i] - mean(Xns_std[, i])) / sd(Xns_std[, i])
}

l1 <- sum(iris[, 5] == 'versicolor')
l2 <- sum(iris[, 5] == 'virginica')
yns[1:l1] <- -1
yns[(l1 + 1): (l1 +l2)] <- 1

## ==============================

##
## ADAptive LInear NEuron algorithms (Gradient Descent)
## ====================================================

adalineGD <- function(X, y, n_iter = 10, eta = 0.01) {
  
  X[, dim(X)[2] + 1] <- 1
  X <- as.matrix(X)
  w <- as.matrix( rep(0, dim(X)[2]) )
  
  cost <- rep(0, n_iter)
  errors <- rep(0, n_iter)
  
  for (i in 1:dim(X)[1]) {
    
    for (j in 1:dim(X)[1]) {
      
      z <- sum(w * X[j, ])
      
      if (z < 0.0) {
        ypred <- -1
      } else {
        ypred <- 1
      }
      
      if (ypred != y[j]) {
        errors[i] <- errors[i] + 1
      }
    } 
    cost[i] <- sum( (y - X %*% w)^2 )/ 2
    
    w <- w + eta*t(x) %*% (y - X %*% w)
  }
  
  infomatrix <- matrix( rep(0, 3 * n_iter), nrow = n_iter, ncol = 3)
  infomatrix[, 1] <- 1:n_iter
  infomatrix[, 2] <- log(cost)
  infomatrix[, 3] <- error
  
  infodf <- as.data.frame(infomatrix)
  names(infodf) <- c("epoch", "log(cost)", "error")
  
  return(infodf)
}

## ====================================================

library(ggplot2)
library(reshape2)

# Standarized vs non-standard data : Cost and error Funcionn
eta <- 0.0001
n_iter = 100

result1 <- adalineGD(X, y, n_iter, eta)
label <- rep("non_standard", dim(result1)[1])
result1 <- cbind(label, result1)

result2 <- adalineGD(X_std, y, n_iter, eta)
label <- rep("standard", dim(result2)[1])
result2 <- cbind(label, result2)

df <- rbind(result1, result2)

# long format of data frame
df.long <- melt(df, id.vars = c("epoch", "label"))
head(df.long)








# source : https://rpubs.com/FaiHas/199387
