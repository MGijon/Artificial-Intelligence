# Multiclass Perceptron Classification implemetation 
# source: https://rpubs.com/FaiHas/197581

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


irisdataset <- iris[, c(1, 3, 5)]
names(irisdataset) <- c("sepal", "petal", "species")

library(ggplot2)
ggplot(irisdataset, aes(x = sepal, y = petal)) + geom_point(aes(colour = species, shape = species), size = 3) + xlab("sepal length") + ylab("petal legth") + ggtitle("Species vs sepal and petal lengths")

# subset of properies of flowers of iris data set
x <- iris[, 1:4]
head(x)
names(x) <- tolower(names(x))

# creates a new species label
y <- rep(-1, dim(x)[1])
y[iris[, 5] == "virginica"] <- 1

# compute and plot error
err <- perceptron(x, y, .01, 50)

# Error's graphic
plot(1:50, err, type = "l", lwd = 2, col = "red", xlab = "epoch #", ylab = "errors")
title("Errors in differentiating Virginica vs epoch - learning rate eta = 0.01")
