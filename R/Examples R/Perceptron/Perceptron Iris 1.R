# Perceptron implemetation 
# source: https://rpubs.com/FaiHas/197581

# Load the Iris data set
data(iris)

# only versicolor and setosa
# only the sepal and petal lengths

irissub <- iris[1:100, c(1, 3, 5)]
names(irissub) <- c("sepal", "petal", "species")
head(irissub)

# plot the data
library(ggplot2)

ggplot(irissub, aes(x = sepal, y = petal)) + geom_point( aes(colour = species, shape = species), size = 3 ) + xlab("sepal length") + ylab("petal length") + ggtitle("Species vs sepal and petal lengths")

# add a binary label

irissub[, 4] <- 1
irissub[ irissub[, 3] == "setosa", 4] <- -1

x <- irissub[, c(1, 2)]
y <- irissub[, 4]

head(x)
head(y)

## ==================== ##
##     PERCEPTRON       ##
## ==================== ##

perceptron <- function(x, y, eta, niter){
  
  weight <- rep(0, dim(x)[2] + 1)
  errors <- rep(0, niter)
  
  for (jj in 1:niter) {
    for (ii in 1:length(y)) {
      z <- sum( weight[ 2:length(weight) ] * as.numeric(x[ii, ]) ) + weight[1]
      if (z < 0) {
        ypred <- -1
      } else {
        ypred <- 1
      }
      
      weight.diff <- eta * ( y[ii] - ypred ) * c(1, as.numeric( x[ii, ] ))
      weight <- weight + weight.diff
      
      if ( (y[ii] - ypred) != 0.0) {
        errors[jj] <- errors[jj] + 1
      }
    }
  }
  
  print(weight)
  return(errors)
}

err <- perceptron(x, y, 1, 10)


plot(1:10, err, type = "l", lwd = 2, col = "red", xlab = "epoch #", ylab = "errors")
title("Errors vs epoch - learning rate eta = 1")
