##
##  Iris dataset and preprocesing:
##  ==============================

# load the iris dataset
data(iris)
str(iris)

# sepal and petal dimensions
X <- iris[1:100, 1:4]
names(X) <- tolower(names(X))

# initialize X_std dataframe
X_std <- iris[1:100, 1:4]

# define standardized data set
for (i in 1:4) {
  X_std[, i] <- (X[, i]-mean(X[, i]))/sd(X[, i])
}

# first few rows of both data frames
head(X)


head(X_std)


# binary classification vector according to species: setosa(-1), versicolor(1)
y <- rep(1, 100)
y[which(iris[, 5] == "setosa")] <- -1
y[which(iris[, 5] == "versicolor")] <- 1

# pre-process non-separable data points (ns stands for non-separable)
# sepal and petal dimensions
Xns <- iris[51:150, 1:4]
names(Xns) <- tolower(names(Xns))

# initialize X_std dataframe
Xns_std <- iris[51:150, 1:4]

# define standardized data set
for (i in 1:4) {
  Xns_std[, i] <- (Xns[, i]-mean(Xns[, i]))/sd(Xns[, i])
}

# binary classification vector according to species: setosa(-1), versicolor(1)
yns <- rep(1, 100)
l1 <- sum(iris[, 5] == "versicolor")
l2 <- sum(iris[, 5] == "virginica")
yns[1:l1] <- -1
yns[(l1+1):(l1+l2)] <- 1
dim(Xns)


length(yns)


##
##  ADAptive LInear NEuron algorithms (Gradient Descent)
##  ====================================================

adalineGD <- function(X, y, n_iter=10, eta=0.01) {
  
  # extend input vector and initialize extended weight
  X[, dim(X)[2] + 1] <- 1 
  X <- as.matrix(X)
  w <- as.matrix(rep(0, dim(X)[2]))
  
  # initialize cost values - gets updated according to epochnums -                number of epochs
  cost <- rep(0, n_iter)
  error <- rep(0, n_iter)
  
  # loop over the number of epochs
  for (i in 1:n_iter) {
    
    # find the number of wrong prediction before weight update
    for (j in 1:dim(X)[1]) {
      
      # compute net input
      z <- sum(w * X[j, ])
      
      # quantizer
      if(z < 0.0) {
        ypred <- -1
      } else {
        ypred <- 1
      }
      
      # comparison with actual labels and counting error
      if(ypred != y[j]) {
        error[i] <- error[i] + 1
      }
    }
    cost[i] <- sum((y - X %*% w)^2)/2
    
    # update weight according to gradient descent
    w <- w + eta*t(X) %*% (y - X %*% w)
  }
  
  # data frame consisting of cost and error info
  infomatrix <- matrix(rep(0, 3 * n_iter), nrow = n_iter, ncol = 3)
  infomatrix[, 1] <- 1:n_iter
  infomatrix[, 2] <- log(cost)
  infomatrix[, 3] <- error
  
  infodf <- as.data.frame(infomatrix)
  names(infodf) <- c("epoch", "log(cost)", "error")
  
  return(infodf)
}

##
##  Cost and Error function
##  =======================

library(ggplot2)
library(reshape2)

# Standardized vs non-standard data: Cost and error function
eta <- 0.0001
n_iter <- 100

result1 <- adalineGD(X, y, n_iter, eta)
label <- rep("non-standard", dim(result1)[1])
result1 <- cbind(label, result1)

result2 <- adalineGD(X_std, y, n_iter, eta)
label <- rep("standard", dim(result2)[1])
result2 <- cbind(label, result2)

df <- rbind(result1, result2)

# long format of data frame
dflong <- melt(df, id.vars = c("epoch", "label"))
head(dflong)

ggplot(dflong, aes(x=epoch, y=value)) + 
  geom_line(aes(color=label, linetype=label), size = 1) +
  facet_grid(variable ~ .) + xlab("Epoch #") + ylab("") +
  ggtitle("Cost and error function for a dataset \n and its standardized form: eta = 0.0001")


# source : https://rpubs.com/FaiHas/199387
