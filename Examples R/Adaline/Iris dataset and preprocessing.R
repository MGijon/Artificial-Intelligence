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


# source : https://rpubs.com/FaiHas/199387

