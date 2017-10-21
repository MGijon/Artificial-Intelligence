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
## 
##

library(ggplot2)
library(reshape2)

# set the number of sweeps through the entire data set 
n_iter <- 50

# the list of learning rates that interests me
eta <- c("0.00005", "0.0001", "0.00025", "0.0005")

# initialize data frames before looping
# adaline applied before standardizing data
result <- adalineGD(X, y, n_iter, as.numeric(eta[1]))
learnrate <- rep(eta[1], dim(result)[1])
result <- cbind(learnrate, result)

# adaline applied after standardizing data
result_std <- adalineGD(X_std, y, n_iter, as.numeric(eta[1]))
learnrate_std <- rep(eta[1], dim(result_std)[1])
result_std <- cbind(learnrate_std, result_std)

# updating the dataframe by row binding cost and error function for each new learning rate
df <- result
df_std <- result_std

# Standardized vs non-standard data: Cost and error function
for(i in 2:length(eta)) {
  
  # adaline applied before standardizing data
  result <- adalineGD(X, y, n_iter, as.numeric(eta[i]))
  learnrate <- rep(eta[i], dim(result)[1])
  result <- cbind(learnrate, result)
  
  # adaline applied after standardizing data
  result_std <- adalineGD(X_std, y, n_iter, as.numeric(eta[i]))
  learnrate_std <- rep(eta[i], dim(result_std)[1])
  result_std <- cbind(learnrate_std, result_std)
  
  # updating the dataframe by row binding cost and error function for each new learning rate
  df <- rbind(df, result)
  df_std <- rbind(df_std, result_std)
}

# long format of data frame
dflong <- melt(df, id.vars=c("epoch", "learnrate"))
df_stdlong <- melt(df_std, id.vars=c("epoch", "learnrate_std"))

head(dflong)

head(df_stdlong)


g <- ggplot(dflong, aes(x=epoch, y=value)) +
  geom_line(aes(color = learnrate, linetype = learnrate), size = 1) +
  facet_grid(variable ~ ., scales="free") + xlab("Epoch #") + ylab("") +
  ggtitle("Cost and error function convergence for \n varying learning rates")
head(df_stdlong)

g_std <- ggplot(df_stdlong, aes(x=epoch, y=value)) +
  geom_line(aes(color = learnrate_std, linetype = learnrate_std), size = 1) +
  facet_grid(variable ~ ., scales="free") + xlab("Epoch #") + ylab("") +
  ggtitle("Cost and error function convergence for \n varying learning rates - standardized data")

# print plots
print(g)